import json


def get_data():
    data = json.load(open("data.json"))
    return data