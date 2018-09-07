def three_sum(arr):
    res = set()
    arr.sort()
    for i in range(len(arr) - 2):
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        l, r = i + 1, len(arr) - 1
        while l < r:
            s = arr[i] + arr[l] + arr[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.add((arr[i], arr[l], arr[r]))
                while l < r and arr[l] == arr[l + 1]:
                    l += 1
                while l < r and arr[r] == arr[r - 1]:
                    r -= 1
                l += 1
                r -= 1
    return res
