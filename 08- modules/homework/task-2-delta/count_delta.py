import deltaf

def main():
    a = int(input('Podaj wartość a: '))
    b = int(input('Podaj wartość b: '))
    c = int(input('Podaj wartość c: '))
    delta = deltaf.count_del(a, b, c)
    print(f'Dla podanych parametrów a={a}, b={b}, c={c} delta wynosi {delta}.', deltaf.count_0_pos(delta, a, b))

if __name__ == '__main__':
    main()

