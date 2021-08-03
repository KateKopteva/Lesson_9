import csv
# ДОБАВЛЯЕМ ДАННЫЕ О ЛЮДЯХ В CSV файл
rows = [['Саша', 'Иванов', '2'],['Оля','Соколова','9']] # часть данных добавлена через терминал
with open('/home/katya/PycharmProjects/Lesson_9/file1.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerows(rows)
# ПРЕОБРАЗОВАНИЕ ДАННЫХ CSV файла В СЛОВАРЬ
with open('/home/katya/PycharmProjects/Lesson_9/file1.csv', 'r') as csvfile2:
    csvreader = csv.DictReader(csvfile2)
    grup1, grup2, grup3, grup4, grup5 = 0, 0, 0, 0, 0
    people = [row for row in csvreader]
    print(people)
    for i in people:
        if int(i[' Возраст']) <= 12:
            grup1 += 1
        elif int(i[' Возраст']) <= 18:
            grup2 += 1
        elif int(i[' Возраст']) <= 25:
            grup3 += 1
        elif int(i[' Возраст']) <= 40:
            grup4 += 1
        elif int(i[' Возраст']) > 40:
            grup5 += 1
# СОЗДАНИЕ ОТЧЕТНОГО CSV ФАЙЛА
fields =['Возрастные группы', 'Количество человек']
rows = [['1-12', grup1],['13-18', grup2], ['19-25', grup3], ['26-40', grup4], ['40+', grup5]]
with open('/home/katya/PycharmProjects/Lesson_9/file2.csv', 'w') as csvfile3:
    csvwriter2 = csv.writer(csvfile3)
    csvwriter2.writerow(fields)
    csvwriter2.writerows(rows)