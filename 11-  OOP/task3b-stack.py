#Napisz klasę Stack (stos); - get element - wyciągnij element ze stosul; - show - wyświetl cały stos; - push - dodaj element do stosu
class Queue:
    def __init__(self, lifo=[]):
        self.lifo = lifo

    def show(self):
        print(self.lifo)

    def is_empty(self):
        return len(self.lifo) == 0

    def put(self, element):
        return self.lifo.insert(0, element)

    def get(self):
        return self.lifo.pop(-1)

def main():
    myqueue = Queue(['dog', 'cat', 'hamster'])
    myqueue.show()
    print(myqueue.is_empty())
    print(myqueue.put('item'))
    myqueue.show()
    item = myqueue.get()
    print('Usunięto: ', item)
    myqueue.show()

if __name__ == '__main__':
    main()
