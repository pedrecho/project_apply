from copy import copy


def matrix_input():
    m = []
    n, k = *input('Введите размер матрицы:').split(' '))
    print('Введите матрицу:')
    for i in range(int(n)):
        a = list(map(lambda x: int(x), input().split(' ')))
        if len(a) != int(k):
            return None
        m.append(a)
    return m


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


def inverse_matrix(m):
    d = determinant(m)


def kramer():
    return


while True:
    fun = ["1. Обратная матрица", "2. Решение системы линейных уравнений методом Крамера", "3. Угол между векторами", "4. Площадь плоской фигуры, построенной на векторах"]
    print('\n'.join(fun))
    a = int(input("Введите номер функции:"))
    if a == 1:
        print(inverse_matrix(matrix_input())