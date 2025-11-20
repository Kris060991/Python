def main():
    # Читаем первую строку с размерами поля
    n, m = map(int, input().split())

    # Читаем само поле
    coins = []
    for _ in range(n):
        row = list(map(int, input().split()))
        coins.append(row)

    # Создаем матрицу для динамического программирования
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = coins[0][0]

    # Заполняем первую строку
    for j in range(1, m):
        dp[0][j] = dp[0][j - 1] + coins[0][j]

    # Заполняем первый столбец
    for i in range(1, n):
        dp[i][0] = dp[i - 1][0] + coins[i][0]

    # Заполняем остальную часть матрицы
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = coins[i][j] + max(dp[i - 1][j], dp[i][j - 1])

    print(dp[n - 1][m - 1])

main()