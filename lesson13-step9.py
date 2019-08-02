def closest_mod_5(x):
    # y = int(x / div) * div + div
    y = x+5-x%5
    if y % 5 == 0:
        return y
    return "I don't know :("
i = int(input ())
print (f"решение = {closest_mod_5(i)}")
