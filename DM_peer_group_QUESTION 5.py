set_x = { }
set_y = { }
def sets(set_x, set_y):
    print(set_x)
    print(set_y)
    for value1 in set_x:
        for value2 in set_y:

            if value1 % value2 == 0:
                return True
    return False
print(sets({1, 2, 3, 4, 5} , {10, 1, 2, 11 }))
print(sets({1, 2, 3, 4, 5} , {10, 8, 6, 11 }))





