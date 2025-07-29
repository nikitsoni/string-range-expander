# String Range Expander

A Python CLI utility to parse and expand string inputs representing numbers and ranges.

## ✅ Features Implemented

- Basic range expansion: `"1-3"` → `[1, 2, 3]`
- Ignores whitespace and empty parts: `" , 1-3 , ,5 "` → `[1, 2, 3, 5]`
- Custom range delimiters: `"1..3"`, `"4~6"`, `"10 to 12"` → all supported
- Handles reversed and invalid ranges: `"5-3"` → `[5, 4, 3]`
- Supports step values: `"1-10:2"` → `[1, 3, 5, 7, 9]`
- Deduplicates overlapping values
- Supports multiple output formats: list, csv, set

## 🧪 Testing

Tests are written using `pytest` and are available in the `tests/` directory.

To run the tests:

```bash
pytest -v
```

## 🚀 CLI Usage

```bash
python main.py "1-3,2-4" [--format list|csv|set]
```

### Examples

```bash
# Default output (list)
python main.py "1-3,5"

# Output as CSV
python main.py "1-3,5" --format csv

```

## 📁 Project Structure

```
string_range_expander/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── expander/
│   ├── __init__.py
│   ├── parser.py
│   ├── validator.py
│   ├── expander.py
│   └── config.py
├── tests/
│   ├── test_script.py
```

## ✅ Requirements

- Python 3.7+
- `pytest`

Install dependencies:

```bash
pip install -r requirements.txt
```

## 👤 Author

Nikit Soni