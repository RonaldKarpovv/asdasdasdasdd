import math
def orientation(p, q, r):
    """
    Функция определения ориентации трех точек.
    """
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2
def convex_hull(points):
    """
    Функция для нахождения выпуклой оболочки множества точек.
    """
    n = len(points)
    if n < 3:
        return []
    # Находим точку с минимальной координатой Y
    ymin = points[0][1]
    min_idx = 0
    for i in range(1, n):
        y = points[i][1]
        if y < ymin or (ymin == y and points[i][0] < points[min_idx][0]):
            ymin = y
            min_idx = i
    # Меняем первую точку с точкой с минимальной координатой Y
    points[0], points[min_idx] = points[min_idx], points[0]
    # Сортируем остальные точки по полярному углу относительно первой точки
    p0 = points[0]
    points = sorted(points, key=lambda x: (math.atan2(x[1] - p0[1], x[0] - p0[0]), x[0], x[1]))
    # Создаем стек и добавляем первые две точки
    stack = [points[0], points[1]]
    # Добавляем остальные точки в стек и удаляем неверные
    for i in range(2, n):
        while len(stack) > 1 and orientation(stack[-2], stack[-1], points[i]) != 2:
            stack.pop()
        stack.append(points[i])
    return stack

n = int(input("Введите количество точек: "))
points = []
for i in range(n):
    x, y = map(int, input("Введите координаты точки {}: ".format(i+1)).split())
    points.append((x, y))

hull = convex_hull(points)
if hull:
    print("Выпуклая оболочка:")
    for point in hull:
        print(point)
else:
    print("Выпуклая оболочка не найдена.")
