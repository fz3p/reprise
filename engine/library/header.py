import csv


def header(path_filename):
    line_number = 0
    diese = "# "
    array = []
    array_first = []
    array_two = []
    with open(path_filename) as csvfile:
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



