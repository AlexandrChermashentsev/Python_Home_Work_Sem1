# 2. Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

x = int(input('Enter the integer number X: '))
y = int(input('Enter the integer number Y: '))
z = int(input('Enter the integer number Z: '))
if -(x and y and z) == -x or -y or -z:
    print('True')
else: print('Falce')
