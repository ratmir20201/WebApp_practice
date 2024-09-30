with open('input.txt', 'a') as file:
    file.write("\n14")


with open('input.txt', 'r') as file:
    data = file.read()
    print(data)