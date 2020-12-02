def sb(b):
    if b == list():
        pass
    elif b[0] == b[-1]:
        pass
    else:
        b[0], b[1] = b[1], b[0]
    return b
