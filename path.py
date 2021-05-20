import math
from tkinter import *

# Создаем матрицу координат из файла с координатами
matrixOfCoordinates = []
with open("coordinatePoint.txt", 'r') as file:
    for line in file:
        if line.strip():  # strip удаляет все стандартные(пробелы, табуляции)символы в начале и конце строки
            matrixOfCoordinates += [line.strip().split(" ")]

# Число точек
count_dots = len(matrixOfCoordinates)

# Выводим матрицу координат в консоль
print("Матрица координат:")

# Меняем тип координат из строки в число
for i in range(count_dots):
    print("")
    for j in range(2):
        matrixOfCoordinates[i][j] = float(matrixOfCoordinates[i][j])
        print(matrixOfCoordinates[i][j], end=' ')
print("\n")

# Сохраняем матрицу в итоговый файл
with open('resultData.txt', 'w') as fileResult:
    fileResult.write("Матрица кординат:\n")
    for row in matrixOfCoordinates:
        fileResult.write(' '.join([str(a) for a in row]) + '\n')
    fileResult.write("\nЧисло потребителей: " + str(count_dots))
print("Число вершин:", count_dots)


# Функция считает расстояние между точками
def distance(p1, p2):
    resultDistance = math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)
    resultDistance = float("{0:.1f}".format(resultDistance))
    return resultDistance


# Формируем матрица расстояний между точками
dis = 0
matrixOfDistance = []
n = count_dots
for v in range(0, n):
    matrixOfDistance.append([])
    for k in range(0, count_dots):
        dis = distance(matrixOfCoordinates[v], matrixOfCoordinates[k])
        matrixOfDistance[v].append(dis)

# Вывод матрицы расстояний на экран
print("Матрица расстояний: ")
for i in range(len(matrixOfDistance)):
    print("")
    for j in range(len(matrixOfDistance)):
        print(matrixOfDistance[i][j], end=' ')

# Сохраняем матрицу расстояний в итоговый файл
with open('resultData.txt', 'a') as fileResult:
    fileResult.write("\nМатрица расстояний:\n")
    for row in matrixOfDistance:
        fileResult.write(' '.join([str(a) for a in row]) + '\n')
print("")


# ----------------------------------------------

# Ищем порядок пути и его длину алгоритмом Литтла
# Функция нахождения минимального элемента, исключая текущий элемент
def Min(lst, myindex):
    return min(x for idx, x in enumerate(lst) if idx != myindex)


# Функция удаления нужной строки и столбца
def Delete(matrix, index1, index2):
    del matrix[index1]
    for i in matrix:
        del i[index2]
    return matrix


n = count_dots  # Колличество вершин графов
matrix = matrixOfDistance  # Базовая матрица
PathLenght = 0
Str = []  # Массив для индексов
Stb = []  # Массив для индексов
res = []  # Нужный путь
result = []  # Порядок пути
StartMatrix = []  # Изначальная матрица

# Создаем массивы для сохранения индексов
for i in range(n):
    Str.append(i)
    Stb.append(i)

# Сохраняем изначальную матрицу
for i in range(n): StartMatrix.append(matrix[i].copy())

# Присваеваем главной диагонали float(inf)
for i in range(n): matrix[i][i] = float('inf')

while True:
    # Редуцируем
    # Вычитаем минимальный элемент в строках
    for i in range(len(matrix)):
        temp = min(matrix[i])  # Ищем минимальный элемент в строке
        for j in range(len(matrix)):
            matrix[i][j] -= temp  # Вычитаем минимальный элемент из всех элементов строки

    # Вычитаем минимальный элемент в столбцах
    for i in range(len(matrix)):
        temp = min(row[i] for row in matrix)  # Ищем минимальный элемент в столбце
        for j in range(len(matrix)):  # Вычитаем минимальный элемент из всех элементов в столбце
            matrix[j][i] -= temp

    # Оцениваем нулевые клетки и ищем нулевую клетку с максимальной оценкой
    NullMax = 0  # Максимальная оценка нулевой клетки
    index1 = 0  # Индексы этой нулевой клетки
    index2 = 0
    tmp = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == 0:
                tmp = Min(matrix[i], j) + Min((row[j] for row in matrix), i)  # Оценка нулевой клетки
                if tmp >= NullMax:  # Сравнение оценки нулевой клетки
                    NullMax = tmp
                    index1 = i
                    index2 = j

    # Находим нужный нам путь, записываем его в res и удаляем все ненужное
    res.append(Str[index1] + 1)
    res.append(Stb[index2] + 1)

    oldIndex1 = Str[index1]
    oldIndex2 = Stb[index2]
    if oldIndex2 in Str and oldIndex1 in Stb:
        NewIndex1 = Str.index(oldIndex2)
        NewIndex2 = Stb.index(oldIndex1)
        matrix[NewIndex1][NewIndex2] = float('inf')
    del Str[index1]  # Удаляем использованные индексы
    del Stb[index2]
    matrix = Delete(matrix, index1, index2)  # Удаляем нужную строку и столбец
    if len(matrix) == 1: break

# Формируем порядок пути
for i in range(0, len(res) - 1, 2):
    if res.count(res[i]) < 2:  # Если число меньше двух
        result.append(res[i])
        result.append(res[i + 1])
for i in range(0, len(res) - 1, 2):
    for j in range(0, len(res) - 1, 2):
        if result[len(result) - 1] == res[j]:
            result.append(res[j])
            result.append(res[j + 1])
# Выстраиваем правильный порядок пути
order = []
for i in result:
    if i not in order:
        order.append(i)
order.insert(0, 1)

print("----------------------------------")
print("Порядок пути: ", order[::-1])

# Считаем длину пути
for i in range(0, len(result) - 1, 2):
    if i == len(result) - 2:
        PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
        PathLenght += StartMatrix[result[i + 1] - 1][result[0] - 1]
    else:
        PathLenght += StartMatrix[result[i] - 1][result[i + 1] - 1]
PathLenght = float("{0:.1f}".format(PathLenght))
print("Длина пути: ", PathLenght)
PathLenght = str(PathLenght)
print("----------------------------------")

# Добавляем порядок и длину пути в конечный файл
pathOrder = order[::-1]
with open('resultData.txt', 'a') as fileResult:
    fileResult.write("\nПорядок пути: " + str(pathOrder))
    fileResult.write("\nДлина пути: " + PathLenght)

# ----------------------------------------------

# Выводим на экран и рисуем схему соединения потребителей
window = Tk()
canva = Canvas(window, width=300, height=300, bg="white")


# Функция рисования линии
def drawLine(p1, p2, canva):
    x1 = int(p1[0] * 30)
    y1 = int(p1[1] * 30)
    x2 = int(p2[0] * 30)
    y2 = int(p2[1] * 30)
    result1 = canva.create_line(x1, y1, x2, y2)  # Команда на отрисовку линии
    return result1


# Алгоритм проходит по матрице координат в порядке списка пути
x = 0
for n in range(0, len(pathOrder)):
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
Button(window, text="Получить данные", command=window.destroy).pack()
window.mainloop()

fileResult.close()
file.close()


'''fileResult.write("\nМатрица кординат:\n")
    for row in matrixOfCoordinates:
        fileResult.write(' '.join([str(a) for a in row]) + '\n')'''

# Сохраняем матрицу расстояний в итоговый файл
'''
with open('resultData.txt', 'a') as fileResult:
    fileResult.write("\nМатрица расстояний:\n")
    for row in matrixOfDistance:
        fileResult.write(' '.join([str(a) for a in row]) + '\n')'''
