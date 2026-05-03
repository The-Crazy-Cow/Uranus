
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

