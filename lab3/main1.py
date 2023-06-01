import queue

with open('graph.txt') as f:
    lines = f.readlines()
    # преобразуем строки в числа
    matrix = [[int(x) for x in line.split()] for line in lines]

# def bfs(graph, start):
#     visited = set()  
#     q = queue.Queue() 
#     q.put(start)  
#     visited.add(start)  
#     while not q.empty():
#         current = q.get()  
#         for neighbor in graph[current]:  
#             if neighbor not in visited:  
#                 q.put(neighbor)  
#                 visited.add(neighbor)  
#     return visited  
def count_components(graph):
    components = []  # список всех компонент связности
    visited = set()  
    q = queue.Queue() 
    q.put(vertex)  
    visited.add(vertex)  
    while not q.empty():
        current = q.get()  
        for neighbor in graph[current]:  
            if neighbor not in visited:  
                q.put(neighbor)  
                visited.add(neighbor)  
    return visited    # множество посещенных вершин
    for vertex in graph:  # проходим все вершины графа
        if vertex not in visited:  # если вершина еще не посещена
            component = bfs(graph, vertex)  # запускаем BFS из этой вершины
            components.append(component)  # добавляем компоненту связности в список
            visited.update(component)  # помечаем все вершины компоненты как посещенные
    return len(components), components  # возвращаем количество компонент связности и список всех компонент
num_components, components = count_components(matrix)
print("Количество компонент связности:", num_components)
print("Список компонент связности:", components)
