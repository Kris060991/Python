def read_matrix(filename):
    # Чтение матрицы из файла
    with open(filename, 'r') as f:
        lines = f.readlines()
    matrix = []
    for line in lines:
        row = [int(x) for x in line.strip().split()]
        matrix.append(row)
    return matrix


def dfs(matrix, visited, i, j, component_info):
    # Рекурсивный обход связанных единиц
    if (i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or
            visited[i][j] or matrix[i][j] == 0):
        return

    visited[i][j] = True
    component_info['count'] += 1

    # Обновляем границы компоненты
    component_info['min_row'] = min(component_info['min_row'], i)
    component_info['max_row'] = max(component_info['max_row'], i)
    component_info['min_col'] = min(component_info['min_col'], j)
    component_info['max_col'] = max(component_info['max_col'], j)

    # Рекурсивно обходим соседние клетки (4-связность)
    dfs(matrix, visited, i + 1, j, component_info)
    dfs(matrix, visited, i - 1, j, component_info)
    dfs(matrix, visited, i, j + 1, component_info)
    dfs(matrix, visited, i, j - 1, component_info)


def count_figures(matrix):
    # Подсчет квадратов и кругов в матрице
    if not matrix:
        return 0, 0

    n = len(matrix)
    m = len(matrix[0])

    visited = [[False for _ in range(m)] for _ in range(n)]
    squares = 0
    circles = 0

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1 and not visited[i][j]:
                # Инициализируем информацию о компоненте
                component_info = {
                    'count': 0,
                    'min_row': i,
                    'max_row': i,
                    'min_col': j,
                    'max_col': j
                }

                # Находим все связанные единицы
                dfs(matrix, visited, i, j, component_info)

                # Пропускаем компоненты из одной единицы
                if component_info['count'] <= 1:
                    continue

                # Вычисляем размеры ограничивающего прямоугольника
                width = component_info['max_col'] - component_info['min_col'] + 1
                height = component_info['max_row'] - component_info['min_row'] + 1
                expected_area = width * height

                # Проверяем, является ли фигура квадратом
                if component_info['count'] == expected_area:
                    squares += 1
                else:
                    circles += 1

    return squares, circles


def main():
    # Читаем матрицу из файла
    matrix = read_matrix('input.txt')

    # Подсчитываем фигуры
    squares, circles = count_figures(matrix)

    # Выводим результат
    print(f"{squares} {circles}")

main()