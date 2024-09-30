my_list = [10, 20, 30, 40]

for i in range(len(my_list)):
    if my_list[i] == 20:
        my_list[i] = 200;
        break

print(my_list)