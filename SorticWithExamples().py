global a
global b
a = [14, 15, 16, 17, 18, 19, 40, 50]
b = [10, 40, 15, 11, 20, 80, 90, 14]


def sa():
    if a == list():
        pass
    elif a[0] == a[-1]:
        pass
    else:
        a[0], a[1] = a[1], a[0]


sa()
print(a)
print(b)


def sb():
    if b == list():
        pass
    elif b[0] == b[-1]:
        pass
    else:
        b[0], b[1] = b[1], b[0]


sb()
print(a)
print(b)


def function():
    pass


def ss():
    sa()
    sb()


ss()
print(a)
print(b)


def pa():
    global a, b
    if b == list():
        pass
    else:
        a = [b[0]] + a
    b = b[1:]


pa()
print(a)
print(b)


def pb():
    global a, b
    if a == list():
        pass
    else:
        b = [a[0]] + b
    a = a[1:]


pb()
print(a)
print(b)


def ra():
    global a
    kol = 0
    for i in a:
        kol += 1
    res = a[-1]
    for i in range(kol):
        a[i - 1] = a[i]
    a[-2] = res


ra()
print(a)


def rb():
    global b
    kol = 0
    for i in b:
        kol += 1
    res = b[-1]
    for i in range(kol):
        b[i - 1] = b[i]
    b[-2] = res


rb()
print(b)


def rr():
    ra()
    rb()


rr()


def rra():
    global a
    kol = 0
    for i in a:
        kol += 1
    res = a[0]
    for i in range(kol):
        a[-i] = a[-i - 1]
    a[1] = res


rra()
print(a)


def rrb():
    global b
    kol = 0
    for i in b:
        kol += 1
    res = b[0]
    for i in range(kol):
        b[-i] = b[-i - 1]
    b[1] = res


rrb()
print(b)


def rrr():
    rra()
    rrb()


rrr()
print(a)
print(b)
