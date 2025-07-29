from expander.expander import expand_string

def main():
    try:
        input_str = input("Enter string with numbers and ranges: ")
        result = expand_string(input_str)
        print(result)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
