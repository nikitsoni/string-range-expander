def parse_input(input_str: str) -> list[str]:
    # Splits the input string by comma, trims whitespace, and filters out empty strings and returns list of tokens.
    raw_tokens = input_str.split(",")
    cleaned_tokens = [token.strip() for token in raw_tokens if token.strip()]
    return cleaned_tokens