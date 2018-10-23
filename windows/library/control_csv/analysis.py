
import csv
import sys
from re import sub, search


def analyse(path_filename): 
    line_number= 0
    array = []
    with open(path_filename.get()) as csvfile:
        line = csv.reader(csvfile, delimiter=';')
        for row in line:
            array_cell = []
            if line_number != 0:
                for cell in row:
                    array_cell.append(cell)
            array.append(array_cell)
            line_number = line_number + 1
    array = treatement(array)
    return array



def treatement(array):
    number_cell_in_line = len(array[1])
    integer = 0
    string = 0
   
    for line in array:
        i = 0
        while i < len(array[i]):
            value = analyse_cell(array[1][i])
            i += 1
            if value == 0:
                string += 1
            elif value == 1: 
                integer += 1
             
        percent_string = not_zero(string, array[i])
        percent_integer= not_zero(string, array[i])
        to_return = "string : " + str(percent_string) + "%, integer : " + str(percent_integer) + "%"
        analysis = []
        analysis.append(to_return)
    return analysis


def analyse_cell(value):
    if isinstance(value,str):
        type_cell = 0
    elif isinstance(value, int):
        type_cell = 1
    return type_cell

def not_zero(value, array):
    if value == 0:
        value = "empty"
    else:
        value = (value /len(array)) * 100
    return value
    
