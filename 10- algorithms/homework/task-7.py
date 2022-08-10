#7▹ Zaimplementuj w Pythonie algorytm Dijkstry.


def dijkstra_algorithm(nodes_list, root):
    n = len(nodes_list)
    dist = [float('infinity') for _ in range(n)]
    dist[root] = 0
    visited = [False for _ in range(n)]
    for node in range(n):
        u = -1
        for i in range(n):
            if not visited[i] and (u == -1 or dist[i] < dist[u]):
                u = i
        if dist[u] == float('infinity'):
            break
        visited[u] = True
        for v, l in nodes_list[u]:
            if dist[u] + l < dist[v]:
                dist[v] = dist[u] + l
    return dist

def main():
    nodes_space = {
        0: [(1, 1)],
        1: [(0, 3), (2, 5), (3, 1)],
        2: [(1, 7), (3, 4), (4, 2)],
        3: [(1, 3), (2, 6), (4, 2)],
        4: [(2, 3), (3, 5)]
    }
    node_num = int(input('Pick note number: '))
    result = dijkstra_algorithm(nodes_space, node_num)
    print(result)


if __name__ == '__main__':
    main()

# print(dijkstra_algorithm(nodes_space, 4))