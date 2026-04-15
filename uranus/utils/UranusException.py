"""
2026 april 15
*************
HIBISCUS PUBLIC LICENSE
***********************
This project was created by a human fueled by questionable decisions,
excessive curiosity, and possibly poor life choices.

The author explicitly disclaims all responsibility, sanity, coherence,
and any illusion that this software is useful, functional, or even 
remotely a good idea.

If it works: do not question it.
If it breaks: that was always the plan.
If it does something unexpected: congratulations, you've discovered a 
feature.

No guarantees. No support. No regrets.
Proceed at your own risk… or don’t. Nobody is watching. Probably.
***************************************************************

this file contains some utils for management 
"""

from utils.utils import Color

class UranusException(Exception):
    """Uranus Exception core"""
    
    def __init__(self,exception):
        self.exception= str(exception)
        super().__init__(self.exception)

    def __str__ (self):
        return self.exception

class ExecutionTraceException(UranusException):
    def __init__(self,exception_msg:str):
        if not exception_msg:
            super().__init__(str(exception_msg))
        else: super().__init__(Color.in_red("assigning type not belong to class <Result>"))
        