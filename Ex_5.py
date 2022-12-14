# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
#   A (3,6); B (2,1) -> 5,09
#   A (7,-5); B (1,-1) -> 7,21
# S = math.sqrt((x2-x1)^2 + (y2-y1)^2)

x1 = int(input('enter x for point A: '))
y1 = int(input('enter y for point A: '))
x2 = int(input('enter x for point B: '))
y2 = int(input('enter x for point B: '))

S = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print(f'distance between A and B = {S:.3f}')