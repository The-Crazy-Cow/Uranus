"""
2026 April 15
*************
HIBISCUS PUBLIC LICENSE
***********************

This project was created by a human fueled by questionable decisions,
excessive curiosity, and possibly poor life choices.

The author explicitly disclaims all responsibility, sanity, coherence,
and any expectation that this software is useful, functional, or even
remotely a good idea.

If it works: do not question it.  
If it breaks: that was always the plan.  
If it does something unexpected: congratulations, you've discovered a feature.

No guarantees. No support. No regrets.  
Proceed at your own risk… or don’t. Nobody is watching. Probably.

***************************************************************

this file contains some utils for management 
"""

import shutil,os,gzip

from enum import Enum
from datetime import date


class Color :
    """use terminal color"""

    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"

    @staticmethod
    def in_red(string:str)->str:
        return f"{Color.RED}{string}{Color.RESET}"

    @staticmethod
    def in_green(string:str)->str:
        return f"{Color.GREEN}{string}{Color.RESET}"

class Result(Enum):
    SUCCESS=0 # [  OK ]
    FAILLURE=1 #[  x  ]
    WAITING=3 # [     ]

class ExecutionTrace():
    """Manage the programme execution trace for the user interface
    like dmesg on lin linux os booting"""

    def __init__(self,prog_name:str,description:str,state:str):
        self.prog=prog_name
        self.description=description
        self.state=state
        self._trace=Result.WAITING

    @property
    def trace(self):
        return self._trace

    @trace.setter
    def trace(self,result):
        if (isinstance(result,Result)):
            super().__setattr__("_trace",result)
        else:
            from utils.UranusException import ExecutionTraceException #hacky but i don't care
            raise ExecutionTraceException("u")
            
    def __str__ (self):
        tracer=""
        if (self.trace==Result.WAITING): tracer = "[     ]"
        elif (self.trace==Result.FAILLURE): tracer = f"[  {Color.in_red('X')}  ]"
        elif (self.trace==Result.SUCCESS): tracer = f"[  {Color.in_green('Ok')} ]"

        return f"{tracer} {20*' '}{self.prog} - {self.description}::{self.state}{random.randrange(0,4,1)*'.'}"

def add_date_suffixe(filename:str):
    """add the suffixe date : eg: req.txt-2005-8-6"""
    return filename+'-'+str(date.today())

def Mk_backup(file):
    """Make backup of an existing file and 
        compress it in default format specify via gzip"""

    #if  file already exists, erase it
    gz_file = str(file+'.back.gz')
    if os.path.exists(gz_file):
        if not os.path.isfile(gz_file):
            #existing a not file with the same name
            from utils.UranusException import UserssecException
            raise UserssecException(f"{gz_file} already exists and not a compressed file")
        os.remove(gz_file)

    #create the compress file
    with open(file,"rb") as f:
        with gzip.open(gz_file,"wb") as gzf:
            shutil.copyfileobj(f,gzf)

#TODO implement dynamism
"""import time

for i in range(21):
    bar = "█" * i + "-" * (20 - i)
    print(f"\r[{bar}] {i*5}%", end="")
    time.sleep(0.1)"""