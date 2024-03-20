import csv
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

def correction(data):
    for i in range(len(data)):
        if data[i][28] == '':
            data[i][28] = 1.0 # Берем за минимальное, т. к. никаким другим образом мы определить не можем
        if data[i][29] == '':
            data[i][29] = 1.0 # Берем за минимальное, т. к. никаким другим образом мы определить не можем
        if data[i][24] == '':
            data[i][24] = 'no'
        if data[i][32] == '':
            data[i][32] = 'no'
        if data[i][25] == '':
            data[i][25] = 1.0
correction(data)

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
        print("Среднее количество затрачиваемого времени на учебу по природоведению: < 2 hours")

    elif Por_2 > Por_3 and Por_1 < Por_2 and Por_2 > Por_4:
        print("Среднее количество затрачиваемого времени на учебу по природоведению: 2 - 5 hours")

    elif Por_3 > Por_2 and Por_1 < Por_3 and Por_3 > Por_4:
        print("Среднее количество затрачиваемого времени на учебу по природоведению: 5 - 10 hours")

    elif Por_4 > Por_2 and Por_4 > Por_3 and Por_1 < Por_4:
        print("Среднее количество затрачиваемого времени на учебу по природоведению: > 10 hours")

    if Math_1 > Math_2 and Math_1 > Math_3 and Math_1 > Math_4:
        print("Среднее количество затрачиваемого времени на учебу по математике: < 2 hours")

    elif Math_1 < Math_2 and Math_2 > Math_3 and Math_2 > Math_4:
        print("Среднее количество затрачиваемого времени на учебу по математике: 2 - 5 hours")

    elif Math_3 > Math_2 and Math_1 < Math_3 and Math_3 > Math_4:
        print("Среднее количество затрачиваемого времени на учебу по математике: 5 - 10 hours")

    elif Math_4 > Math_2 and Math_4 > Math_3 and Math_1 < Math_4:
        print("Среднее количество затрачиваемого времени на учебу по математике: > 10 hours")

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
        print("Главной причиной выбора государственной школы (GP) стало расположение рядом с домом (home)")
    elif home_GP < reputation_GP and reputation_GP > course_GP and reputation_GP > other_GP:
        print("Главной причиной выбора государственной школы (GP) стала репутация школы (reputation)")
    elif course_GP > reputation_GP and home_GP < course_GP and course_GP > other_GP:
        print("Главной причиной выбора государственной школы (GP) стали преподаваемые предметы (course)")
    elif other_GP > reputation_GP and other_GP > course_GP and home_GP < other_GP:
        print("Главной причиной выбора государственной школы (GP) стали иные причины (other)")

    if home_MS > reputation_MS and home_MS > course_MS and home_MS > other_MS:
        print("Главной причиной выбора частной школы (MS) стало расположение рядом с домом (home)")
    elif home_MS < reputation_MS and reputation_MS > course_MS and reputation_MS > other_MS:
        print("Главной причиной выбора частной школы (MS) стала репутация школы (reputation)")
    elif course_MS > reputation_MS and home_MS < course_MS and course_MS > other_MS:
        print("Главной причиной выбора частной школы (MS) стали преподаваемые предметы (course)")
    elif other_MS > reputation_MS and other_MS > course_MS and home_MS < other_MS:
        print("Главной причиной выбора частной школы (MS) стали иные причины (other)")

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
_separation()
# Задание 6.1
def time_on_street(data):
    sliced_data = [[row[3]]+row[28:30] for row in data[1:]]
    man_time = 0
    fem_time = 0
    for i in range(len(sliced_data)):
        for j in range(len(sliced_data[i])):
            if sliced_data[i][0] == "M":
                man_time += float(sliced_data[i][1]) + float(sliced_data[i][2])
            elif sliced_data[i][0] == "F":
                fem_time += float(sliced_data[i][1]) + float(sliced_data[i][2])
    if man_time > fem_time:
       print("Мальчики проводят времени на улице больше чем девочки")
    elif man_time < fem_time:
       print("Девочки проводят времени на улице больше чем мальчики")
    elif man_time == fem_time:
       print("Мальчики и девочки проводят одиннаковое количество времени на улице")
