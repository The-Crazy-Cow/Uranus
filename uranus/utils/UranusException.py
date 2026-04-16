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

this file provide the management of excpetions
"""

from utils.UranusUtils import Color

class UranusException(Exception):
    """Uranus Exception core"""
    
    def __init__(self,exception):
        self.exception= str(exception)
        super().__init__(self.exception)

    def __str__ (self):
        return "\n\n\n"+Color.in_red(self.exception)

class ExecutionTraceException(UranusException):
    def __init__(self,
                exception_msg:str="assigning type not belong to class <Result>"):
        super().__init__(exception_msg)

class UserssecException(UranusException):
    def __init__(self,exception_msg:str):
        super().__init__(exception_msg)

