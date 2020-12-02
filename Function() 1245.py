global a, b
def sa(a):
    if a == list():
        pass
    elif a[0] == a[-1]:
        pass
    else:
        a[0], a[1] = a[1], a[0]

def sb(b):
    if b == list():
        pass
    elif b[0] == b[-1]:
        pass
    else:
        b[0], b[1] = b[1], b[0]

def ss():
    sa(a)
    sb(b)

ss()
print(a)
print(b)
print('')
