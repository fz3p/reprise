import csv
import sys
from re import search, sub

def header(path_filename):
    # print("load header_to_csv")
    # print(path_filename.get())

    # just first line 
    line_number= 0
    diese = "# "
    array = []
    array_first = []
    array_two = []
    with open(path_filename.get()) as csvfile:
        line = csv.reader(csvfile, delimiter=';')
        for row in line:
            column_number = 0
            if line_number == 0:
                for cell in row:
                    array_first.append(diese + alphabet_letter(column_number) + " = " + str(column_number) + " - " + cell)
                    column_number = column_number + 1
            elif line_number == 1:
                for cell in row:
                    array_two.append(cell)
                    column_number = column_number + 1
            line_number = line_number + 1
    array = [array_first, array_two]

    if __name__ == "__main__":
        print(array)

    return array


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
    
    i = 1
    number_cell_in_line = len(array)
    integer = 0
    string = 0

    # for one column
    while i < len(array):
        value = analyse_cell(array[1][i])
        i += 1
        if value == 0:
            string += 1
        elif value == 1: 
            integer += 1
    percent_string = (string / len(array))*100
    percent_integer= (integer / len(array))*100
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

def alphabet_letter(number):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if number < 25:
        return alphabet[number].upper()
    elif number > 25:
        first_letter = alphabet[round(number/25 - 1)]
        second_letter = alphabet[number%25]
        return str(first_letter).upper()+str(second_letter).upper()
    else:
        text = "wrong data"
        return text



