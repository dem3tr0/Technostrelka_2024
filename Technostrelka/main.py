import csv
with open("students_data.csv", "r") as main:
    data = []
    reader = csv.reader(main)
    for row in reader:
        data.append(row)  # Вывод таблицы как матрицы
    #for i in range(0, len(data) - 1):
        #print(*data[i])
    # Строчек в матрице - 1045, столбцов - 36

# Словарь для более удобной работы, придумаете че с ним делать
names ={'Subjects': {'Por': 1, 'Math': 2}, 'School': {'GP': 1, 'MS': 2}}

# Задание 1.1
# Категориальные признаки
cat_features = ['Subject', 'School', 'sex', 'address', 'famsize', 'Pstatus', 'Medu', 'Fedu', 'Mjob', 'Fjob', 'reason', 'guardian', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'romantic', 'cheating']

# Числовые признаки
num_features = ['traveltime', 'studytime', 'failures', 'famrel', 'freetime', 'goout', 'Dalc', 'Walc', 'health', 'abscenes', 'G1', 'G2', 'G3', 'G4'] # G4 Задание 9

# Задание 1 + 2
def mistakes(data):
    mistakes_count = 0
    misses_count = 0
    for i in range(1, len(data)):
        for j in range(35):
            if j == 0:
                if len(list(data[i][j])) > 6:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 1:
                if data[i][j] != 'Math' or data[i][j] != 'Por':
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 2:
                if data[i][j] not in ['GP', 'MS']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 3:
                if data[i][j] not in ['F', 'M']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 4:
                if not (10 < int(data[i][j]) < 40):
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 5:
                if data[i][j] not in ['U', 'R']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 6:
                if data[i][j] not in ['GT3', 'LE3']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 7:
                if data[i][j] not in ['T', 'A']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 8 or j == 9:
                if not (data[i][j].isdigit() and 0 <= int(data[i][j]) <= 4):
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
                elif type(data[i][j]) != int:
                    mistakes_count += 1
            elif j == 10 or j == 11:
                if data[i][j] not in ['teacher', 'health', 'services', 'at_home', 'other']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 12:
                if data[i][j] not in ['home', 'reputation', 'course', 'other']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 13:
                if data[i][j] not in ['mother', 'father', 'other']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 14 or j == 15:
                if not (1 <= int(data[i][j]) <= 4):
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif 17 <= j <= 24:
                if data[i][j] not in ['yes', 'no']:
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif j == 32:
                if data[i][j] not in ['yes', 'no']:
                    mistakes_count += 1
                elif data[i][j] in ['', ' ']:
                    misses_count += 1
            elif 25 <= j <= 30:
                if data[i][j] == '':
                    misses_count += 1
                elif not (1.0 <= float(data[i][j]) <= 5.0):
                    mistakes_count += 1
            elif j == 31:
                if not (type(data[i][j] == int)):
                    mistakes_count += 1
                elif data[i][j] == '':
                    misses_count += 1
            elif data[i][j] == '':
                mistakes_count += 1
    return [mistakes_count, misses_count]

print("Ошибки, пропуски: ", mistakes(data)) # Тест задания

#Задание 3.2
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

def avgMarks(data):
    mathGradesG1 = []
    mathGradesG2 = []
    mathGradesG3 = []
    porGradesG1 = []
    porGradesG2 = []
    porGradesG3 = []
    countPor = 0
    countMath = 0
    avgMathG1 = 0
    avgMathG2 = 0
    avgMathG3 = 0
    avgPorG1 = 0
    avgPorG2 = 0
    avgPorG3 = 0
    for i in range(len(data)):
        for j in range(len(data)):
            if(data[i][1] == 'Math'):
                countMath += 1
                mathGradesG1.append(int(data[i][33]))
                mathGradesG2.append(int(data[i][34]))
                mathGradesG3.append(int(data[i][35]))
                avgMathG1 = sum(mathGradesG1) / len(mathGradesG1)
                avgMathG2 = sum(mathGradesG2) / len(mathGradesG2)
                avgMathG3 = sum(mathGradesG3) / len(mathGradesG3)
            else:
                countPor += 1
                porGradesG1.append(int(data[i][33]))
                porGradesG2.append(int(data[i][34]))
                porGradesG2.append(int(data[i][35]))
                avgPorG1 = sum(porGradesG1)/len(porGradesG1)
                avgPorG2 = sum(porGradesG2)/len(porGradesG2)
                avgPorG3 = sum(porGradesG3)/len(porGradesG3)

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