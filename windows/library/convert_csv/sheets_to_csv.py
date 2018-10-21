from openpyxl import load_workbook
import csv
from os import listdir
from re import search, sub
import sys


#convert
def from_xslx(file, csv_filename):
    wb = load_workbook(filename=file, read_only=True)
    sh = wb.active
    csv_file = open(csv_filename, 'w')
    wr = csv.writer(csv_file, delimiter=';')
    for row in sh.rows:
        liste= []
        for cell in row:     
            liste.append(cell.value)
        wr.writerow(liste)
    csv_file.close()

def from_ods(file, csv_filename):
    # to code
    print("test")

#explore dir
def explore_dir(path):
    liste = os.listdir(path)
    if __name__ == "__main__":
        for file in liste:
            if re.search("xlsx", file): 
                print(file)
    return liste

#treatment
def treatement(files_list):
    for file in liste:
        if re.search("xlsx", file):
            newname = re.sub('xlsx', 'csv', file)
            from_xlsx(file, newname)
        elif re.search("ods", file):
            newname = re.sub('ods', 'csv', file)
            from_ods(newname)
        elif re.search("xls". file):
            newname = re.sub('xls', 'csv', file)
            from_xls(newname)

def from_ods(file, csv_filename):
    # to code
    print("test")
