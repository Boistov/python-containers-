my_list = [1, 3, 5, 7, 9, 10],[2, 4, 6, 8]
num = len(my_list) - 1
a = my_list[num]
my_list = my_list[:-1]

i = 0
for _ in range(len(a)):
    my_list.append(a[i])
    i += 1

print(my_list)