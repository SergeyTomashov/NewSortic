def rrb():
    global b
    kol = 0
    for i in b:
        kol += 1
    res = b[0]
    for i in range(kol):
        b[-i] = b[-i - 1]
    b[1] = res
