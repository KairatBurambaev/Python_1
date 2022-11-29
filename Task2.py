for x in (True, False):
    for y in (True, False):
        for z in (True, False):
           print(not(x or y or z) == (not x and not y and not z))
           print(x, y, z)