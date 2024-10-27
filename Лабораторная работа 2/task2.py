salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
count = 0
money_capital = 0
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
while count != months:
    count += 1
    if count != 1:
        spend *= (1 + increase)
    money_capital += spend - salary
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(money_capital))
