def rra():
    global a
    kol = 0
    for i in a:
        kol += 1
    res = a[0]
    for i in range(kol):
        a[-i] = a[-i - 1]
    a[1] = res
