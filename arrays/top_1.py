def top_1(arr):
    values = {}
    result = []
    f_val = 0

    for i in arr:
        if i in values:
            values[i] += 1
        else:
            values[i] = 1

    f_val = max(values.values())
        
    for i in values.keys():
        if values[i] == f_val:
            result.append(i)
        else:
            continue
    
    return result