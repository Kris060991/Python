def main():
    # Читаем первую строку
    first_line = input().replace(',', '.').split()
    n = int(first_line[0])
    x = float(first_line[1])

    # Читаем коэффициенты
    coefficients = []
    for _ in range(n + 1):
        coef = float(input().replace(',', '.'))
        coefficients.append(coef)

    # Вычисляем производную в точке x
    derivative_value = 0.0
    for power in range(n, 0, -1):
        # Коэффициент для степени power
        a = coefficients[n - power]
        # Производная a * x^power = a * power * x^(power-1)
        derivative_value += a * power * (x ** (power - 1))

    print(f"{derivative_value:.3f}")

main()