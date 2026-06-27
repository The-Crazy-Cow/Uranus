#test the console command's handle behavior command : 28/06/2026

from click.testing import CliRunner
from utils.Console import Console, CommandConfig, OptionConfig
from utils.shared import console

test_config = CommandConfig(
    name="harden",
    help_text="Test command rule.",
    choices=["ssh", "sudoers"],
    options=[
        OptionConfig(name="--force", is_flag=True, help_text="Force execution")
    ]
)

def mock_behavior(module, force):
    if force:
        print(f"Forcing hardening on {module}")
    else:
        print(f"Standard hardening on {module}")

console.add_command(config=test_config, behavior=mock_behavior)


def main():
    #terminal simulation
    runner = CliRunner()
    
    # test 1
    print("[*] Test 1: launch with flag --force")
    result_1 = runner.invoke(console._cli, ['harden', 'ssh','--force'])
    
    print(f"exit_code : {result_1.exit_code} (0 = Success)")
    print(f"output  : {result_1.output.strip()}")
    print("-" * 40)

    # test 2
    print("[*] Test 2: launch without flag --force")
    result_2 = runner.invoke(console._cli, ['harden', 'sudoers'])
    
    print(f"exit_code : {result_2.exit_code} (0 = Success)")
    print(f"output  : {result_2.output.strip()}")
    print("-" * 40)

    #test 3
    print("[*] Test 3: ")
    result_3 = runner.invoke(console._cli, ['harden', 'bad_module'])
    
    print(f"exit_code : invalid error : {result_3.exit_code} (0 = Success)")
    print(f"output  : {result_3.output.strip()}")
    print("-" * 40)
    print('E N D.')