import json


def load_data():
    """Load data as a dictionary"""
    with open('city.json') as f:
        data = json.load(f)
    return data

