opposite = {
        'NORTH': "SOUTH",
        'SOUTH': "NORTH",
        'WEST': "EAST",
        'EAST': "WEST",
    }
    

def dir_reduc(arr):
    new_plan = []
    for plan in arr:
        if new_plan and new_plan[-1] == opposite[plan]:
            new_plan.pop()
        else:
            new_plan.append(plan)
    return new_plan