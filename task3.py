my_list = [1, 2, 3, 4]
text = "emp"

text_list = list(text)
num= 0

while num < len(my_list):
    my_list[num] = text + str(my_list[num])
    num+= 1

print(my_list)
