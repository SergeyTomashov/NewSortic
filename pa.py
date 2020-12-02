def pa():
    global a, b
    if b == list():
        pass
    else:
        a = [b[0]] + a
    b = b[1:]
