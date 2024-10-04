def ComputePay(hours, rate):
    if hours > 40:
        pay = (40 * rate) + (hours - 40) * rate * 1.5
    else:
        pay = hours * rate
    return pay


hours = int(input("Введите часы: "))
rate = float(input("Введите ставку: "))
pay = ComputePay(hours, rate)
print("Оплата: ", pay)
