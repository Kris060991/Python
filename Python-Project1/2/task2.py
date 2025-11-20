def main():

    num = int(input())

    if num < 0:
        print(False)
    else:
        original = num
        reversed_num = 0

        while num > 0:
            reversed_num = reversed_num * 10 + num % 10
            num = num // 10

        print(original == reversed_num)

main()