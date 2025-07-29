from expander.config import ALTERNATE_RANGE_DELIMITERS, DEFAULT_RANGE_DELIMITER

def parse_input(input_str: str) -> list[str]:
    
    # Normalize alternate delimiters to default delimiters
    for delimiter in ALTERNATE_RANGE_DELIMITERS:
        input_str = input_str.replace(delimiter, DEFAULT_RANGE_DELIMITER)
        
    # Splits the input string by comma, trims whitespace, and filters out empty strings and returns list of tokens.
    raw_tokens = input_str.split(",")
    cleaned_tokens = [token.strip() for token in raw_tokens if token.strip()]
    return cleaned_tokens