def final_deposit_amount(*interest, amount=1000):
    t = amount
    for i in interest:
        t = t * (1 + i / 100)
    return round(t, 2)


