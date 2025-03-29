money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов
while money_capital >= 0 and money_capital - spend >= 0:
    money_capital += salary
    money_capital -= spend
    count += 1
    if count != 1:
        spend *= (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:", count)
