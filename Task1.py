day = int(input('введите число от 1 до 7: '))
if (day < 6):
    print('Это будний день')
elif (day > 7):
    print('введите число от 1 до 7')
else :
    print('Это выходной день')