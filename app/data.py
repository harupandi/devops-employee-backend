import os
import json

_DEFAULT_DIR = os.path.dirname(os.path.abspath(__file__))
_DATA_DIR = os.environ.get("EMPLOYEES_DATA_DIR", _DEFAULT_DIR)
_DATA_FILE = os.path.join(_DATA_DIR, "employees.json")

with open(_DATA_FILE, "r", encoding="utf-8") as f:
    EMPLOYEES = json.load(f)