import json
import os

def dataread(compound):
    source = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "compounds", compound + ".json"))
    with open(source) as file:
        data = json.load(file)
    return data

def interpolate(x1, y1, x2, y2, x):
    """
    Linear interpolation between two points.
    
    Args:
        x1, y1: First data point
        x2, y2: Second data point
        x: The x value to interpolate at
    
    Returns:
        Interpolated y value
    """
    y = y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return y