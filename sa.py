def sa(a):
    if a == list():
        pass
    elif a[0] == a[-1]:
        pass
    else:
        a[0], a[1] = a[1], a[0]
    return a
