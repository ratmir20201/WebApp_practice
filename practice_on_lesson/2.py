def main():
    age = int(input("Введите возраст: "))
    if age >= 20:
        print("Вы взрослый.")
    elif 19 >= age >= 13:
        print("Вы подросток.")
    else:
        print("Вы ребенок.")


if __name__ == "__main__":
    main()
