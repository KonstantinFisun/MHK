import matplotlib.pyplot as plt
import numpy as np
import wx



def show(matrix):
    for i in range(matrix.shape[0]):
        plt.scatter(matrix[i,0] , matrix[i,1]) # scatter - метод для нанесения маркера в точке

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

    system_of_equation = ([[sum_xi2, sum_xi, sum_xi_yi], [sum_xi, matrix.shape[0], sum_yi]])
    m1 = np.array([[sum_xi2, sum_xi], [sum_xi, matrix.shape[0]]])
    v1 = np.array([sum_xi_yi, sum_yi])
    result = np.linalg.solve(m1, v1)
    print(np.around(result, 2))
    return 0


def main():
    # Таблица значений некоторой функциональной зависимости
    matrix = np.array([[1, 1], [2, 1.5], [3, 3], [4, 4.5], [5, 7], [6, 8.5]])

    #show(matrix) # Вывод точек

    #print(matrix.shape[0])
    lin_func(matrix)

if __name__ == '__main__':
    main()