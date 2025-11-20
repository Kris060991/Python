def string_to_float(s):
    s = s.strip()
    if not s:
        return None  # Пустая строка

    is_positive = True # Флаг для хранения знака числа. По умолчанию считаем число положительным.
    digits = [] # Пустой список для хранения всех цифр числа
    digits_after_point = 0 # Счётчик цифр, которые находятся после десятичной точки.
    point_found = False # Флаг, показывающий, нашли ли мы уже точку в числе
    i = 0 # начинаем с первого символа строки
    n = len(s) # сохраняем длину строки для использования в цикле

    # Обработка знака
    if i < n and s[i] in ('+', '-'):
        if s[i] == '-':
            is_positive = False
        i += 1

    # Проверка на строки только из знака
    if i >= n:
        return None

    # Обработка целой и дробной части
    has_digits = False # флаг-индикатор, который показывает, были ли найдены хотя бы одна цифра в строке
    while i < n:
        char = s[i] # char - текущий обрабатываемый символ

        if char == '.':
            if point_found:
                return None  # если точка уже была найдена ранее - возвращаем ошибку
            point_found = True
        elif char.isdigit():
            digits.append(int(char))
            has_digits = True
            if point_found:
                digits_after_point += 1 # Если точка уже найдена, увеличиваем счётчик цифр после точки
        else:
            return None  # Если символ не точка и не цифра - ошибка

        i += 1 # Переходим к следующему символу

    # Проверка корректности
    if not has_digits:
        return None

    # Восстановление числа
    result = 0.0 # здесь будем накапливать итоговое число
    # Вычисляем начальную степень для первой цифры
    # Общее количество цифр минус цифры после точки дает цифры до точки
    digits_before_point = len(digits) - digits_after_point
    power = digits_before_point - 1  # Начинаем с самой старшей степени

    # Умножаем каждую цифру на 10 в нужной степени
    for digit in digits:
        result += digit * (10 ** power)
        power -= 1  # Уменьшаем степень для следующей цифры

    # Умножаем на -1 если отрицательное число
    if not is_positive:
        result = -result

    return result

def main():
    s = input()

    num = string_to_float(s)

    if num is None:
        print("Ошибка: некорректный ввод")
    else:
        doubled = num * 2
        print(f"{doubled:.3f}")

main()