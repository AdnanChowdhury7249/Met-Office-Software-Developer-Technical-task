import json
import argparse
from read_csv import read_csv
from covjson_builder import (
    convert_to_pointseries_covjson,
)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert weather CSV to CoverageJSON")
    parser.add_argument("--csv", required=True, help="CSV file name (in project root)")
    args = parser.parse_args()

    rows = read_csv(args.csv)

    covjson = convert_to_pointseries_covjson(rows)

    print(json.dumps(covjson, indent=2))

    with open("coverage.json", "w", encoding="utf-8") as f:
        json.dump(covjson, f, indent=2)
