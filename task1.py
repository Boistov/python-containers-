sample_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

i = [0, 4, 5]

num = []
for index, item in enumerate(sample_list):
    if index not in i:
        num.append(item)

print(num)
