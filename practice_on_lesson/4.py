def main():
    string = input("Введите строку: ")
    result = ""
    count = 1
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            count += 1
        else:
            result += f"{string[i]}{count}"
            count = 1

    print(result)


if __name__ == "__main__":
    main()
