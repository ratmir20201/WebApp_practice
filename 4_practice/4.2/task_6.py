result = 0

with open('input.txt', 'r') as file:
    data = file.readlines()
    for i in data:
        result += int(i.strip())



with open('result.txt', 'w') as file:
    file.write(str(result))