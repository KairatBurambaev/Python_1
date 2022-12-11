day = int(input('введите число от 1 до 7: '))

if day < 0 or day > 7:
    print('неправильнный ввод')
    exit()

if (day <= 5):
    print('Это будний день')
else:
    print('Это выходной день')
