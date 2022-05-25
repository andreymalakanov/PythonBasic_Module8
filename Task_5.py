# Andrey Malakanov
# Skillbox PythonBasic
print('Задача 5. Функция 2')

#В прошлый раз мы написали Саше программу,
# которая считает функцию в каждой точке отрезка и выводит значение на экран.
# Но теперь ему нужно,
# чтобы значения считались в обратном порядке.
# Плюс к этому в программе ему нужно сделать так,
# чтобы можно было настраивать шаг, с которым он скачет по точкам отрезка.
# 
# Напишите программу,
# которая получает на вход начало и конец отрезка, а также шаг.
# Затем высчитывает функцию игрек в каждой точке отрезка
# и с нужным шагом, начиная с конца, и выводит ответ на экран.

# Сама функция выглядит так:
# y = x**3 + 2x**2 - 4x + 1

# Пример:
# 
# Введите начало отрезка: -2
# Введите конец отрезка: 2
# Введите шаг: -1
# В точке 2 функция равна 9
# В точке 1 функция равна 0
# В точке 0 функция равна 1
# В точке -1 функция равна 6
# В точке -2 функция равна 9

segment_start = int(input('Введите начало отрезка: ')) 
segment_end = int(input('Введите конец отрезка: '))
segment_step = int(input('Введите шаг: '))
print('Значение функции y = x^3 + 2x^2 - 4x + 1')
print(segment_start, segment_end)
if segment_step < 0:
  if segment_start < segment_end:
    segment_start, segment_end = segment_end, segment_start
  for x in range(segment_start, segment_end - 1, segment_step):
    y = x**3 + 2*x**2 - 4*x + 1
    print (f'В точке {x} функция равна {y}')
else:
  if segment_start > segment_end:
    segment_start, segment_end = segment_end, segment_start
  for x in range(segment_start, segment_end + 1, segment_step):
    y = x**3 + 2*x**2 - 4*x + 1
    print (f'В точке {x} функция равна {y}')