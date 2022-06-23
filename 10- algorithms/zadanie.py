def foobar(n):
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            print('Foobar')
        elif num % 3 == 0:
            print('Foo')
        elif num % 5 == 0:
            print('bar')
        else:
            print(num)

def main():
    n = int(input('Pick a number: '))
    foobar(n)


if __name__ == '__main__':
    main()
