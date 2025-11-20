def main ():

    try:
        n = int(input().strip())

        # Проверка, что число натуральное
        if n <= 0:
            print("Ошибка: Ожидалось положительное число")
        else:
            triangle = []

            for i in range(n):
                row = [1] * (i + 1)  # создаем строку из единиц

                # Заполняем внутренние элементы
                for j in range(1, i):
                    row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

                triangle.append(row)

            # Вывод треугольника
            for row in triangle:
                print(' '.join(map(str, row))) # Форматируем вывод: преобразуем числа в строки и соединяем пробелами

    except ValueError:
        print("Ошибка: Ожидалось натуральное число")

main()