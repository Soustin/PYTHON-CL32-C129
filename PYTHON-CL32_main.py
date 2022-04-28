import csv

data = []
with open("test.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)

headers = data[0]
planet_data = data[1:]

for datapoints in planet_data:
    datapoints[2] = datapoints[2].lower()

planet_data.sort(key=lambda planet_data:planet_data[2])

with open("NEW_sorted.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)