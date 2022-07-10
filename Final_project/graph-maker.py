import numpy as np
import matplotlib.pyplot as plt
import calculations

def get_data(filename):
    try:
        with open(filename, encoding='utf-8-sig') as fopen:
            content = fopen.read()
            return content
    except FileNotFoundError as e:
        print(f'File {filename} was not found. ')

def show_bar(x_axis, y_axis, filename):
    plt.bar(x_axis, y_axis, label=f'Hardness for {filename}', width=0.7, color='b')
    plt.title('The hardness of the weld in relation to the distance from its center')
    plt.legend()
    plt.xlabel('The distance from the center of the weld [µm]')
    plt.ylabel('Hardness [HV]')
    return plt.show()

def show_scatter(x_axis, y_axis, filename):
    plt.scatter(x_axis, y_axis, label=f'Hardness for {filename}', color='purple', s=30, alpha=0.8)
    plt.title('The hardness of the weld in relation to the distance from its center')
    plt.legend()
    plt.xlabel('The distance from the center of the weld [µm]')
    plt.ylabel('Hardness [HV]')
    return plt.show()

def show_line(x_axis, y_axis, filename):
    plt.plot(x_axis, y_axis, ls='-', label=f'Hardness for {filename}', linewidth='1.5', c='g', marker='.', ms=6)
    plt.title('The hardness of the weld in relation to the distance from its center')
    plt.legend()
    plt.xlabel('The distance from the center of the weld [µm]')
    plt.ylabel('Hardness [HV]')
    return plt.show()

def save(graph):
    with open('result.pdf', 'w') as res:
        pass
def main():
    filename = input('Enter the name of the file with data to prepare a plot: ')
    user_data = get_data(filename).replace('\n', ';').split(';')
    data_for_array = np.array(user_data, dtype=int)
    new_data_fa = data_for_array.reshape(-1, 3)
    # print(new_data_fa)
    final_data = np.stack((new_data_fa[0:]), axis=1)
    # print(final_data)
    hardness = final_data[1] #measured_hardness
    position = final_data[2] #position_of_mearument
    ar_position = position.copy()
    ar_position = ar_position.astype(str)

    average = calculations.count_average(hardness, len(hardness))
    deviation = calculations.count_deviation(hardness, average, len(hardness))
    print(f'For these datas the average hardness is {average} HV whereas the standard deviation is {deviation}.')

    graph_type = input('Pick the type of graph you want to receive: bar(b), scatter(s) or line(l): ')
    if len(graph_type) != 1:
        print('You entered too long name. I do not understand. Please repeat. ')
    elif graph_type == 'b':
        user_graph = show_bar(ar_position, hardness, filename)
        print(user_graph)
        plt.savefig(f'BarPlot_{filename}.png')
    elif graph_type == 's':
        user_graph = show_scatter(position, hardness, filename)
        print(user_graph)
        save(user_graph)
    else:
        user_graph = show_line(position, hardness, filename)
        print(user_graph)
        save(user_graph)


if __name__ == '__main__':
    main()


