def cakes(recipe, available):
    result = []
    for key in recipe:
        if key in available:
            result.append(available[key] // recipe[key])
        else:
            return 0
    return min(result)


def cakes(recipe, available):
    counts = []
    for ingredient, amount in recipe.items():
        if ingredient not in available:
            return 0
        counts.append(available[ingredient] // amount)
    return min(counts)
