# TODO: Check this file trying to handle errors

class SemanticError(Exception):
    """Base class for all semantic errors."""
    def __init__(self, message, line=None):
        if line is not None:
            message = f"Line {line}: {message}"
        super().__init__(message)


class TypeMismatchError(SemanticError):
    def __init__(self, expected_type, actual_type, var_name, line=None):
        message = (
            f"Type mismatch: cannot assign '{actual_type}' to variable '{var_name}' of type '{expected_type}'"
        )
        super().__init__(message, line)


class UndeclaredVariableError(SemanticError):
    def __init__(self, var_name, line=None):
        message = f"Undeclared variable: '{var_name}'"
        super().__init__(message, line)


class RedefinedVariableError(SemanticError):
    def __init__(self, var_name, line=None):
        message = f"Redefinition error: variable '{var_name}' is already defined"
        super().__init__(message, line)


class UnsupportedOperationError(SemanticError):
    def __init__(self, operator, operand_type, line=None):
        message = f"Unsupported operation: '{operator}' not supported for type '{operand_type}'"
        super().__init__(message, line)


class InvalidFunctionCallError(SemanticError):
    def __init__(self, func_name, reason, line=None):
        message = f"Invalid function call: {func_name} - {reason}"
        super().__init__(message, line)
