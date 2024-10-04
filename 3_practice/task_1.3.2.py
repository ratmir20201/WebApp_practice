try:
    hours = int(input("Введите часы: "))
    rate = float(input("Введите ставку: "))
    if hours > 40:
        pay = (40 * rate) + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    print("Оплата: ", hours * rate)
except BaseException:
    print("Error, please enter numeric input")