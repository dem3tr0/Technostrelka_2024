import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
with open("students_data.csv", "r") as main:
    data = []
    reader = csv.reader(main)
    for row in reader:
        data.append(row)

# Словарь для более удобной работы, придумаете че с ним делать
main_dict = {}
names = [el for el in data[0][:]]
for i in range(len(names)):
    main_dict.update({i: str(names[i])})

def _separation():
    print('_' * 30)

# Задание 1.1
# Категориальные признаки
cat_features = ['Subject', 'School', 'sex', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'cheating']

# Числовые признаки
num_features = ['traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'abscenes', 'G1', 'G2', 'G3', 'G4'] # G4 Задание 9

# Задание 1.2 + 1.3
def mistakes():
    df = pd.read_csv('students_data.csv')
    count = 0
    for i in range(1, 36):
        column_name = str(main_dict[i])
        column = df[column_name]
        for j in range(len(column)):
            if column_name == 'Subjects':
                if column[j] not in ['Por', 'Math']:
                    count += 1
            elif column_name == 'school':
                if column[j] not in ['GP', 'MS']:
                    count += 1
            if column_name == 'sex':
                if column[j] != 'F' and column[j] != 'M':
                    count += 1
                    column[j].replace('m', 'M')
            elif column_name == 'address':
                if column[j] not in ['U', 'R']:
                    count += 1
            elif column_name == 'famsize':
                if column[j] not in ['GT3', 'LE3']:
                    count += 1
            elif column_name == 'Pstatus':
                if column[j] not in ['T', 'A']:
                    count += 1
                    column[j].replace('t', 'T')
            elif column_name in ['Fedu', 'Medu']:
                if column[j].isdigit():
                    if int(column[j]) > 4 or int(column[j]) < 0:
                        count += 1
                else:
                    count += 1
                    column[j].replace('o', '0')
            elif column_name in ['Mjob', 'Fjob']:
                if column[j] not in ['services', 'other', 'at_home', 'teacher', 'health']:
                    count += 1
                    column[j].replace('at-home', 'at_home')
            elif column_name == 'reason':
                if column[j] not in ['home', 'reputation', 'course', 'other']:
                    count += 1
            elif column_name == 'guardian':
                if column[j] not in ['father', 'mother', 'other']:
                    count += 1
                    column[j].replace('futher', 'father')
            elif column_name in ['traveltime', 'studytime']:
                int(column[j])
                if column[j] > 4 or column[j] < 1:
                    count += 1
            elif column_name in ['romantic', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'cheating']:
                if column[j] not in ['yes', 'no']: # пропуски не учитываются за ошибки
                    count += 1
            elif column_name in ['famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health']:
                if 1 > float(column[j]) > 5 or pd.isnull(column[j]):
                    count += 1
            elif column_name in ['G1', 'G2', 'G3']:
                if not (0 <= int(column[j]) <= 20):
                    count += 1
    data = df.values.tolist()
    return count

for i in range(len(data)):
    print(*data[i])

# Задание 2.1
def misses(data):
    res = 0
    keys = set()
    for i in range(1, len(data)):
        for j in range(0, 35):
            if data[i][j] == '':
                res += 1
                keys.add(main_dict[j])
    keys_str = ', '.join(sorted(keys))
    result_string = f'Пропусков {res} в таких параметрах как: {keys_str}'
    return res, keys_str, result_string
res, keys_str, result_string = misses(data)

print('Ошибок и опечаток в таблице: ', mistakes() - res)
_separation()

print(result_string)
_separation()

# Задание 3.1



# Задание 3.2
def count_schools(data):
    GP = 0
    MS = 0
    for i in range(1,len(data)):
        if data[i][2] == "GP":
            GP += 1
        elif data[i][2] == "MS":
            MS += 1
    return [GP, MS]
print("В государственных школах учится (GP): ", count_schools(data)[0], "\nВ частных школах учится (MS): ", count_schools(data)[1]) # Тест задания
_separation()

#Задание 3.3
def count_students(data):
    Por = 0
    Math = 0
    for i in range(1,len(data)):
        if data[i][1] == "Por":
            Por += 1
        elif data[i][1] == "Math":
            Math += 1

    return [Por, Math]
print("Природоведение (Por): ", count_students(data)[0], "\nМатематика (Math): ", count_students(data)[1])
_separation()

# Задание 3.4
def amount_failures(data):
    amount_por = 0
    amount_math = 0

    for i in range(0, len(data)):
        if data[i][1] == "Math":
            amount_por += int(data[i][16])
        elif data[i][1] == "Por":
            amount_math += int(data[i][16])
    print("Количество завалов по математике (Math): ", amount_math, "\nКоличество завалов по природоведению (Por): ", amount_por)

    if amount_por > amount_math:
        print('Природоведение заваливают чаще')
    elif amount_por < amount_math:
        print('Математику заваливают чаще')

    elif amount_por == amount_math:
        print("Оба предмета заваливают одинаково")

amount_failures(data)
_separation()

def amount_studytime(data):
    Por_1 = 0
    Por_2 = 0
    Por_3 = 0
    Por_4 = 0

    Math_1 = 0
    Math_2 = 0
    Math_3 = 0
    Math_4 = 0

    for i in range(0, len(data)):
        if data[i][1] == "Math":
            if int(data[i][15]) == 1:
                Math_1 += 1
            elif int(data[i][15]) == 2:
                Math_2 += 1
            elif int(data[i][15]) == 3:
                Math_3 += 1
            elif int(data[i][15]) == 4:
                Math_4 += 1
        elif data[i][1] == "Por":
            if int(data[i][15]) == 1:
                Por_1 += 1
            elif int(data[i][15]) == 2:
                Por_2 += 1
            elif int(data[i][15]) == 3:
                Por_3 += 1
            elif int(data[i][15]) == 4:
                Por_4 += 1

    if Por_1 > Por_2 and Por_1 > Por_3 and Por_1 > Por_4:
        print("amount_studytime Por: < 2 hours")

    elif Por_2 > Por_3 and Por_1 < Por_2 and Por_2 > Por_4:
        print("amount_studytime Por: 2 - 5 hours")

    elif Por_3 > Por_2 and Por_1 < Por_3 and Por_3 > Por_4:
        print("amount_studytime Por: 5 - 10 hours")

    elif Por_4 > Por_2 and Por_4 > Por_3 and Por_1 < Por_4:
        print("amount_studytime Por: > 10 hours")

    if Math_1 > Math_2 and Math_1 > Math_3 and Math_1 > Math_4:
        print("amount_studytime Math: < 2 hours")

    elif Math_1 < Math_2 and Math_2 > Math_3 and Math_2 > Math_4:
        print("amount_studytime Math: 2 - 5 hours")

    elif Math_3 > Math_2 and Math_1 < Math_3 and Math_3 > Math_4:
        print("amount_studytime Math: 5 - 10 hours")

    elif Math_4 > Math_2 and Math_4 > Math_3 and Math_1 < Math_4:
        print("amount_studytime Math: > 10 hours")

amount_studytime(data)
_separation()

# Задание 3.6
def amount_reasons(data):
    home_GP = 0
    reputation_GP = 0
    course_GP = 0
    other_GP = 0

    home_MS = 0
    reputation_MS = 0
    course_MS = 0
    other_MS = 0

    for i in range(0, len(data)):
        if data[i][2] == "GP":
            if data[i][12] == "home":
                home_GP += 1
            elif data[i][12] == "reputation":
                reputation_GP += 1
            elif data[i][12] == "course":
                course_GP += 1
            elif data[i][12] == "other":
                other_GP += 1
        elif data[i][2] == "MS":
            if data[i][12] == "home":
                home_MS += 1
            elif data[i][12] == "reputation":
                reputation_MS += 1
            elif data[i][12] == "course":
                course_MS += 1
            elif data[i][12] == "other":
                other_MS += 1

    if home_GP > reputation_GP and home_GP > course_GP and home_GP > other_GP:
        print("The main reason of choosing GP school is home")
    elif home_GP < reputation_GP and reputation_GP > course_GP and reputation_GP > other_GP:
        print("The main reason of choosing GP school is reputation")
    elif course_GP > reputation_GP and home_GP < course_GP and course_GP > other_GP:
        print("The main reason of choosing GP school is course")
    elif other_GP > reputation_GP and other_GP > course_GP and home_GP < other_GP:
        print("The main reason of choosing GP school is other")

    if home_MS > reputation_MS and home_MS > course_MS and home_MS > other_MS:
        print("The main reason of choosing MS school is home")
    elif home_MS < reputation_MS and reputation_MS > course_MS and reputation_MS > other_MS:
        print("The main reason of choosing MS school is reputation")
    elif course_MS > reputation_MS and home_MS < course_MS and course_MS > other_MS:
        print("The main reason of choosing MS school is course")
    elif other_MS > reputation_MS and other_MS > course_MS and home_MS < other_MS:
        print("The main reason of choosing MS school is other")

amount_reasons(data)
_separation()

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

# Задание 9
def G4 (data):
    G4 = ['G4']
    for i in range(1, len(data)):
        grade = int(data[i][35])
        if 18 <= grade <= 20:
            G4.append('excellent')
        elif 14 <= grade <= 17:
            G4.append('good')
        elif 8 <= grade <= 13:
            G4.append('satisfactory')
        elif grade < 8:
            G4.append('unsatisfactory')
    return G4

for i in range(len(data)):
    data[i].append(G4(data)[i])

for i in range(len(data)):
    print(*data[i])
_separation()
# task 8.1
def both_subjects(data):
    num_people = 0
    sliced_data = [row[3:12] + [row[13]] + row[20:26] + row[27:30] for row in data[1:]]
    for i in range(len(sliced_data)):
        print(*sliced_data[i])
    return num_people
print(both_subjects(data))
_separation()
