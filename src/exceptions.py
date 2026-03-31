class ShortenerBaseException(Exception):
    pass


class NoLongUrlFoundException(ShortenerBaseException):
    pass
