import csv
records = []
with open('data.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] == 'f':
            records.append(row[0])
print(records)
