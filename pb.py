def pb():
    global a, b
    if a == list():
        pass
    else:
        b = [a[0]] + b
    a = a[1:]
