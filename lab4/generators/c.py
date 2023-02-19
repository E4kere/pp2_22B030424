n = int(input())
def define(nurichmo):
    for i in range(1, 1 + nurichmo):
        if i % 3 == 0 and i % 4 == 0:
            print(i, end = " ")
define(n)