time_on_street(data)
_separation()

# Задание 7
def depend_on_sex(data):
    male = []
    fem = []
    for i in range(len(data)):
        if data[i][3] == 'M':
            male.append(int(data[i][35]))
        elif data[i][3] == 'F':
            fem.append(int(data[i][35]))
    avg_male = sum(male)/len(male)
    avg_fem = sum(fem)/len(fem)
    return [avg_fem, avg_male]
print(depend_on_sex(data))

def depend_on_traveltime(data):
    time_1 = []
    time_2 = []
    time_3 = []
    time_4 = []
    for i in range(len(data)):
        if data[i][14] == '1':
            time_1.append(int(data[i][35]))
        elif data[i][14] == '2':
            time_2.append(int(data[i][35]))
        elif data[i][14] == '3':
            time_3.append(int(data[i][35]))
        elif data[i][14] == '4':
            time_4.append(int(data[i][35]))
    avg_time_1 = sum(time_1)/len(time_1)
    avg_time_2 = sum(time_2)/len(time_2)
    avg_time_3 = sum(time_3)/len(time_3)
    avg_time_4 = sum(time_4)/len(time_4)
    return [avg_time_1, avg_time_2, avg_time_2, avg_time_3, avg_time_4]
print(depend_on_traveltime(data))

def depend_on_famsup(data):
    famsup_yes = []
    famsup_no = []
    for i in range(1, len(data)):
        if data[i][18] == 'yes':
            famsup_yes.append(int(data[i][35]))
        elif data[i][18] == 'no':
            famsup_no.append(int(data[i][35]))
    avg_famsup_yes = sum(famsup_yes)/len(famsup_yes)
    avg_famsup_no = sum(famsup_no)/len(famsup_no)
    return[avg_famsup_yes, avg_famsup_no]
print(depend_on_famsup(data))


def depend_on_schoolsup(data):
    schoolsup_yes = []
    schoolsup_no = []
    for i in range(1, len(data)):
        if data[i][17] == 'yes':
            schoolsup_yes.append(int(data[i][35]))
        elif data[i][17] == 'no':
            schoolsup_no.append(int(data[i][35]))
    avg_schoolsup_yes = sum(schoolsup_yes)/len(schoolsup_yes)
    avg_schoolsup_no = sum(schoolsup_no)/len(schoolsup_no)
    return [avg_schoolsup_yes, avg_schoolsup_no]
print(depend_on_schoolsup(data))

def depend_on_paid(data):
    paid_yes = []
    paid_no = []
    for i in range(1, len(data)):
        if data[i][19] == 'yes':
            paid_yes.append(int(data[i][35]))
        elif data[i][19] == 'no':
            paid_no.append(int(data[i][35]))
    avg_paid_yes = sum(paid_yes)/len(paid_yes)
    avg_paid_no = sum(paid_no)/len(paid_no)
    return [avg_paid_yes, avg_paid_no]
print(depend_on_paid(data))

def depend_on_internet(data):
    internet_yes = []
    internet_no = []
    for i in range(1, len(data)):
        if data[i][23] == 'yes':
            internet_yes.append(int(data[i][35]))
        elif data[i][23] == 'no':
            internet_no.append(int(data[i][35]))
    avg_internet_yes = sum(internet_yes)/len(internet_yes)
    avg_internet_no = sum(internet_no)/len(internet_no)
    return [avg_internet_yes, avg_internet_no]
print(depend_on_internet(data))

