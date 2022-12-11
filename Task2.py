def expression_1(x, y, z):
    return not(x or y or z)

def expression_2(x, y, z):
    return not x and not y and not z

flag = True

for x in (True, False):
    for y in (True, False):
        for z in (True, False):
           if not (expression_1(x, y, z) == expression_2(x, y, z)):
               flag = False
               print('x =', x, 'y =', y, 'z =', z)
               print('expression_1 =', expression_1(x, y, z))
               print('expression_2 =', expression_2(x, y, z))
               break
if flag:
    print('Все верно')
else:
    print('Не верно')
