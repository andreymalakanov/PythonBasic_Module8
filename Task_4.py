# Andrey Malakanov
# Skillbox PythonBasic
print('Задача 4. Отрезок')

#Напишите программу, 
# которая считывает с клавиатуры два числа a и b,
# считает и выводит на консоль среднее арифметическое
# всех чисел из отрезка [a; b], которые кратны числу c.
# Подсказка: (a и b  являются промежутком, а c для проверки кратности).

a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
summ = 0
counter = 0
if a > b:
  a, b = b, a
for number in range(a, b + 1):
  summ += number
  counter +=1
average = summ / counter
print ('Среднее арифметическое всех чисел из отрезка [a; b] =', average)

