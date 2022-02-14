import numpy
import matplotlib.pyplot as plt
import wx

fig = plt.figure() # Создание объекта
print (fig.axes) # Список текущих объектов
print (type(fig)) # тип объекта figure

plt.scatter(1.0 , 1.0) # scatter - метод для нанесения маркера в точке (1, 1)

# После нанесения графического элемента в виде маркера
# список текущих областей состоит из одной области

print (fig.axes)


plt.show()