def rotate(arr, k):
    arr = arr[:]
    n = len(arr)
    k = k % len(arr)

    def reverse(arr, a, b):
        while a < b:
            arr[a], arr[b] = arr[b], arr[a]
            a += 1
            b -= 1

    reverse(arr, 0, n - k - 1)
    reverse(arr, n - k, n - 1)
    reverse(arr, 0, n - 1)
    return arr
