from helperfunctions import *

def heatcapacity(compound, temperature, unit="mol"):
    data = dataread(compound)["heat_capacity"]

    if data["liquid"]["model"] == "shomate":
        if temperature < data["liquid"]["validity_range"][0] or temperature > data["liquid"]["validity_range"][1]:
            raise ValueError(f"Temperature {temperature} K is out of validity range for liquid phase of {compound}. Valid range is {data['heat_capacity']['liquid']['validity_range']} K.")    
        coeffs = data["liquid"]["coefficients"]
        a = coeffs["a"]
        b = coeffs["b"]
        c = coeffs["c"]
        d = coeffs["d"]
        e = coeffs["e"]
        f = coeffs["f"]
        g = coeffs["g"]
        h = coeffs["h"]

        T = temperature/1000
        Cp = a + b*T + c*T**2 + d*T**3 + e/T**2
        if unit == "mol":
            return f"{Cp:.4f} J/(mol*K)"
        elif unit == "kg":
            return f"{mol_to_mass(Cp, compound):.4f} J/(kg*K)"