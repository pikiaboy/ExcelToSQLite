#!/usr/bin/python

import sys
import xlrd

import db_table
import DataModel



bookName = sys.argv[1]

book = xlrd.open_workbook(bookName)
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)
print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))

for rx in range(15, sh.nrows):
    db_id = rx - 15
    date = sh.cell(rx, 0)
    start = sh.cell(rx, 1)
    end = sh.cell(rx, 2)
    session = sh.cell(rx, 3)
    session_title = sh.cell(rx, 4)
    location = sh.cell(rx, 5)
    description = sh.cell(rx, 6)
    speakers = sh.cell(rx, 7)

    newData = DataModel.DataModel(db_id, date, start, end, session, session_title, location, description, speakers)

    # print(sh.row(rx))
    print(newData)
    print("\n")



