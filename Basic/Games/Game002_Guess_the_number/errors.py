def error(error_id):
    """Returns an error based on ErrorID"""
    errors = {
        1: "Mismatched input",
    }
    return errors[error_id]
