hours = int(input("Введите часы: "))
rate = float(input("Введите ставку: "))
if hours > 40:
    rate *= 1.5
print("Оплата: ", hours * rate)