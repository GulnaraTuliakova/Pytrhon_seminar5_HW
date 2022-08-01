# 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем
# первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

n = int(input('Введите число n чисел, которые необходио добавить в список: '))
num = list(range(1, n*3, 3))
print(f'Первоначальный список: {num}')
mult = 0
new_list = []
if n % 2 == 0:
    mult = [num[i] * num[len(num)-1-i] for i in range(len(num)//2)]
    new_list.append(mult)
    print(f'Произведение пар чисел: {new_list}')
else:
    mult = [num[i] * num[len(num)-1-i] for i in range(len(num)//2+1)]
    new_list.append(mult)
    print(f'Произведение пар чисел: {new_list}') 