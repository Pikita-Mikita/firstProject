from tkinter import *

window = Tk()
canva = Canvas(window, width=300, height=300, bg="white")

pathOrder = [1, 2, 3, 6, 4, 5, 1]

matrixOfCoordinates = []  # Создаем матрицу координат из файла с координатами
with open("coordinatePoint.txt", 'r') as file:
    for line in file:
        if line.strip():  # strip удаляет все стандартные(пробелы, табуляции)символы в начале и конце строки
            matrixOfCoordinates += [line.strip().split(" ")]

count_dots = len(matrixOfCoordinates)

for i in range(count_dots):  # Переводим координаты из строк в числа
    print("")
    for j in range(2):
        matrixOfCoordinates[i][j] = float(matrixOfCoordinates[i][j])
        print(matrixOfCoordinates[i][j], end=' ')


def drawLine(p1, p2, canva):  # Функция рисования линии
    x1 = int(p1[0] * 30)
    y1 = int(p1[1] * 30)
    x2 = int(p2[0] * 30)
    y2 = int(p2[1] * 30)
    result1 = canva.create_line(x1, y1, x2, y2)  # Команда на отрисовку линии должна быть здесь
    return result1


# result2 = canva.create_text(x1, y1 + 10, text="", justify=CENTER, font="Verdana 8")
'''
x1, y1, x2, y2 = 10, 20, 30, 40
window = Tkinter.Tk()
canva = Tkinter.Canvas(window)
line = canva.create_line(x1, y1, x2, y2)
canva.pack()
'''

x = 0
for n in range(0, len(pathOrder)):  # Алгоритм проходит по матрице координат в порядке списка пути
    if x != len(pathOrder) - 2:
        x = n
        y = n + 1
        drawL = drawLine(matrixOfCoordinates[x], matrixOfCoordinates[y], canva)
        x += 1
    else:
        x = n
        y = 0
        drawL = drawLine(matrixOfCoordinates[x], matrixOfCoordinates[y], canva)
        break
canva.pack()
lab = Label(window, text="Схема соединения потребителей между собой", font="Arial 16")
lab.pack()

window.minsize(width=800, height=500)
window.mainloop()

