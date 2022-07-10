#Utwórz dekorator @timepassed mierzący czas działania dowolnej funkcji.
import time
import matplotlib.pyplot as plt

def count_time(function):
    def counter():
        start = time.time()
        function()
        finish = time.time()
        return finish - start
    return counter

@count_time
def build_graph():
    x_axis = ['poland', 'germany', 'spain', 'croatia']
    y_axis = [322575, 357588, 505990, 56594]
    plt.xticks(size=7, rotation=0.3)
    plt.plot(x_axis, y_axis, color='b', marker = 'o')
    plt.title('The area of country')
    plt.xlabel('Country')
    plt.ylabel('Area [km^2]')
    plt.savefig(f'Area.pdf')
    return plt.show()

def main():
    effect = build_graph()
    print(effect)


if __name__ == '__main__':
    main()
