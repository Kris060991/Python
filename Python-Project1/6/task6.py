import json

def merge_sorted_lists(list1, list2):
    # Объединяет два отсортированных списка фильмов в один отсортированный используя алгоритм слияния за O(n)
    result = []
    i = j = 0  # указатели для list1 и list2

    # Проходим по обоим спискам одновременно
    while i < len(list1) and j < len(list2):
        # Сравниваем годы фильмов
        if list1[i]['year'] <= list2[j]['year']:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    # Добавляем оставшиеся элементы из list1 (если есть)
    while i < len(list1):
        result.append(list1[i])
        i += 1

    # Добавляем оставшиеся элементы из list2 (если есть)
    while j < len(list2):
        result.append(list2[j])
        j += 1

    return result

try:
    # Читаем входные данные из файла
    with open('input.txt', 'r', encoding='utf-8') as file:
        data = file.read()

    # Парсим JSON
    input_data = json.loads(data)

    # Проверяем структуру данных
    if not isinstance(input_data, dict) or 'list1' not in input_data or 'list2' not in input_data:
        print("Неверный формат ввода")
        exit(1)

    list1 = input_data['list1']
    list2 = input_data['list2']

    # Проверяем что это списки
    if not isinstance(list1, list) or not isinstance(list2, list):
        print("Неверный формат ввода")
        exit(1)

    # Проверяем структуру каждого фильма
    for movie in list1 + list2:
        if not isinstance(movie, dict) or 'title' not in movie or 'year' not in movie:
            print("Неверный формат ввода")
            exit(1)
        if not isinstance(movie['year'], int):
            print("Неверный формат ввода")
            exit(1)

    # Объединяем списки с помощью алгоритма слияния за O(n)
    merged_list = merge_sorted_lists(list1, list2)

    # Формируем результат
    result = {
        "list0": merged_list
    }

    # Выводим в формате JSON
    print(json.dumps(result, indent=2, ensure_ascii=False))

except FileNotFoundError:
    print("Файл input.txt не найден")
except json.JSONDecodeError:
    print("Неверный формат JSON")
except Exception:
    print("Неверный формат ввода")