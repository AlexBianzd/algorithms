def missing_ranges(arr, lo, hi):
    res = []
    start = lo

    for n in arr:
        if n == start:
            start += 1
        elif n > start:
            res.append((start, n - 1))
            start = n + 1

    if start <= hi:
        res.append((start, hi))

    return res
    

print(missing_ranges([3, 5], 0, 8))