# создаю список всех ребер и сортирую его по весу
edges = []
for i in range(len(matrix)):
    for j in range(i+1, len(matrix[i])):
        if matrix[i][j] > 0:
            edges.append((matrix[i][j], i, j))
edges.sort()
# создаю список подмножеств вершин
subsets = [{i} for i in range(len(matrix))]
# перебираю отсортированные ребра и добавляю их к минимальным подмножествам
minimum_spanning_tree = []
for edge in edges:
    weight, u, v = edge
    subset_u = None
    subset_v = None
    for subset in subsets:
        if u in subset:
            subset_u = subset
        if v in subset:
            subset_v = subset
    if subset_u != subset_v:
        minimum_spanning_tree.append(edge)
        subset_u.update(subset_v)
        subsets.remove(subset_v)
    # закончить, если все вершины находятся в одном и том же подмножестве
    if len(subsets) == 1:
        break
result_filename = "result.txt"
with open(result_filename, "w") as f:
    for edge in minimum_spanning_tree:
        f.write(f"{edge[1]} - {edge[2]}: {edge[0]}\n")