def depend_on_Dalc(data):
    dalc_1 = []
    dalc_2 = []
    dalc_3 = []
    dalc_4 = []
    dalc_5 = []
    for i in range(1, len(data)):
        if data[i][28] == '1.0':
            dalc_1.append(int(data[i][35]))
        elif data[i][28] == '2.0':
            dalc_2.append(int(data[i][35]))
        elif data[i][28] == '3.0':
            dalc_3.append(int(data[i][35]))
        elif data[i][28] == '4.0':
            dalc_4.append(int(data[i][35]))
        elif data[i][28] == '5.0':
            dalc_5.append(int(data[i][35]))
    avg_dalc_1 = sum(dalc_1)/len(dalc_1)
    avg_dalc_2 = sum(dalc_2)/len(dalc_2)
    avg_dalc_3 = sum(dalc_3)/len(dalc_3)
    avg_dalc_4 = sum(dalc_4)/len(dalc_4)
    avg_dalc_5 = sum(dalc_5)/len(dalc_5)
    return [avg_dalc_1, avg_dalc_2, avg_dalc_3, avg_dalc_4, avg_dalc_5]
print(depend_on_Dalc(data))

def depend_on_Walc(data):
    walc_1 = []
    walc_2 = []
    walc_3 = []
    walc_4 = []
    walc_5 = []
    for i in range(1, len(data)):
        if data[i][28] == '1.0':
            walc_1.append(int(data[i][35]))
        elif data[i][28] == '2.0':
            walc_2.append(int(data[i][35]))
        elif data[i][28] == '3.0':
            walc_3.append(int(data[i][35]))
        elif data[i][28] == '4.0':
            walc_4.append(int(data[i][35]))
        elif data[i][28] == '5.0':
            walc_5.append(int(data[i][35]))
    avg_walc_1 = sum(walc_1)/len(walc_1)
    avg_walc_2 = sum(walc_2)/len(walc_2)
    avg_walc_3 = sum(walc_3)/len(walc_3)
    avg_walc_4 = sum(walc_4)/len(walc_4)
    avg_walc_5 = sum(walc_5)/len(walc_5)
    return [avg_walc_1, avg_walc_2, avg_walc_3, avg_walc_4, avg_walc_5]
print(depend_on_Walc(data))
_separation()

# Задание 8.1 + 8.2
def both_subjects(data):
    num_people = 0
    subject = [row[1] for row in data[1:]]
    sliced_data = [row[3:12] + [row[13]] + row[20:26] + row[27:31] for row in data[1:]]
    marks = [[row[1]] + [row[35]] for row in data[1:]] # Сравниваем итоговые оценки
    mark_math = 0
    mark_por = 0
    mark_equals = 0
    for i in range(len(sliced_data)):
        for j in range(i+1, len(sliced_data)):
            if sliced_data[i] == sliced_data[j] and subject[i] != subject[j]:
                if marks[i][0] == "Por":
                    if marks[i][1] > marks[j][1]:
                        mark_por += 1
                    elif marks[i][1] < marks[j][1]:
                        mark_math += 1
                    elif marks[i][1] == marks[j][1]:
                        mark_equals +=1
                elif marks[i][0] == "Math":
                    if marks[i][1] > marks[j][1]:
                        mark_math += 1
                    elif marks[i][1] < marks[j][1]:
                        mark_por += 1
                    elif marks[i][1] == marks[j][1]:
                        mark_equals += 1
                num_people += 1
    print(f"Количество людей, учащихся по обоим предметам: {num_people}")
    print(f"Количество людей, у которых оценка по математике лучше, чем оценка по природоведению: {mark_math}")
    print(f"Количество людей, у которых оценка по природоведению лучше, чем оценка по математике: {mark_por}")
    print(f"Количество людей, которые имеют одинаковые оценки по обоим предмета {mark_equals}")
both_subjects(data)
_separation()

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

with open("corrected_students_data.csv", 'w', newline='') as my_csv: # Запись исправленной (не польностью) матрицы
    csvWriter = csv.writer(my_csv, delimiter=',')
    csvWriter.writerows(data)
