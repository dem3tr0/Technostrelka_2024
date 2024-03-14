import numpy as np
import csv
import matplotlib.pyplot as plt

# Исходный двумерный массив
data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Дополнительная колонка для добавления
new_column = [10, 20, 30]

# Добавление новой колонки в каждую строку массива
for i in range(len(data)):
    data[i].append(new_column[i])

# Вывод результата
for row in data:
    print(row)

with open("students_data.csv", "r") as main:
    list = []
    reader = csv.reader(main)
    for row in reader:
        list.append(row)

def statistics(data):
    res = []
    for i in range(1, 35):
        sliced_data = np.array(data[:, i])
        if sliced_data.dtype.type == np.int64:
            res.append(np.mean(sliced_data))
    return res

print(statistics(data))

# Задание 4
def min_max_avg_mark(data, G):
    Gx = 0
    if G == 1:
        Gx = 33
    elif G == 2:
        Gx = 34
    elif G == 3:
        Gx = 35

    math_grades = []
    por_grades = []

    for i in range(1, len(data)):
        grade = int(data[i][Gx])
        if data[i][1] == 'Math':
            math_grades.append(grade)
        elif data[i][1] == 'Por':
            por_grades.append(grade)

    min_math = min(math_grades)
    max_math = max(math_grades)
    avg_math = int(sum(math_grades) / len(math_grades))

    min_por = min(por_grades)
    max_por = max(por_grades)
    avg_por = int(sum(por_grades) / len(por_grades))

    return min_math, max_math, avg_math, min_por, max_por, avg_por, math_grades, por_grades


G = int(input('Введите номер семестра (G1, G2, G3): '))
min_math, max_math, avg_math, min_por, max_por, avg_por, math_grades, por_grades = min_max_avg_mark(data, G)

# Построение графиков с границами для столбцов
fig, axs = plt.subplots(2, 2, figsize=(16, 12))

# График минимальных и максимальных оценок
axs[0, 0].bar(['Min Math', 'Max Math', 'Min Por', 'Max Por'], [min_math, max_math, min_por, max_por], edgecolor='black')
axs[0, 0].set_yticks(range(0, 21))
axs[0, 0].set_title('Минимальные и максимальные оценки')

# График средних оценок
axs[0, 1].bar(['Средняя Math', 'Средняя Por'], [avg_math, avg_por], edgecolor='black')
axs[0, 1].set_yticks(range(0, 21))
axs[0, 1].set_title('Средние оценки')

# График всех оценок по математике
axs[1, 0].hist(math_grades, bins=20, range=(0, 20), align='mid', edgecolor='black')
axs[1, 0].set_title('Все оценки по математике')
axs[1, 0].set_xticks(range(0, 21))
axs[1, 0].set_yticks(range(0, 61, 10))

# График всех оценок по природоведению
axs[1, 1].hist(por_grades, bins=20, range=(0, 20), align='mid', edgecolor='black')
axs[1, 1].set_title('Все оценки по природоведению')
axs[1, 1].set_xticks(range(0, 21))
axs[1, 1].set_yticks(range(0, 101, 10))

plt.tight_layout()
plt.show()