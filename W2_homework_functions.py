def fuel_range (value, consumption_per_100km):
    """
    >>> fuel_range (50, 10)
    480.0
    """
    fuel_consumption_1km = consumption_per_100km / 100
    fuel_range_km = (value / fuel_consumption_1km) - 20
    return fuel_range_km
print(round(fuel_range (50, 10)))
