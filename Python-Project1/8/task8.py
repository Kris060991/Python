def main():
    n = int(input()) # читаем количество чисел
    unique_numbers = set() # создаем пустое множество

    for _ in range(n):
        number = int(input()) # читаем очередное число
        unique_numbers.add(number) # добавляем число в множество (если такое число уже есть, оно не добавится повторно)

    print(len(unique_numbers)) # выводим количество уникальных чисел

main()