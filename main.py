#!/usr/bin/python3


import lib


file = "src/data.txt" # 0 1 1 0
#file = "src/matrix.txt" # 1 0 1 0
#file = "src/matrix2.txt" # 1 0 -1 0 1
#file = "src/matrix3.txt" # 5 4 5 4
#file = "src/matrix4.txt" # 1 1 1
#file = "src/infinite_solutions.txt" # exception "Infinite number of solutions"
#file = "src/no_solutions.txt" # exception "No solutions"


with open(file, "r") as f:
    data = [list(map(int, s.split())) for s in f.readlines()]

print(lib.gauss(data))
