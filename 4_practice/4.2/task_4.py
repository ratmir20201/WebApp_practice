def CalculateGrade(grade):
    if grade < 0 or grade > 1:
        return "Ошибка"
    else:
        if grade >= 0.9:
            return "A"
        elif grade >= 0.8:
            return "B"
        elif grade >= 0.7:
            return "C"
        elif grade >= 0.6:
            return "D"
        else:
            return "F"

grade = float(input("Введите оценку: "))
answer = CalculateGrade(grade)
print(answer)