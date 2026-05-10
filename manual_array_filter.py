def array_filter(array, key, condition): 
    i = 0 

    while i < len(array): 
        if array[i][key] == condition: 
            array.pop[i]
        else: 
             i += 1

    return array
