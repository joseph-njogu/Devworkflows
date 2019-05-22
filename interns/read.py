import csv
records = []
with open('data.csv') as f:
      reader = csv.reader(f)
 
      for row in reader:
         records.append(row[0])
     #for column in reader:
        # records.append(column[1])
print("{title}\n".format(title=records[2]))
print("{title}\n".format(title=records[5]))