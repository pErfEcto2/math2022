def div(data: list, i: int, j: int) -> list:
    for k in range(j + 1, len(data) + 1):
        data[i][k] /= data[i][j]
    data[i][j] = 1
    return data

def draw(l: list) -> None:
    for row in l:
        print(row)

def sub(data: list, i1: int, i2: int) -> list:
    for k in range(i1 + 1, len(data) + 1):
        data[i2][k] -= data[i1][k]
    data[i2][i1] = 0
    return data

def gauss(data: list, f: bool = False) -> "list[int]":
    if f:
        print("start")
        draw(data)
        print("\n")

    dimensions = len(data)
    for d in range(dimensions):
        for i in range(d, dimensions):
            if data[i][d] != 0:
                if i != d:
                    data[i], data[d] = data[d], data[i]
                break
        else:
            raise Exception("Error")  

        for i in range(d, dimensions):
            if data[i][d] != 0:
                data = div(data, i, d)

        for i in range(d + 1, dimensions):
            if data[i][d] != 0:
                data = sub(data, d, i)
        if f:
            print(f"loop; iteration {d}")
            draw(data)
            print("\n")

    res = [0] * dimensions

    for i in range(dimensions - 1, -1, -1):
        s = 0
        for j in range(i + 1, dimensions):
            s += data[i][j] * res[j]
        res[i] = data[i][dimensions] - s
    
    return res
