def read_graph(filename):
    # Чтение матрицы смежности ориентированного графа из файла
    matrix = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            matrix.append(list(map(int, line.strip().split())))
    return matrix


def dfs(graph, visited, start, component):
    # Обход в глубину
    visited[start] = True
    component.append(start)
    for i in range(len(graph)):
        if graph[start][i] == 1 and not visited[i]:
            dfs(graph, visited, i, component)

def find_scc(graph):#обход в глубину для составления порядка обхода
    #обход  еще раз,но в порядке убывания времени выхода из вершин,используем транспонированный граф
    # Поиск всех сильно связанных компонент
    n = len(graph)
    visited = [False] * n
    order = []
    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i, order)
    transposed_graph = [[graph[j][i] for j in range(n)] for i in range(n)]
    visited = [False] * n
    scc_list = []
    for i in reversed(order):
        if not visited[i]:
            scc = []
            dfs(transposed_graph, visited, i, scc)
            scc_list.append(scc)
    return scc_list

input_file = "input.txt"

# Чтение графа из входного файла
graph = read_graph(input_file)

 # Поиск сильно связанных компонент
scc = find_scc(graph)

with open('result.txt', 'w') as f:
    f.write(f"Количество сильно связных компонент: {len(scc)}\n")
    for i, component in enumerate(scc):
        f.write(f"Сильно связанные компоненты:{i+1}: {component}\n")
