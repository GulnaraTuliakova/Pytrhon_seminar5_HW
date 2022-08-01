# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

n = int(input('Введите число n чисел, которые необходио добавить в список: '))

num = list(range(1, n*3, 3))
print (num)
li = [i for i in range(len(num)) if i % 2 == 0]
new_list = list(map(lambda i:num[i], li))
sum = 0
for i in new_list:
    sum = sum + i
print(f'Числа на нечетных позициях = {new_list}') 
print (f'Сумма чисел на нечетных позициях = {sum}')  