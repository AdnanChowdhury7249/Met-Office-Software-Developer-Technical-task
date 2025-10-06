from typing import List, Dict
from read_csv import Weather_Data


def convert_to_pointseries_covjson(rows: List[Weather_Data]):
    if not rows:
        raise ValueError("NO data provided")

    temps = [r.temperature for r in rows]
    times = [r.time for r in rows]
    lon = rows[0].lon
    lat = rows[0].lat

    return {
        "type": "Coverage",
        "domain": {
            "type": "Domain",
            "domainType": "PointSeries",
            "axes": {
                "x": {"values": [lon]},
                "y": {"values": [lat]},
                "t": {"values": times},
            },
            "referencing": [
                {
                    "coordinates": ["x", "y"],
                    "system": {
                        "type": "GeographicCRS",
                        "id": "http://www.opengis.net/def/crs/EPSG/0/4326",
                    },
                },
                {
                    "coordinates": ["t"],
                    "system": {"type": "TemporalRS", "calendar": "Gregorian"},
                },
            ],
        },
        "parameters": {
            "temperature": {
                "type": "Parameter",
                "observedProperty": {
                    "id": "http://vocab.nerc.ac.uk/standard_name/air_temperature/",
                    "label": {"en": "Air temperature"},
                },
                "unit": {
                    "label": {"en": "kelvin"},
                    "symbol": {
                        "value": "K",
                        "type": "http://www.opengis.net/def/uom/UCUM/",
                    },
                },
            }
        },
        "ranges": {
            "temperature": {
                "type": "NdArray",
                "dataType": "float",
                "axisNames": ["t"],
                "shape": [len(temps)],
                "values": temps,
            }
        },
    }
