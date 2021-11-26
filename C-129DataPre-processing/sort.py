import csv

data=[]
with open ('dataset_2.csv') as df:
    rd=csv.reader(df)
    for row in rd:
        data.append(row)

header=data[0]

list_1=data[1:]
for data_point in list_1:
    data_point[2]=data_point[2].lower() 

list_1.sort(key=lambda list_1: list_1[2])

with open ('dataset_2_sorted.csv', 'w') as df1:
    csvwritter=csv.writer(df1)
    csvwritter.writerow(header)
    csvwritter.writerows(list_1)
