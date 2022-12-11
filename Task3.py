x = int(input('Введите x отличное от 0: '))
y = int(input('Введите y отличное от 0: '))

if not (x != 0 and y != 0):
    print('Введите числа отличные от 0!')
    exit()

if (x > 0 and y > 0):
    print(1)
elif (x > 0 and y <0):
    print(4)
elif (x < 0 and y > 0):
    print(2)
else:
    print(3)
