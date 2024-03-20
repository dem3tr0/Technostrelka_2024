import pandas as pd
import csv

with open("students_data.csv", "r") as main:
    data = []
    reader = csv.reader(main)
    for row in reader:
        data.append(row)


main_dict = {}
names = [el for el in data[0][:]]
for i in range(len(names)):
    main_dict.update({i: str(names[i])})

def mistakes():
    df = pd.read_csv('students_data.csv')
    count = 0
    print(df)
    for i in range(1, 36):
        column_name = str(main_dict[i])
        column = df[column_name]
        column.mask(column.eq('')).dropna()
        print(column_name)
        for j in range(len(column)):
            if column_name == 'Subjects':
                if column[j] not in ['Por', 'Math']:
                    count += 1
                    print(column[j])
            elif column_name == 'school':
                if column[j] not in ['GP', 'MS']:
                    count += 1
                    print(column[j])
            if column_name == 'sex':
                if column[j] != 'F' and column[j] != 'M':
                    count += 1
                    column[j].replace('m', 'M')
                    print(column[j])
            elif column_name == 'address':
                if column[j] not in ['U', 'R']:
                    print(column[j])
                    count += 1
            elif column_name == 'famsize':
                if column[j] not in ['GT3', 'LE3']:
                    count += 1
                    print(column[j])
            elif column_name == 'Pstatus':
                if column[j] not in ['T', 'A']:
                    count += 1
                    column[j].replace('t', 'T')
                    print(column[j])
            elif column_name in ['Fedu', 'Medu']:
                if column[j].isdigit():
                    if int(column[j]) > 4 or int(column[j]) < 0:
                        count += 1
                        print(column[j])
                else:
                    count += 1
                    column[j].replace('o', '0')
                    print(column[j])
            elif column_name in ['Mjob', 'Fjob']:
                if column[j] not in ['services', 'other', 'at_home', 'teacher', 'health']:
                    count += 1
                    column[j].replace('at-home', 'at_home')
                    print(column[j])
            elif column_name == 'reason':
                if column[j] not in ['home', 'reputation', 'course', 'other']:
                    count += 1
                    print(column[j])
            elif column_name == 'guardian':
                if column[j] not in ['father', 'mother', 'other']:
                    count += 1
                    column[j].replace('futher', 'father')
                    print(column[j])
            elif column_name in ['traveltime', 'studytime']:
                int(column[j])
                if column[j] > 4 or column[j] < 1:
                    count += 1
                    print(column[j])
            elif column_name in ['romantic', 'schoolsup', 'famsup', 'paid', 'activities', 'nursery', 'higher', 'internet', 'cheating']:
                if column[j] not in ['yes', 'no']: # пропуски не учитываются за ошибки
                    count += 1
                    print(column[j])

    data = df.values.tolist()
    return count

print(mistakes())

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