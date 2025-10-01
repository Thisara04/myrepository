from pathlib import Path
import csv
import logging
from typing import Iterable, Sequence

def load_signal_csv(path: Path) -> list[float]:
    
    filename = "C:\Users\amtha\myrepository\signal.csv"
    data: list[float] = []

    with open(filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
      data.append(float(row[0]))

    """
    TODO:
      - Validate that path exists and is a file; else raise FileNotFoundError
      - Read rows; parse as float; collect into list
      - Use try/except to catch ValueError and log it (then re-raise)
    """
    # TODO: implement
    return []

def save_features_csv(path: Path, rows: Iterable[Sequence[float]]) -> None:
    """
    Save a CSV with header: rms,zero_crossings,peak_to_peak,mad
    TODO:
      - Ensure parent dir exists (mkdir parents=True, exist_ok=True)
      - Write header and rows via csv.writer
    """
    # TODO: implement
    pass
