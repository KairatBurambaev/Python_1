day = int(input('введите число от 1 до 7: '))

if day not in range(1,8):
    exit()

if day > 5:
    print('Это выходной день')
else:
    print('Это будний день')