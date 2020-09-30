def number_of_frogs(year):
    frogs = 120
    if year == 1:
        return 120
    else:
        frogs = 2*(number_of_frogs(year - 1) - 50)
        return frogs

