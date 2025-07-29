from expander.parser import parse_input


def expand_string(input_str: str) -> list[int]:

    tokens = parse_input(input_str)
    expanded = []

    for token in tokens:

        if "-" in token:
            start_str, end_str = token.split("-")
            expanded.extend(range(int(start_str), int(end_str) + 1))
        else:
            expanded.extend([int(token)])

    return expanded
