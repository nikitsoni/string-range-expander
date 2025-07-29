from expander.parser import parse_input
from expander.validator import is_valid_number


def expand_string(input_str: str) -> list[int]:

    tokens = parse_input(input_str)
    expanded = []

    for token in tokens:

        if "-" in token:
            parts = token.split("-")

            if len(parts) != 2:
                raise ValueError(f"Invalid range format: '{token}'")

            start_str, end_str = parts

            if not (is_valid_number(start_str) and is_valid_number(end_str)):
                raise ValueError(f"Range contains non-numeric values: '{token}'")

            start = int(start_str)
            end = int(end_str)

            step = 1 if start <= end else -1
            expanded.extend(range(start, end + step, step))

        else:
            if not is_valid_number(token):
                raise ValueError(f"Non-numeric value found: '{token}'")
            expanded.append(int(token))

    return expanded
