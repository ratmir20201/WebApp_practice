def main():
    num = int(input("Введите число: "))
    result = 1
    for i in range(num):
        result *= i + 1
    print(result)


if __name__ == "__main__":
    main()
