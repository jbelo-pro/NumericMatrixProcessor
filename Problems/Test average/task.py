def average_mark(*args):
    s = 0
    for n in args:
        s += n
    return round(s / len(args), 1)
