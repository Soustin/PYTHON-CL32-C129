import csv

dataset1 = []
dataset2 = []

with open("dataset_1.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset1.append(row)

with open("NEW_sorted.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset2.append(row)

header1 = dataset1[0]
planet_data1 = dataset1[1:]

header2 = dataset2[0]
planet_data2 = dataset2[1:]

headers = header1 + header2
planet_data_total = []

for index, datarow in enumerate(planet_data1):
    planet_data_total.append(planet_data1[index]+planet_data2[index])

with open("final.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerow(planet_data_total)