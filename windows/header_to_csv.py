import csv
import sys 

def header_to_csv(path_filename):
    # print("load header_to_csv")
    # print(path_filename.get())

    # just first line 
    line_number= 0
    diese = "# "
    array = []
    with open(path_filename.get()) as csvfile:
        line = csv.reader(csvfile, delimiter=';')
        for row in line:
            column_number = 0
            if line_number == 0:
                for cell in row:
                  array.append(diese + str(column_number) + " - " + cell)
                column_number = column_number + 1
            line_number = line_number + 1
 
    return array

