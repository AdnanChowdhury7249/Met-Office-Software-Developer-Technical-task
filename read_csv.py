import argparse
import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Weather_Data:
    time: str
    lon: float
    lat: float
    temperature: str


def read_csv(filename: str):
    path = Path(__file__).parent / filename

    if not path.exists():
        raise FileNotFoundError(f" File not found: {path}")

    weather_data = []
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            weather_data.append(
                Weather_Data(
                    time=row["time"],
                    lon=float(row["longitude"]),
                    lat=float(row["latitude"]),
                    temperature=str(row["temperature"]),
                )
            )
    return weather_data


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Read weather CSV data from project root"
    )
    parser.add_argument(
        "--csv",
        required=True,
        help="Name of the CSV file in the project root (e.g. weather_data.csv)",
    )
    args = parser.parse_args()

    data = read_csv(args.csv)
    for d in data:
        print(d)
