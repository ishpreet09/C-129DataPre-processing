import csv

data_1=[]
data_2=[]

with open('final.csv') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data_1.append(row)

with open('dataset_2_sorted.csv') as f:
    csvreader=csv.reader(f)
    for row in csvreader:
        data_2.append(row)

header_1=data_1[0]
planet_data_1=data_1[1:]

header_2=data_2[0]
planet_data_2=data_2[1:]

headers=header_1+header_2
planet_data = []
for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("final1.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)