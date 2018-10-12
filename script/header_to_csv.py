import csv
import sys 
# arg
path_filename = sys.argv[1] 
list_filename = sys.argv[2]
file = open(list_filename, "w")

# just first line 
line_number= 0
diese = "# "
with open(path_filename) as csvfile:
	line = csv.reader(csvfile, delimiter=';')
	for row in line:
		column_number = 0
		if line_number == 0:
	 		for cell in row:
	 			file.write(diese + str(column_number) + " - " + cell + "\n")
	 			# print(diese + str(numero_column) + " - " + cell)
	 			column_number = column_number + 1
		line_number = line_number + 1
file.close()


# control at the end 
file = open(list_filename, "r")
print(file.read())
file.close()