import matplotlib.pyplot as plt
import numpy as np
import wx



def show(matrix):
    for i in range(matrix.shape[0]):
        plt.scatter(matrix[i,0] , matrix[i,1]) # scatter - метод для нанесения маркера в точке

    plt.show()

# зависимость линейной функции y = a*x + b
def lin_func(matrix):
    return 0


def main():
    # Таблица значений некоторой функциональной зависимости
    matrix = np.array([[1, 1], [2, 1.5], [3, 3], [4, 4.5], [5, 7], [6, 8.5]])

    show(matrix) # Вывод точек

    #print(matrix.shape[0])

if __name__ == '__main__':
    main()