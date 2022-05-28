# Andrey Malakanov
# Skillbox PythonBasic
print('Задача 9. Выражение')

#Дано число x.
#Напишите программу для вычисления следующего выражения 

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))


x = int(input('Введите число x: '))
a = 1
for number in range(1,65,2):
  # print(number) 
  #a *= ((x - number) / (x - 1 - number))
  b = x - number
  if b == 0:
    a = '0'
    break
  c = x - 1 - number
  if c == 0:
    a = 'Бесконечности'
    break
  # print(b, c)
  a *= (b / c)
  # print('====================')
print(f'При x = {x} выражение ((x-1)(x-3)(x-7)…(x-63) / ((x-2)(x-4)(x-8)…(x-64)) = {a}')
