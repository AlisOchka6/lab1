def input_text():
    eps = -1

    while True:
        try:
            x = float(input("Введите X: "))
            break
        except ValueError:
            print("Введите корректное значение!")
    while eps >= 1 or eps <= 0:
        try:
            eps = float(input("Введите Eps от 0 до 1: "))
        except ValueError:
            print("Введите корректное значение!")

    return x, eps


def cal(x, eps):
    s = 0
    n=0
    overflowMin = 1.7e-308
    overflowMax =1.7e+308
    overflow = 0
    q = x


    while True:
        if ((abs(q) < overflowMin or abs(q) > overflowMax) and q != 0) or \
                ((abs(s) < overflowMin or abs(s) > overflowMax) and s != 0):
            overflow = 1
            break
        if n % 2 == 0:
            s += q
        else:
            s -= q
        q *= (x*x)/((2 * n + 2) * (2 * n +3))
        n += 1
        if abs(q) < eps:
            break
    return s, overflow


def output_text(s, overflow):
    if overflow:
        print("Ряд расходится, невозможно посчитать сумму!")
    else:
        print("Сумма =", s)
    return


while True:
    x, eps = input_text()
    s, overflow = cal(x, eps)
    output_text(s, overflow)

    work = input("Нажмите любую клавишу для продолжения работы! Если хотите завершить, введите \"стоп\": ")
    if work == "стоп":
        break