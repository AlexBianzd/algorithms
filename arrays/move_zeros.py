def move_zeros(arr):
    res = []
    zeros = 0
    for i in arr:
        if i is 0:
            zeros += 1
        else:
            res.append(i)

    res.extend([0] * zeros)
    return res