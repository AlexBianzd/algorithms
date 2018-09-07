def josephus(int_list, skip):
    skip = skip - 1 # list starts with 0 index
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (skip + idx) % len_list # hash index to every 3rd
        yield int_list.pop(idx)
        len_list -= 1
