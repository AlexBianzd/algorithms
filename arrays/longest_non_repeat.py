def longest_non_repeat(string):
    used_char = {}
    max_len = 0
    j = 0
    for i in range(string):
        if string[i] in dict:
            j = max(used_char[string[i], j])
        used_char[i] = i + 1
        max_len = max(max_len, i - j + 1)
    return max_len