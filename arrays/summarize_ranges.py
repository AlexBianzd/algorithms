def summarize_ranges(arr):
    res = []
    i = 0
    n = len(arr)
    while i < n:
        num = arr[i]
        while i + 1 < n and arr[i + 1] - arr[i] == 1:
            i += 1
        res.append((num, arr[i]))
        i += 1
    return res
