import os
import csv
from typing import List, Dict, Tuple

REQUIRED_HEADERS = ["id", "feedback", "sentiment"]

def verify_csv_headers(file_path: str, required_headers: List[str] = REQUIRED_HEADERS) -> bool:
    """Check if the CSV file contains the required headers."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        return headers is not None and all(h in headers for h in required_headers)

def read_csv(file_path: str) -> List[Dict[str, str]]:
    """Read a CSV file and return a list of dictionaries."""
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        return [row for row in reader]

def save_uploaded_file(uploaded_file, save_dir: str) -> str:
    """Save an uploaded file to the specified directory."""
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, uploaded_file.filename)
    with open(file_path, "wb") as f:
        f.write(uploaded_file.file.read())
    return file_path

def parse_and_validate_csv(file_path: str) -> Tuple[bool, List[Dict[str, str]]]:
    """Verify headers and parse CSV, returning (is_valid, data)."""
    if not verify_csv_headers(file_path):
        return False, []
    data = read_csv(file_path)
    return True, data