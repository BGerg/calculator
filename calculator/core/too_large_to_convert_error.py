class TooLargeToConvertError(Exception):
    """
    Exception for handling large numbers that cannot be converted.
    """
    def __init__(self, message: str):
        super().__init__(message)

