def heatcapacity(compound, temperature):
    from helperfunctions import dataread
    data = dataread(compound)

    if data["heat_capacity"]["liquid"]["model"] == "shomate":
        if temperature < data["heat_capacity"]["liquid"]["validity_range"][0] or temperature > data["heat_capacity"]["liquid"]["validity_range"][1]:
            raise ValueError(f"Temperature {temperature} K is out of validity range for liquid phase of {compound}. Valid range is {data['heat_capacity']['liquid']['validity_range']} K.")    
        coeffs = data["heat_capacity"]["liquid"]["coefficients"]
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
        return Cp # J/(mol*K)