def is_valid_number(value: str) -> bool:
    try:
        int(value)
        return True
    except ValueError:
        return False
