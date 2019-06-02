import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")

firstrow = True

with open(csvpath, newline='') as csvfile:
	csvreader = csv.reader(csvfile, delimiter = ',')
	for row in csvreader:
		if firstrow == False and float(row[7]) >= 5:
			print(f"The cereal '{row[0]}' contains {row[7]} grams of fiber.")
		firstrow = False