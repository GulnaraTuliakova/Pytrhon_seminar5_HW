# 3. Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран.
    
n = int(input('Введите число n: '))
new_num  = list(map(lambda x:(x+1/x)**x, [i for i in range(1, n+1)]))
print(new_num)