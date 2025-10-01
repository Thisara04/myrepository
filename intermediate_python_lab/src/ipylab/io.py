from pathlib import Path
import csv
import logging
from typing import Iterable, Sequence

def load_signal_csv(path: Path) -> list[float]:
    
    data: list[float] = []
    with open(path, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                try:
                    data.append(float(row[0]))
                except ValueError as e:
                    logging.exception(f"Failed to convert value '{row[0]}' to float")
                    raise
    return data

def save_features_csv(path: Path, rows: Iterable[Sequence[float]]) -> None:
     with open(path, mode='w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["rms", "zero_crossings", "peak_to_peak", "mad"])  # header
        writer.writerows(rows)