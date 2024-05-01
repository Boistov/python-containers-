my_list = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

max_sum = 0
max_sublist = []

for sublist in my_list:
    sublist_sum = sum(sublist)
    if sublist_sum > max_sum:
        max_sum = sublist_sum
        max_sublist = sublist

print(max_sublist)
