import csv


def analyse(path_filename): 
    line_number = 0
    array = []
    with open(path_filename) as csvfile:
        line = csv.reader(csvfile, delimiter=';')
        for row in line:
            if line_number != 0:
                array_cell = []
                for cell in row:
                    array_cell.append(cell)
                array.append(array_cell)
            line_number = line_number + 1
    array = treatment_line(array)
    return array


def treatment_line(array):
    analysis = []
    nb_column: int = 0
    total_column = len(array[0])
    while nb_column < total_column:
        i = 0
        integer = 0
        string = 0
        empty = 0
        for line in array:
            value = analyse_cell(array[i][nb_column])
            if value == 0:
                string += 1
            elif value == 1:
                integer += 1
            elif value == 2:
                empty += 1
            i += 1
        percent_string = not_zero(string, i)
        percent_integer = not_zero(integer, i)
        percent_empty = not_zero(empty, i)
        to_return = "str: {0}%, int : {1}%, empty : {2}%".format(str(percent_string), str(percent_integer),
                                                                 str(percent_empty))
        analysis.append(to_return)
        nb_column += 1
    analysis.reverse()
    return analysis


# review analyse cell
def analyse_cell(value):
    if not value:
        type_cell = 2
    elif value.isdigit():
        type_cell = 0
    else:
        type_cell = 1
    return type_cell


def not_zero(value, number_line):
    if value == 0:
        value = 0
    else:
        value = (value / number_line) * 100
    value = round(value, 2)
    return value
