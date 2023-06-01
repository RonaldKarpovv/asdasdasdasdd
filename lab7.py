import heapq
def prim(graph, start):
    # Создаем множество посещенных вершин и очередь с приоритетом
    visited, heap = set(), [(0, start)]
    # Пока в очереди с приоритетом есть элементы
    while heap:
        # Извлекаем минимальный вес и вершину с очереди с приоритетом
        (weight, vertex) = heapq.heappop(heap)
        # Если вершина еще не посещена
        if vertex not in visited:
            # Добавляем ее в посещенные
            visited.add(vertex)
            # Добавляем в очередь с приоритетом все смежные вершины
            for neighbor, neighbor_weight in graph[vertex].items():
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_weight, neighbor))
    # Возвращаем множество посещенных вершин
    return visited
