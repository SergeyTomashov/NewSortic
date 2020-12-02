def sa(b):
    if b[0] == '' or b[1] == '':
        pass
    b[0], b[1] = b[1], b[0]
    return b
