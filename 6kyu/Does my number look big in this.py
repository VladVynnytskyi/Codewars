def narcissistic( value ):
    array_value = list(str(value))
    string_result = 0
    for num in array_value:
        string_result += int(num)** len(array_value)
    if string_result == value:
        return True
    else:
        return False
    


    # if string_result == value:
    #     return True
    # else:
    #     return False
    
    # OR

    # return string_result == value