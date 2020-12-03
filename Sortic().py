global a
global b


def sa():
    if a == list():
        pass
    elif a[0] == a[-1]:
        pass
    else:
        a[0], a[1] = a[1], a[0]
#Функция sa(), которая меняет первые два элемента
#стека a и проверяет, что в стеке
#не один элемент и что он не пустой,
#а содержится два целых числовых значения в списке

def sb():
    if b == list():
        pass
    elif b[0] == b[-1]:
        pass
    else:
        b[0], b[1] = b[1], b[0]
#Функция sb(), которая меняет первые два элемента
#стека b и проверяет, что в стеке
#не один элемент и что он не пустой,
#а содержит два целых числовых значения


def ss():
    sa()
    sb()
#Функция ss(), которая обращается к
#функциям sa() и sb() одновременно и выводит результат


def pa():
    global a, b
    if b == list():
        pass
    else:
        a = [b[0]] + a
    b = b[1:]
#Фукция pa(), которая перемещает первый элемент из списка b
#в список a и удаляет перемещенный элемент из списка b


def pb():
    global a, b
    if a == list():
        pass
    else:
        b = [a[0]] + b
    a = a[1:]
#Функция pb(), котора перемещает первый элемент из списка a
#в список b и удаляет перемещенный элемент из списка a


def ra():
    global a
    kol = 0
    for i in a:
        kol += 1
    res = a[-1]
    for i in range(kol):
        a[i - 1] = a[i]
    a[-2] = res


def rb():
    global b
    kol = 0
    for i in b:
        kol += 1
    res = b[-1]
    for i in range(kol):
        b[i - 1] = b[i]
    b[-2] = res


def rr():
    ra()
    rb()


def rra():
    global a
    kol = 0
    for i in a:
        kol += 1
    res = a[0]
    for i in range(kol):
        a[-i] = a[-i - 1]
    a[1] = res


def rrb():
    global b
    kol = 0
    for i in b:
        kol += 1
    res = b[0]
    for i in range(kol):
        b[-i] = b[-i - 1]
    b[1] = res


def rrr():
    rra()
    rrb()
