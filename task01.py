 # 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

list_str = ['212584', '78500', '6987']
print (list_str)
find_str = input('Enter the number: ')
my_list = [i for i in range (len(list_str))]
a = lambda i: True if (find_str in list_str[i]) else False
res = list(map (a, my_list ))
for i in res:
    if i == True:
        print(f'Число {find_str} присуствует в строке')
        break  