import math

import matplotlib.pyplot as plt
import numpy as np
import wx



def show(matrix):

    x = np.linspace(matrix[0,0]-1, matrix[-1,0]+1, num = 100)

    lin = lin_func(matrix)
    sed = sed_func(matrix)
    exp = exp_func(matrix)
    qua = qua_func(matrix)

    lin_y = lin[0]*x + lin[1]
    sed_y = sed[0]*np.power(x,sed[1])
    exp_y = exp[0]*np.exp(x*exp[1])
    qua_y = (qua[0]*x*x)+(qua[1]*x)+qua[2]

    fig, ax = plt.subplots()

    ax.plot(x, lin_y, label =f'y = {lin[0]}*x + {lin[1]}')
    ax.plot(x, sed_y, label=f'y = {sed[0]}*x^{sed[1]}')
    ax.plot(x, exp_y, label=f'y = {exp[0]}*exp^(x*{exp[1]})')
    ax.plot(x, qua_y, label=f'y = ({qua[0]}*x^2) + ({qua[1]}*x) + ({qua[2]}) ')

    ax.legend(fontsize = 15,
              ncol = 1, # Количество столбцов
              facecolor = 'oldlace', # Цвет области
              edgecolor = 'r', # Цвет крайней линии
              title = 'Прямые', # Заголовок
              title_fontsize = '20', # Размер шрифта
              loc = "upper right"
              )

    fig.set_figwidth(12)
    fig.set_figheight(12)

    for i in range(matrix.shape[0]):
        plt.scatter(matrix[i,0] , matrix[i,1], s = 20, color='black') # scatter - метод для нанесения маркера в точке

    plt.show()

# зависимость линейной функции y = a*x + b
def lin_func(matrix):

    # сумма по xi
    sum_xi = 0
    for i in range(matrix.shape[0]):
        sum_xi += matrix[i,0]

    # сумма по yi
    sum_yi = 0
    for i in range(matrix.shape[0]):
        sum_yi += matrix[i, 1]

    # сумма по xi^2
    sum_xi2 = 0
    for i in range(matrix.shape[0]):
        sum_xi2 += pow(matrix[i, 0], 2)

    # сумма по xi*yi
    sum_xi_yi = 0
    for i in range(matrix.shape[0]):
        sum_xi_yi += matrix[i,0] * matrix[i, 1]

    m1 = np.array([[sum_xi2, sum_xi], [sum_xi, matrix.shape[0]]]) # Матрица коэффициентов
    v1 = np.array([sum_xi_yi, sum_yi]) # Вектор свободных членов
    result = np.linalg.solve(m1, v1)
    # print(np.around(result, 2))
    return np.around(result, 2)

# зависимость степенной функции y = B * x^a
def sed_func(matrix):
    # X = ln(x) и Y = ln(y) получаем зависимость
    matrix_ln = matrix.copy() # Создаем копию массива
    for i in matrix_ln:
        i[0] = math.log(i[0])
        i[1] = math.log(i[1])

    # сумма по xi
    sum_xi = 0
    for i in range(matrix_ln.shape[0]):
        sum_xi += matrix_ln[i,0]

    # сумма по yi
    sum_yi = 0
    for i in range(matrix_ln.shape[0]):
        sum_yi += matrix_ln[i, 1]

    # сумма по xi^2
    sum_xi2 = 0
    for i in range(matrix_ln.shape[0]):
        sum_xi2 += pow(matrix_ln[i, 0], 2)

    # сумма по xi*yi
    sum_xi_yi = 0
    for i in range(matrix_ln.shape[0]):
        sum_xi_yi += matrix_ln[i,0] * matrix_ln[i, 1]

    # Найдем коэффициенты
    m1 = np.array([[sum_xi2, sum_xi], [sum_xi, matrix_ln.shape[0]]]) # Матрица коэффициентов
    v1 = np.array([sum_xi_yi, sum_yi]) # Вектор свободных членов
    result = np.around(np.linalg.solve(m1, v1),2)[::-1]

    result[0] = math.exp(result[0]).__round__(2)
    # print(result)
    return result

# Зависимость y от x в виде показательной функции y = B * e^(ax)
def exp_func(matrix):
    # x и Y = ln(y) получаем зависимость
    matrix_ln = matrix.copy()  # Создаем копию массива
    for i in matrix_ln:
        i[1] = math.log(i[1])

    # сумма по xi
    sum_xi = 0
    for i in range(matrix_ln.shape[0]):
        sum_xi += matrix_ln[i, 0]

    # сумма по yi
    sum_yi = 0
    for i in range(matrix_ln.shape[0]):
        sum_yi += matrix_ln[i, 1]

    # сумма по xi^2
    sum_xi2 = 0
    for i in range(matrix_ln.shape[0]):
        sum_xi2 += pow(matrix_ln[i, 0], 2)

    # сумма по xi*yi
    sum_xi_yi = 0
    for i in range(matrix_ln.shape[0]):
        sum_xi_yi += matrix_ln[i, 0] * matrix_ln[i, 1]

    # Найдем коэффициенты
    m1 = np.array([[sum_xi2, sum_xi], [sum_xi, matrix_ln.shape[0]]])  # Матрица коэффициентов
    v1 = np.array([sum_xi_yi, sum_yi])  # Вектор свободных членов
    result = np.around(np.linalg.solve(m1, v1), 2)[::-1]

    result[0] = math.exp(result[0]).__round__(2)
    # print(result)
    return result

# зависимость y от x в виде квадратичной функции y = ax^2 + bx + c
def qua_func(matrix):

    # сумма по xi
    sum_xi = 0
    for i in range(matrix.shape[0]):
        sum_xi += matrix[i, 0]

    # сумма по xi^3
    sum_xi3 = 0
    for i in range(matrix.shape[0]):
        sum_xi3 += pow(matrix[i, 0], 3)

    # сумма по xi^4
    sum_xi4 = 0
    for i in range(matrix.shape[0]):
        sum_xi4 += pow(matrix[i, 0], 4)

    # сумма по yi
    sum_yi = 0
    for i in range(matrix.shape[0]):
        sum_yi += matrix[i, 1]

    # сумма по xi^2
    sum_xi2 = 0
    for i in range(matrix.shape[0]):
        sum_xi2 += pow(matrix[i, 0], 2)

    # сумма по xi*yi
    sum_xi_yi = 0
    for i in range(matrix.shape[0]):
        sum_xi_yi += matrix[i, 0] * matrix[i, 1]

    # сумма по xi2*yi
    sum_xi2_yi = 0
    for i in range(matrix.shape[0]):
        sum_xi2_yi += pow(matrix[i, 0], 2) * matrix[i, 1]

    m1 = np.array([[sum_xi4, sum_xi3, sum_xi2], [sum_xi3, sum_xi2, sum_xi], [sum_xi2, sum_xi, matrix.shape[0]]])  # Матрица коэффициентов
    v1 = np.array([sum_xi2_yi, sum_xi_yi, sum_yi])  # Вектор свободных членов
    result = np.linalg.solve(m1, v1)
    # print(np.around(result, 2))
    return np.around(result, 2)

def main():
    # Таблица значений некоторой функциональной зависимости
    matrix = np.array([[1, 1], [2, 1.5], [3, 3], [4, 4.5], [5, 7], [6, 8.5]])
    show(matrix) # Вывод точек

if __name__ == '__main__':
    main()