with open('matrix.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f]
n = len(matrix)  # количество вершин в графе
visited = [False] * n  # массив для отслеживания посещенных вершин
components = []  # список для хранения компонент связности
# Функция поиска в ширину
def bfs(start):
    queue = [start]  # инициализация очереди
    visited[start] = True  # помечаем начальную вершину как посещенную
    
    while queue:
        vertex = queue.pop(0)  # извлекаем вершину из очереди
        components[-1].append(vertex)  # добавляем вершину в текущую компоненту связности
        
        # обходим соседей вершины
        for neighbor in range(n):
            if matrix[vertex][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True  # помечаем соседа как посещенного
                queue.append(neighbor)  # добавляем соседа в очередь
# Поиск компонента связности
for i in range(n):
    if not visited[i]:
        components.append([])  # создаем новую компоненту связности
        bfs(i)  # запускаем поиск в ширину из непосещенной вершины
# Запись результата в файл
with open('result.txt', 'w') as f:
    f.write(f'Количество компонент связности: {len(components)}\n')
    for i, component in enumerate(components):
        f.write(f'Компонента связности {i + 1}: {component}\n')
