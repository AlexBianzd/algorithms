def limit(arr, min_lim = None, max_lim = None):
    result = []
    if min_lim == None and max_lim == None:
        result = arr
    elif min_lim == None:
        for i in arr:
            if i <= max_lim:
                result.append(i)
    elif max_lim == None:
        for i in arr:
            if i <= min_lim:
                result.append(i)
    else:
        for i in arr:
            if i >= min_lim and i <= max_lim:
                result.append(i)

    return result