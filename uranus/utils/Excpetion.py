#handle uranus Exception:Core

class UranusException(Exception):
    default_message = "An unhandled error occurred."

    def __init__(self, message=None):
        super().__init__(message)
        self.custom_message = message

    def __str__(self) -> str:
        return self.custom_message if self.custom_message else self.default_message


class ExecutionTraceException(UranusException):
    default_message = "Assigned type does not belong to the <Result> Enum class."

class UserssecException(UranusException):
    default_message = "Linux user space security rule or file validation failed."