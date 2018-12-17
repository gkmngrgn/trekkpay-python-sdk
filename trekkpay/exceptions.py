CODE_AUTH_FAILED = 0
CODE_VALIDATION_FAILED = 400
CODE_INTERNAL_SERVER_ERROR = 500


class ParameterError(Exception):
    pass


class ValidationError(Exception):
    pass
