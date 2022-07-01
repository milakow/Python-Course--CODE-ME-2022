#Stwórz własną implementację kolejki FIFO. Klasa kolejka (Queue) powinna na starcie przyjmować listę elementów. Wśród metod powinny się znaleźć takie jak: wyswietlenie kolejki, sprawdzenie czy jest pusta, dodanie elementu do kolejki (put), wyjęcie elementu z kolejki (get).Utwórz kilka obiektów klasy Queue z różnymi parametrami.
class Queue:
    def __init__(self, fifo=[]):
        self.fifo = fifo

    def show(self):
        print(self.fifo)

    def is_empty(self):
        return len(self.fifo) == 0

    def put(self, element):
        return self.fifo.append(element)

    def get(self):
        return self.fifo.pop(0)

def main():
    myqueue = Queue(['dog', 'cat', 'hamster'])
    myqueue.show()
    print(myqueue.is_empty())
    myqueue.put('fish')
    myqueue.show()
    item = myqueue.get()
    print('Usunięto: ', item)
    myqueue.show()

if __name__ == '__main__':
    main()
