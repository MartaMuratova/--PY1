money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить
total_money = money_capital + salary
while total_money > 0:
    month += 1
    total_money -= spend
    spend += (spend * increase)




# TODO Оформить решение

print(month)
