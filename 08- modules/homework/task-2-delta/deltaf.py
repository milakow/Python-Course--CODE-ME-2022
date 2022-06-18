import math


def count_del(a, b, c):
    return b ** 2 - 4 * a * c


def count_0_pos (delta, a, b):
    if delta > 0:
        x1 = (- b - math.sqrt(delta)) / 2 * a
        x2 = (- b + math.sqrt(delta)) / 2 * a
        return 'Istnieją dwa miejsca zerowe:', x1, x2
    elif delta == 0:
        x0 = -b / 2 * a
        return 'Istnieje jedno miejsce zerowe:', x0
    else:
        return 'Brak miejsc zerowych.'


