import csv

# User input
f_path = input("Please enter file-path: ")

with open(f_path, "r") as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        print(line[1])