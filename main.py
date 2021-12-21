import math


def matrix_input_1():
    print('Введите матрицу:')
    m = [list(map(lambda x: int(x), input().split(' ')))]
    for i in range(len(m[0]) - 1):
        a = list(map(lambda x: int(x), input().split(' ')))
        if len(a) != len(m[0]):
            return None
        m.append(a)
    return m


def matrix_input_2():
    print('Введите матрицу:')
    m = [list(map(lambda x: int(x), input().split(' ')))]
    for i in range(len(m[0]) - 2):
        a = list(map(lambda x: int(x), input().split(' ')))
        if len(a) != len(m[0]):
            return None
        m.append(a)
    return m


def vector_input():
    return list(map(lambda x: int(x), input().split(' ')))


def vectors_input():
    print('Введите первый вектор:')
    a = vector_input()
    print('Введите второй вектор:')
    b = vector_input()
    if len(b) == len(a):
        return a, b
    return None, None


def determinant(m):
    l = len(m)
    if l == 0:
        return None
    if l == 1:
        return m[0][0]
    if l == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    res = 0
    for i in range(l):
        d = []
        for k in range(1, l):
            d.append(m[k][:i] + m[k][i + 1:])
        # print(d, determinant(d), -1 ** i, i, m[0][i])
        # print(-1 ** i * m[0][i] * determinant(d))
        res += (-1) ** i * m[0][i] * determinant(d)
    return res


def vector_module(a):
    c = 0
    for i in a:
        c += i ** 2
    return c ** 0.5


def vector_angle(a, b):
    c = 0
    for i in range(len(a)):
        c += a[i] * b[i]
    return math.acos(round(c / (vector_module(a) * vector_module(b)), 6))


def inverse_matrix(m):
    d = determinant(m)


def kramer(m):
    d = [determinant(list(map(lambda x: x[:-1], m)))]
    for i in range(len(m)):
        # print(list(map(lambda x: x[:i] + [x[-1]] + x[i + 1:-1], m)))
        d.append(determinant(list(map(lambda x: x[:i] + [x[-1]] + x[i + 1:-1], m))))
    # print(d)
    a = []
    for i in range(1, len(d)):
        a.append(d[i] / d[0])
    return a


def square(a, b):
    u = math.sin(vector_angle(a, b)) * vector_module(a) * vector_module(b)
    return round(u, 4), round(u * 2, 4)




while True:
    fun = ["1. Обратная матрица", "2. Решение системы линейных уравнений методом Крамера", "3. Угол между векторами", "4. Площадь плоской фигуры, построенной на векторах"]
    print('\n'.join(fun))
    a = int(input("Введите номер функции:"))
    if a == 1:
        print(inverse_matrix(matrix_input_1()))
    if a == 2:
        print(*kramer(matrix_input_2()))
    if a == 3:
        print(vector_angle(*vectors_input()))
    if a == 4:
        print(*square(*vectors_input()))
