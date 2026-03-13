import json
import os

def dataread(compound):
    source = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "compounds", compound + ".json"))
    with open(source) as file:
        data = json.load(file)