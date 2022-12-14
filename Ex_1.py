# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:    
#   6 -> да
#   7 -> да
#   1 -> нет

day_of_the_week = int(input('Enter the number of the day of the week: '))
if 0 < day_of_the_week < 8:
    if day_of_the_week == 6 or day_of_the_week == 7:
        print("It's a holiday")
    else: print("It's a workong day")
else: print("There is not such day in the week, joker")