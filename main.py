#!/usr/bin/python3


import lib
from time import time


#file = "src/data.txt" # 0 1 1 0
#file = "src/matrix.txt" # 1 0 1 0
#file = "src/matrix2.txt" # 1 0 -1 0 1
#file = "src/matrix3.txt" # 5 4 5 4
#file = "src/matrix4.txt" # 1 1 1
#file = "src/infinite_solutions.txt" # exception "Infinite number of solutions"
#file = "src/no_solutions.txt" # exception "No solutions"

#with open(file, "r") as f:
#    data = [list(map(int, s.split())) for s in f.readlines()]
#
#print(lib.gauss(data))

# inp = []
# 
# for _ in range(3):
    # inp.append(list(map(float, input("$ ").split())))
# 
# matrix = []
# 
# for row in inp:
    # matrix.append([row[0] ** 2, row[0], 1, row[-1]])
# 
# ans = lib.gauss(matrix)
# 
# print(f"y = {ans[0]}*x^2 + {ans[1]}*x + {ans[2]}")





start, finish = list(map(float, input("$ ").split()))

if start >= finish:
    raise Exception

# X = 1e-3

x1 = start * (1 + (3 - 5 ** 0.5) / 2)
x2 = start * (1 - (5 ** 0.5 - 1) / 2)

y1 = lib.f(x1)
y2 = lib.f(x2)

fStart = lib.f(start)
fFinish = lib.f(finish)

# x = finish - ((finish - start) * lib.f(finish) / (lib.f(finish) - lib.f(start)))
# 
# x = start
# x = (lib.f(x + dX) - 2 * lib.f(x) + lib.f(x - dX)) / (dX ** 2)

accuracy = 1e-10
t = time()
while abs(x1 - x2) >= accuracy <= abs(start - finish):
    if fStart >= y1 >= y2:
        start, x1 = x1, x2
        fStart, y1 = y1, y2
        x2 = (1 + (3 - 5 ** 0.5) / 2) * start
        y2 = lib.f(x2)

    else:
        finish, x2 = x2, x1
        fFinish, y2 = y2, y1
        x1 = (1 - (5 ** 0.5 - 1) / 2) * finish
        y1 = lib.f(x1)
    
    # x = finish - ((finish - start) * lib.f(finish) / (lib.f(finish) - lib.f(start)))

    # x = (lib.f(x + dX) - 2 * lib.f(x) + lib.f(x - dX)) / (dX ** 2)

    # if x < 0:
    #     finish = x
    # else:
    #     start = x
    # print(f"{start = }; {finish = }; {x1 = }; {x2 = }; {y1 = }; {y2 = }")

print(f"{min(fStart, y1, y2, fFinish)}")
print(f"{time() - t}")

