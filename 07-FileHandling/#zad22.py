
import csv
with open('students.CSV') as csv_file:
    csv_r = csv.reader(csv_file, delimiter=',')
    a = int()
    for row in csv_r:
        if row == 0:
            pass
        elif eval(row[2]) <= 30:

            print(f'{row[0]}  {row[1]}   {row[4]}')

