import math

x1 = int(input('Введите координату x1: '))
y1 = int(input('Введите координату y1: '))
x2 = int(input('Введите координату x2: '))
y2 = int(input('Введите координату y2: '))

one = (x1, y1)
two = (x2, y2)

def distance(one, two):
    return math.sqrt((one[0]-two[0])**2 + ((one[1]-two[1])**2))

print(distance(one, two))
