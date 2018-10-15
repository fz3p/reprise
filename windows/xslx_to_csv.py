from openpyxl import load_workbook
import csv
import os
import re
import sys


def csv_from_excel(file, your_csv_file_name):
    wb = load_workbook(filename=file, read_only=True)
    sh = wb.active
    your_csv_file = open(your_csv_file_name, 'w')
    wr = csv.writer(your_csv_file, delimiter=';')
    for row in sh.rows:
        liste= []
        for cell in row:     
            liste.append(cell.value)
        wr.writerow(liste)
    your_csv_file.close()


liste = os.listdir('.')
print('liste des fichiers')
for file in liste:
    if re.search("xlsx", file): 
        print(file)

print("début du traitement des fichiers")
for file in liste:
    if re.search("xlsx", file):
        print(file)
        newname = re.sub('xlsx', 'csv', file)
        print(newname)
        csv_from_excel(file, newname)
