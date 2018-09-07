def trimmean(arr, per):
    ratio = per / 200
    cul_sum = 0
    arr.sort()
    neg_val = int(len(arr)*ratio)
    arr = arr[neg_val:len(arr)-neg_val]
    for i in arr:
        cal_sum += i
    return cal_sum/len(arr)