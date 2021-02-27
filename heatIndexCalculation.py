def calculate_heat_index(T, RH): # T = temperature, RH = relative humidity
    HI = 1.1 * T - 10.3 + 0.046 * RH
    if HI < 80:
        return HI
    else:
        HI = -42.379 + 2.04901523 * T + 10.14333127 * RH - 0.22475541 * T * RH - 0.00683783 * T * T - 0.05481717 * RH * RH + 0.00122874 * T * T * RH + 0.00085282 * T * RH * RH - 0.00000199 * T * T * RH * RH
        if (80 <= HI <= 87) and (RH>85):
            HI = HI + 0.02 * (RH - 85)*(87-T)
            return HI
        else:
            return HI

# def to_celsius(T):
#     temp_celsius = (T-32)/1.8
#     return temp_celsius

def to_fah(T):
    temp_f = T* 1.8 + 32
    return temp_f

def evaluate_risk(T):
    if T <= 27:
        return "Normal"
    elif 27.1 <= T <= 32:
        return "Cautela"
    elif 32.1 <= T <= 41:
        return "Cautela extrema"
    elif 41.1 <= T <= 54:
        return "Perigo"
    elif T > 54:
        return "Perigo extremo"
    else:
        return "NA"


print(calculate_heat_index(to_fah(25.7),73.4))
# # print(calculate_heat_index(82,40))
# print(calculate_heat_index(90,100))
# print("normal", evaluate_risk(to_celsius(calculate_heat_index(80,40))))
# print("cautela", evaluate_risk(to_celsius(calculate_heat_index(88,45))))
# print("cautela extrema", evaluate_risk(to_celsius(calculate_heat_index(92,60))))
# print("perigo", evaluate_risk(to_celsius(calculate_heat_index(94,80))))
# print("perigo extremo", evaluate_risk(to_celsius(calculate_heat_index(94,85))))