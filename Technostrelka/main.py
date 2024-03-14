import csv
import numpy as np
import matplotlib.pyplot as plt
with open("students_data.csv", "r") as main:
    data = []
    reader = csv.reader(main)
    for row in reader:
        data.append(row)

# Словарь для более удобной работы, придумаете че с ним делать
# main_dict = {0: 'ID', 1: 'Subject', 2: 'school', 3: 'sex', 4: 'age', 5: '', 6: '', 7: '', 8: ''}
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
def mistakes(data):
    mistakes_count = 0
    for i in range(1, len(data)):
        for j in range(35):
            if j == 0:
                if len(list(data[i][j])) > 6:
                    mistakes_count += 1
            elif j == 1:
                if data[i][j] != 'Math' or data[i][j] != 'Por':
                    mistakes_count += 1
            elif j == 2:
                if data[i][j] not in ['GP', 'MS']:
                    mistakes_count += 1
            elif j == 3:
                if data[i][j] not in ['F', 'M']:
                    mistakes_count += 1
            elif j == 4:
                if not (10 < int(data[i][j]) < 40):
                    mistakes_count += 1
            elif j == 5:
                if data[i][j] not in ['U', 'R']:
                    mistakes_count += 1
            elif j == 6:
                if data[i][j] not in ['GT3', 'LE3']:
                    mistakes_count += 1
            elif j == 7:
                if data[i][j] not in ['T', 'A']:
                    mistakes_count += 1
            elif j == 8 or j == 9:
                if not (data[i][j].isdigit() and 0 <= int(data[i][j]) <= 4):
                    mistakes_count += 1
                elif type(data[i][j]) != int:
                    mistakes_count += 1
            elif j == 10 or j == 11:
                if data[i][j] not in ['teacher', 'health', 'services', 'at_home', 'other']:
                    mistakes_count += 1
            elif j == 12:
                if data[i][j] not in ['home', 'reputation', 'course', 'other']:
                    mistakes_count += 1
            elif j == 13:
                if data[i][j] not in ['mother', 'father', 'other']:
                    mistakes_count += 1
            elif j == 14 or j == 15:
                if not (1 <= int(data[i][j]) <= 4):
                    mistakes_count += 1
            elif 17 <= j <= 24:
                if data[i][j] not in ['yes', 'no']:
                    mistakes_count += 1
            elif j == 32:
                if data[i][j] not in ['yes', 'no']:
                    mistakes_count += 1
            elif 25 <= j <= 30:
                if not (data[i][j].isdigit() and 1.0 <= float(data[i][j]) <= 5.0):
                    mistakes_count += 1
            elif j == 31:
                if not (type(data[i][j] == int)):
                    mistakes_count += 1
    return f'Ошибки: {mistakes_count}'

print(mistakes(data))
_separation()

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
    return f'Пропусков {res} в таких параметрах как: {keys_str}'
print(misses(data))
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