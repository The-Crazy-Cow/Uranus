import click
from dataclasses import dataclass,field
from typing import List,Callable, Optional


"""
if __name__ == "__main__":
    console = Console()
    
    # On enregistre la commande d'un coup propre
    console.add_command(config=harden_setup, behavior=run_hardening)
    
    # On démarre le script
    console.launch()

"""

class Console:
    """Manages the CLI IO operations, formatting, and command registration."""

    def __init__(self, title: str = "Uranus",synopsis: str ="Ultimate Security Hardening Tool for Linux"):
        @click.group()
        def cli():
            pass
        
        cli.__doc__ = f"{title} - {synopsis}."
        self._cli = cli

    def print_error(self, string: str):
        """Prints a critical error message in bold red."""
        click.echo(click.style(f"[-] ERROR: {string}", fg="red", bold=True))

    def print_info(self, string: str):
        click.echo(click.style(f"[*] INFO: {string}", fg="cyan"))

    def format_green(self, string: str) -> str:
        """Returns a string formatted in bold green (e.g., for success statuses)."""
        return click.style(string, fg="green", bold=True)

    def format_red(self, string: str) -> str:
        return click.style(string, fg="red", bold=True)

    def add_command(self, config: 'CommandConfig', behavior: Callable):
        """Builds a command from a configuration and registers it into the console."""

        builder = CommandBuilder(config, behavior)
        click_command = builder.build()
        
        self._cli.add_command(click_command)

    def launch(self):
        """Starts the CLI application execution loop."""
        self._cli()

@dataclass
class OptionConfig:
    """configuration command argument options"""
    name: str         
    is_flag: bool = True
    help_text: str = ""

@dataclass
class CommandConfig:
    name: str                                     
    help_text: str                               
    choices: List[str]                           
    options: List[OptionConfig] = field(default_factory=list)

class CommandBuilder:
    def __init__(self, config: CommandConfig, behavior: Callable):
        self.config = config
        self.behavior = behavior  

    def build(self) -> click.Command:
        
        cmd_callback = click.command(name=self.config.name, help=self.config.help_text)(self.behavior)
        
        cmd_callback = click.argument(
            'module', 
            type=click.Choice(self.config.choices)
        )(cmd_callback)
        
        for opt in self.config.options:
            cmd_callback = click.option(
                opt.name, 
                is_flag=opt.is_flag, 
                help=opt.help_text
            )(cmd_callback)
            
        return cmd_callback