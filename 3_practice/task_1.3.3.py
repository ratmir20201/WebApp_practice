grade = float(input("Введите оценку: "))

if grade < 0 or grade > 1:
    print("Ошибка")
else:
    if grade >= 0.9:
        print("A")
    elif grade >= 0.8:
        print("B")
    elif grade >= 0.7:
        print("C")
    elif grade >= 0.6:
        print("D")
    else:
        print("F")