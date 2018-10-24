import csv


def analyse(path_filename): 
    line_number = 0
    array = []
    with open(path_filename.get()) as csvfile:
        line = csv.reader(csvfile, delimiter=';')
        for row in line:
            if line_number != 0:
                array_cell = []
                for cell in row:
                    array_cell.append(cell)
                array.append(array_cell)
            line_number = line_number + 1
    array = treatment(array)
    return array


def treatment(array):
    integer = 0
    string = 0
    analysis = []
    nb_column: int = 0
    total_column = len(array[0])
    while nb_column < total_column:
        i = 0
        for line in array:
            value = analyse_cell(array[i][nb_column])
            if value == 0:
                string += 1
            elif value == 1:
                integer += 1
            i += 1
            # print(integer)
            # print(string)
        percent_string = not_zero(string, i)
        percent_integer = not_zero(integer, i)
        to_return = "string : " + str(percent_string) + "%, integer : " + str(percent_integer) + "%"
        analysis.append(to_return)
        nb_column += 1
    return analysis


# review analyse cell
def analyse_cell(value):
    print(value)
    type_cell = ""
    if isinstance(value, str):
        type_cell = 0
    elif isinstance(value, int):
        type_cell = 1
    else:
        print("not understand")
    print(type_cell)
    return type_cell


def not_zero(value, number_line):
    if value == 0:
        value = "empty"
    else:
        value = (value / number_line) * 100
    return value
