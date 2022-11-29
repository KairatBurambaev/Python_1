part = int(input('Введите номер четверти: '))
q = list(range(11))
c = list(range(-10,1))
if (part == 1):
    {print('x:',q,'y:',q)}
elif (part == 2):
    {print('x:',c,'y:',q)}
elif (part == 3):
    {print('x:',c,'y:',c)}
elif (part == 4):
    {print('x:',q,'y:',c)}
else:
    {print('Введите число от 1 до 4!')}