def fortune(f0, p, c0, n, i):
    # your code
    f = f0
    percent = 0.01 * p
    c = c0
    inflation = 0.01 * i
    for year in range(n):
        f = f + (f * percent) - c
        c = c + (c * inflation)

    if f >= 0:
        return True
    else: 
        return False