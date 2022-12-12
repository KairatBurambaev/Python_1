
def function_1(x, y, z):
    return not(x or y or z)

def function_2(x, y, Z):
    return (not x and not y and not z)

for x in (True, False):
    for y in (True, False):
        for z in (True, False):
           print(function_1(x, y, z) == function_2(x, y, z))
           print(x, y, z)