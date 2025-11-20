def main():

    # Чтение координат первого вектора
    x1, y1, z1 = map(float, input().split())

    # Чтение координат второго вектора
    x2, y2, z2 = map(float, input().split())

    # Вычисление скалярного произведения
    dot_product = x1 * x2 + y1 * y2 + z1 * z2

    # Вывод результата
    print(dot_product)

main()