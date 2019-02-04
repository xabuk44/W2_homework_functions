def fuel_consumption (value, consumption_per_100km):
    fuel_consumption_1km = consumption_per_100km / 100
    fuel_range = (value / fuel_consumption_1km) - 20
    return fuel_range
print(round(fuel_consumption(47.6, 10.5)))