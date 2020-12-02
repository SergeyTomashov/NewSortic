def rb():
    global b
    kol = 0
    for i in b:
        kol += 1
    res = b[-1]
    for i in range(kol):
        b[i - 1] = b[i]
    b[-2] = res
