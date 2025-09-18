def pick_peaks(arr):
    result = {
        'pos': [],
        'peaks': []
    }

    plateau_start = None 

    for el in range(1, len(arr)-1):
        if arr[el-1] < arr[el] > arr[el+1]:
            result['pos'].append(el)
            result['peaks'].append(arr[el])

        elif arr[el-1] < arr[el] == arr[el+1]:
            plateau_start = el

        elif plateau_start is not None and arr[el] > arr[el+1]:
            result['pos'].append(plateau_start)
            result['peaks'].append(arr[plateau_start])
            plateau_start = None

        elif arr[el] < arr[el+1]:
            plateau_start = None

    return result
