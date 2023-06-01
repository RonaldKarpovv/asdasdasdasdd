import queue
def bfs(graph, start):
    # создаем очередь для обхода вершин в ширину
    q = queue.Queue()
    # добавляем начальную вершину в очередь
    q.put(start)
    # создаем словарь для хранения расстояний от начальной вершины до остальных вершин графа
    distances = {start: 0}
    # выполняем обход в ширину
    while not q.empty():
        # извлекаем вершину из очереди
        current = q.get()
        # проходим по всем соседним вершинам
        for neighbor in range(len(graph[current])):
            # если между текущей и соседней вершинами есть ребро
            if graph[current][neighbor] != 0:
                # если соседняя вершина еще не была посещена
                if neighbor not in distances:
                    # добавляем ее в очередь и вычисляем расстояние
                    q.put(neighbor)
                    distances[neighbor] = distances[current] + 1
    return distances

with open('graph.txt') as f:
    lines = f.readlines()
    # преобразуем строки в числа
    matrix = [[int(x) for x in line.split()] for line in lines]
distances = bfs(matrix, 0)
# выводим расстояния до всех вершин графа
for vertex, distance in distances.items():
    print('Расстояние до вершины {}: {}'.format(vertex, distance))
