def search(squence, number, lower, upper):
    if (lower == upper):
        return upper
    else:
        middle = lower + (upper - lower)//2
        if number > middle:
            search(squence, number, middle + 1, upper)
        else:
            search(squence, number, lower, middle)