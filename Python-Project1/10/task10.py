def main():
    try:
        n, total_time = map(int, input().split()) # Читаем первую строку, разбиваем на 2 числа: количество станков и требуемое время

        if n <= 0 or total_time <= 0:
            print("Неверный формат ввода")
            return

        from collections import defaultdict # специальный словарь со значениями по умолчанию
        devices_by_year = defaultdict(dict) # Создаем словарь, где для каждого года будет храниться словарь {время: минимальная_стоимость}

        # Читаем данные
        for _ in range(n):
            year, cost, time = map(int, input().split())
            if year <= 0 or cost <= 0 or time <= 0:
                print("Неверный формат ввода")
                return

            # Сохраняем минимальную стоимость для каждого времени
            if time not in devices_by_year[year] or cost < devices_by_year[year][time]:
                devices_by_year[year][time] = cost

        # Поиск оптимальной пары станков
        min_cost = float('inf')
        found = False

        # Перебираем все года и их словари времени-стоимости
        for year, time_costs in devices_by_year.items():
            times = list(time_costs.keys())

            # Для каждого времени time1 вычисляем какое время time2 нужно для пары
            for i in range(len(times)):
                time1 = times[i]
                cost1 = time_costs[time1]
                time2 = total_time - time1

                # Проверяем есть ли станок с нужным временем time2
                if time2 in time_costs:
                    cost2 = time_costs[time2]
                    # Если time1 == time2, нужно проверить что есть хотя бы 2 аппарата
                    if time1 == time2:
                        # Считаем сколько аппаратов с таким временем
                        count = sum(1 for t in times if t == time1)
                        if count >= 2:
                            total_cost = cost1 + cost2
                            if total_cost < min_cost:
                                min_cost = total_cost
                                found = True
                    else: # Если времена разные - просто складываем стоимости
                        total_cost = cost1 + cost2
                        if total_cost < min_cost:
                            min_cost = total_cost
                            found = True

        if found:
            print(min_cost)
        else:
            print("Неверный формат ввода")

    except (ValueError, IndexError):
        print("Неверный формат ввода")

main()