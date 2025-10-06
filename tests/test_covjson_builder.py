from covjson_builder import convert_to_pointseries_covjson
from read_csv import Weather_Data
import pytest


def test_convert_to_pointseries_covjson_creates_valid_structure():
    dummy = [
        Weather_Data(time="2025-10-01T00:00Z", lon=-3.48, lat=50.73, temperature=275.2),
        Weather_Data(time="2025-10-01T01:00Z", lon=-3.48, lat=50.73, temperature=275.5),
        Weather_Data(time="2025-10-01T02:00Z", lon=-3.48, lat=50.73, temperature=275.7),
        Weather_Data(time="2025-10-01T02:00Z", lon=-3.48, lat=50.73, temperature=275.7),
        Weather_Data(time="2025-10-01T02:00Z", lon=-3.48, lat=50.73, temperature=275.7),
    ]
    cov = convert_to_pointseries_covjson(dummy)
    assert cov["type"] == "Coverage"
    assert cov["domain"]["domainType"] == "PointSeries"
    assert cov["domain"]["axes"]["x"]["values"] == [-3.48]
    assert cov["domain"]["axes"]["y"]["values"] == [50.73]
    assert cov["domain"]["axes"]["t"]["values"][0] == "2025-10-01T00:00Z"
    temp_param = cov["parameters"]["temperature"]
    assert temp_param["observedProperty"]["label"]["en"] == "Air temperature"
    assert temp_param["unit"]["symbol"]["value"] == "K"
    temp_range = cov["ranges"]["temperature"]
    assert temp_range["dataType"] == "float"
    assert temp_range["shape"] == [5]
    assert temp_range["values"] == [275.2, 275.5, 275.7, 275.7, 275.7]


def test_builder_empty_rows_raises():
    with pytest.raises(ValueError):
        convert_to_pointseries_covjson([])
