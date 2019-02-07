def fuel_range (value, consumption_per_100km):
    """
    >>> fuel_range (50, 10) #doctest:+ELLIPSIS
    480...
    """
    fuel_consumption_1km = consumption_per_100km / 100
    fuel_range_km = (value / fuel_consumption_1km) - 20
    return fuel_range_km

if __name__ == "__main__":
    import doctest
    doctest.testmod()
