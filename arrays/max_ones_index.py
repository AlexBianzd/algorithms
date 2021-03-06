def max_ones_index(arr):

    n = len(arr)
    max_count = 0
    max_index = 1
    prev_zero = -1
    prev_prev_zero = -1

    for curr in range(n):

        # If current element is 0,
        # then calculate the difference
        # between curr and prev_prev_zero
        if arr[curr] == 0:
            if curr - prev_prev_zero > max_count:
                max_count = curr - prev_prev_zero
                max_index = prev_zero

            prev_prev_zero = prev_zero
            prev_prev_zero = curr

    if n - prev_prev_zero > max_count:
        max_index = prev_zero

    return max_index