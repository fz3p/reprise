import csv
import sys 

def header_to_csv(path_filename):
    print("load header_to_csv")
    print(path_filename.get())
    file = open(path_filename.get()+'.csv', "w")

    # just first line 
    line_number= 0
    diese = "# "
    with open(path_filename.get()) as csvfile:
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
    file = open(path_filename.get()+'.csv', "r")
    print(file.read())
    file.close()
