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
