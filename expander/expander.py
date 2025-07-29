from expander.parser import parse_input
from expander.validator import is_valid_number
from expander.config import STEP_DELIMITER


def expand_string(input_str: str) -> list[int]:

    tokens = parse_input(input_str)
    expanded = []

    for token in tokens:
        
        step = 1
        
        # Check for step delimiter
        if STEP_DELIMITER in token:
            range_part, step_part = token.split(STEP_DELIMITER, 1)
            if not is_valid_number(step_part):
                raise ValueError(f"Invalid step value: '{step_part}'")
            step = int(step_part)
        else:
            range_part = token

        
        if "-" in range_part:
            
            parts = range_part.split("-")
            if len(parts) != 2:
                raise ValueError(f"Invalid range format: '{token}'")

            start_str, end_str = parts

            if not (is_valid_number(start_str) and is_valid_number(end_str)):
                raise ValueError(f"Range contains non-numeric values: '{token}'")

            start = int(start_str)
            end = int(end_str)
            
            if start > end and step > 0:
                step = -step

            if step > 0:
                expanded.extend(range(start, end + 1, step))
            else:
                expanded.extend(range(start, end - 1, step))

        else:
            if not is_valid_number(token):
                raise ValueError(f"Non-numeric value found: '{token}'")
            expanded.append(int(token))

    return expanded
