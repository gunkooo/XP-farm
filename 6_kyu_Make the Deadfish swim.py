def parse(data):
    # TODO: your code here
    i = 0
    list = []
    for n in data:
        if n == "i" :
            i += 1
        elif n == "d" :
            i -= 1
        elif n == "s" :
            i *= i
        elif n == "o":
            list.append(i)
    return list


