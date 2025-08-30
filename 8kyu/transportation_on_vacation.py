def rental_car_cost(d):
    if d < 3:
        res = 40 * d
        return res
    elif 3 <= d < 7:
        res = (40 * d) - 20
        return res
    elif 7 <= d:
        res = (40 * d) - 50
        return res