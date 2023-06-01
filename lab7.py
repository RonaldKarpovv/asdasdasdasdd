import sys
def read_matrix(filename):
    with open(filename) as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        row = [int(x) for x in line.strip().split()]
        matrix.append(row)
    return matrix
def prim(matrix):
    n = len(matrix)
    visited = [False] * n
    key = [sys.maxsize] * n
    parent = [None] * n
    key[0] = 0
    for _ in range(n):
        u = min((i for i in range(n) if not visited[i]), key=lambda x: key[x])
        visited[u] = True
        for v in range(n):
            if matrix[u][v] and not visited[v] and matrix[u][v] < key[v]:
                key[v] = matrix[u][v]
                parent[v] = u
    return [(parent[i], i) for i in range(1, n)]
#filename = 'matrix.txt'
#matrix = read_matrix(filename)
matrix = [[0, 1, 1, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1], [0, 0, 0, 0, 0]]
edges = prim(matrix)
for u, v in edges:
    print(u, '-', v)
