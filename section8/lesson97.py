import csv

with open("section8/test.csv", "w") as csv_file:
    fieldnames = ["name", "count"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"name": "A", "count": 1})
    writer.writerow({"name": "B", "count": 2})

with open("section8/test.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(row["name"], row["count"])
