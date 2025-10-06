import json
import argparse
from read_csv import read_csv
from convertToCoverageJSON import (
    convert_to_pointseries_covjson,
)  # adjust name if different

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert weather CSV to CoverageJSON")
    parser.add_argument("--csv", required=True, help="CSV file name (in project root)")
    args = parser.parse_args()

    # Step 1: Read CSV
    rows = read_csv(args.csv)

    # Step 2: Convert to CoverageJSON
    covjson = convert_to_pointseries_covjson(rows)

    # Step 3: Pretty-print JSON to terminal
    print(json.dumps(covjson, indent=2))

    # (Optional) Step 4: Save to file
    with open("coverage.json", "w", encoding="utf-8") as f:
        json.dump(covjson, f, indent=2)
    print("\n✅ CoverageJSON saved to coverage.json")
