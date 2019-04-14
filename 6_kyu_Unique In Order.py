def unique_in_order(iterable):
    list = [' ']
    for n in iterable:
        if list[-1] != n:
            list.append(n)
    list.pop(0)
    return list

    pass