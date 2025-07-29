import argparse
from expander.expander import expand_string

def main():
    parser = argparse.ArgumentParser(description="Expand a string of numbers and ranges.")
    parser.add_argument(
        "input", type=str, 
        help="String with numbers and ranges (e.g. '1-3,5')"
    )
    parser.add_argument(
        "--format", choices=["list", "csv", "set"], default="list",
        help="Choose output format: list (default), csv, or set"
    )

    args = parser.parse_args()

    try:
        result = expand_string(
            input_str=args.input,
            output_format=args.format,
        )
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
