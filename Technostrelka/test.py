import numpy as np
import csv
import pandas as pd

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
    data = np.array(list[1:][:], dtype=str)

def statistics(data):
    res = []
    for i in range(1, 35):
        sliced_data = np.array(data[:, i])
        if sliced_data.dtype.type == np.int64:
            res.append(np.mean(sliced_data))
    return res

print(statistics(data))

df = pd.read_csv('students_data.csv')
df.head()
df.drop(['ID', 'school', 'sex','age','address','famsize','Pstatus','Medu','Fedu','Mjob','Fjob','reason','guardian','traveltime','studytime','failures','schoolsup','famsup','paid','activities','nursery','higher','internet','romantic','famrel','freetime','goout','Dalc','Walc','health','absences','cheating'],axis=1,inplace=True)
df.head()
df = df.set_index('Subject')

# Задание 4
def min_max_mark(data):
    G = int(input('Введите номер семестра (G1, G2, G3): '))
    Gx = 0
    if G == 1:
        Gx = 33
    elif G == 2:
        Gx = 34
    elif G == 3:
        Gx = 35
    math = []
    por = []
    for i in range(len(data)):
        if data[i][1] == 'Math':
            math.append(int(data[i][Gx]))
        elif data[i][1] == 'Por':
            por.append(int(data[i][Gx]))
    return [min(math), max(math), min(por), max(por)]

print("Наихудщая оценка по математике (Math): ", min_max_mark(data)[0], "наилучшая: ", min_max_mark(data)[1])
print("Наихудщая оценка по природоведению (Por): ", min_max_mark(data)[2], "наилучшая: ", min_max_mark(data)[3])

def avg_mark(data):
    G = int(input('semester(G) number = '))
    Gx = 0
    if (G == 1):
        Gx = 33
    elif(G == 2):
        Gx = 34
    elif(G == 3):
        Gx == 35
    math = []
    por = []

    for i in range(len(data)):
        if data[i][1] == 'Math':
            math.append(int(data[i][Gx]))
        elif data[i][1] == 'Por':
            por.append(int(data[i][Gx]))
    return [sum(math)/len(math), sum(por)/len(por)]

print("Средняя оценка по математике (Math): ", avg_mark(data)[0])
print("Средняя оценка по природоведению (Por): ", avg_mark(data)[1])

def count_grade_students(data):
    G = int(input('semester(G) number = '))
    Gx = 0
    if (G == 1):
        Gx = 33
    elif(G == 2):
        Gx = 34
    elif(G == 3):
        Gx == 35

    math_more_10 = 0
    math_more_15 = 0
    math_20 = 0
    por_more_10 = 0
    por_more_15 = 0
    por_20 = 0

    for i in range(len(data)):
        if data[i][1] == 'Math' and int(data[i][Gx]) >= 10:
            math_more_10 += 1
        elif data[i][1] == 'Math' and int(data[i][Gx]) >= 15:
            math_more_15 += 1
        elif data[i][1] == 'Math' and int(data[i][Gx]) == 20:
            math_20 += 1
        if data[i][1] == 'Por' and int(data[i][Gx]) >= 10:
            por_more_10 += 1
        elif data[i][1] == 'Por' and int(data[i][Gx]) >= 15:
            por_more_15 += 1
        elif data[i][1] == 'Por' and int(data[i][Gx]) == 20:
            por_20 += 1
    return[math_more_10, math_more_15, math_20, por_more_10, por_more_15, por_20]