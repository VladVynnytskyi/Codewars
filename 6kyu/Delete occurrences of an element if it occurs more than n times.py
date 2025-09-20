def delete_nth(order,max_e):
    result = []
    for e in order:
        if result.count(e) < max_e:
            result.append(e)
    return result


def delete_nth(order, max_e):
    result = []
    counts = {}
    for e in order:
        if counts.get(e, 0) < max_e:
            result.append(e)
            counts[e] = counts.get(e, 0) + 1
    return result
