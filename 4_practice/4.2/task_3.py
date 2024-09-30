def ComputePay(hours, rate):
    if hours > 40:
        rate *= 1.5
    return rate * hours

hours = int(input("Введите часы: "))
rate = float(input("Введите ставку: "))
pay = ComputePay(hours, rate)
print("Оплата: ", pay)