# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат
# точек в этой четверти (x и y).

def findPoints(number):
    if number == 1: return 'X < 0 and Y > 0'
    elif number == 2: return 'X > 0 and Y > 0'
    elif number == 3: return 'X < 0 and Y < 0'
    elif number == 4: return 'X > 0 and Y < 0'
    else: return 'Error!'

userNumber = int(input('Enter the number of quarter (1 or 2 or 3 or 4): '))

print(findPoints(userNumber))
