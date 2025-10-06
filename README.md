# Met-Office-Software-Developer-Technical-task

Overview

This project simulates a backend service which reads a CSV file containing weather data and converts it to a CoverageJSON point series representation.
The dataset represents a time series for a single geographic point, following the PointSeries domain type.

Requirements

- Python 3.11+
- Dependencies listed in requirements.txt


Install dependencies:
pip install -r requirements.txt


How to Run the Application

- Ensure weather data is located in project root.
- How to run the Script: python main.py --csv weather_data.csv



How to Run the Tests

- Run pytest -v
- expected output: tests/test_covjson_builder.py::test_convert_to_pointseries_covjson_creates_valid_structure PASSED    



Design Choices and Assumptions

- Language Python 3.12 
- Dependencies Standard Python libraries and Pytest are used. 

- Weather data dataclass provides strong typing
- Data is read once and transformed into coverageJSON following the Pointseries spec.

Assumptions:
- The input file should be located in the root folder. 
- CSV should contain valid longitude, latitude and  values.
- Dataset represents a Pointseries  
- The unit symbol uses ("type": "http://www.opengis.net/def/uom/UCUM/") outlined in the spec. 

Separation of concerns:
- read_csv.py handles file I/O.
- covjson_builder.py handles the transformation logic to build the coverageJSON
- main.py is used as the CLI interface.
- Test checks the json structure.

The application is intentionally structured to be easily extendable and maintainable. I ensured each file follows single responsibility. Application can be easily
extended to include Grid CoverageJSON. 
