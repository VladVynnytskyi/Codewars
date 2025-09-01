def number(bus_stops):
    res = []
    for el in bus_stops:
        res.append(el[0] - el[1])
    return sum(res)