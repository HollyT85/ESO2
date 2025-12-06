# ESO2

Python project

## Setup

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Project Structure

```
ESO2/
├── src/           # Source code
├── tests/         # Test files
├── venv/          # Virtual environment (not committed)
├── requirements.txt
└── README.md
```

## Usage

```bash
python src/main.py
```

## Testing

```bash
python -m pytest tests/
```
