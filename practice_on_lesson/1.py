grade = float(input("Введите оценку: "))

if grade < 0 or grade > 100:
    print("Ошибка")
else:
    if grade >= 90:
        print("A")
    elif grade >= 80:
        print("B")
    elif grade >= 70:
        print("C")
    elif grade >= 60:
        print("D")
    else:
        print("F")