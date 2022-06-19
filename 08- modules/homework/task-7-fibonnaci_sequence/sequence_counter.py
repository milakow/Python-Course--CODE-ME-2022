#Stwórz moduł, który dla dowolnej wartości n, zwróci ciąg fibonnaciego.
import fibonacci

def main():
    num = int(input('Pick a number: '))
    print(*fibonacci.count_sequence(num))

if __name__ == '__main__':
    main()