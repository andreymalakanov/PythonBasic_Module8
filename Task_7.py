# Andrey Malakanov
# Skillbox PythonBasic
print('Задача 7. Стипендия')

#Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
# 
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.

educational_grant = int(input('Введите сумму стипендии: '))
expenses = int(input('Введите сумму расходов в первый месяц: '))
current_mounth = 1
for mounth in range(0, 10):
  if educational_grant >= expenses:
    print(f'В этом({current_mounth}) месяце стипендия покрывает все рассходы')
  else:
    parants_money = (int((expenses - educational_grant) * 100)) / 100
    print(f'В этом месяце ({current_mounth}) потребуется {parants_money} рублей сверх стипендии')
  current_mounth += 1
  expenses *= 1.03
