#!./venv/bin/python

import sys
import xlrd

import db_table
import DataModel

bookName = sys.argv[1]

book = xlrd.open_workbook(bookName)
print("The number of worksheets is {0}".format(book.nsheets))
print("Worksheet name(s): {0}".format(book.sheet_names()))
sh = book.sheet_by_index(0)

# print("{0} {1} {2}".format(sh.name, sh.nrows, sh.ncols))
print("Cell D30 is {0}".format(sh.cell_value(rowx=29, colx=3)))

dm = DataModel.DataModel(None, None, None, None, None, None, None, None, None)
schema = {
    dm.sID: "integer",
    dm.sDATE: "date",
    dm.sSTART: "datetime",
    dm.sEND: "datetime",
    dm.sSESSION: "text",
    dm.sSESSION_TITLE: "text",
    dm.sLOCATION: "text",
    dm.sDESCRIPTION: "text",
    dm.sSPEAKERS: "text"
}

db_table = db_table.db_table("initial_table", schema)

for rx in range(15, sh.nrows):
    db_id = rx - 15
    date = str(sh.cell_value(rowx=rx, colx=0)).replace("'", "")
    start = str(sh.cell_value(rowx=rx, colx=1)).replace("'", "")
    end = str(sh.cell_value(rowx=rx, colx=2)).replace("'", "")
    session = str(sh.cell_value(rowx=rx, colx=3)).replace("'", "")
    session_title = str(sh.cell_value(rowx=rx, colx=4)).replace("'", "")
    location = str(sh.cell_value(rowx=rx, colx=5)).replace("'", "")
    description = str(sh.cell_value(rowx=rx, colx=6)).replace("'", "")
    speakers = str(sh.cell_value(rowx=rx, colx=7)).replace("'", "")

    newData = DataModel.DataModel(db_id, date, start, end, session, session_title, location, description, speakers)

    # print(sh.row(rx))
    print(newData.data)
    db_table.insert(newData.data)
    print("\n")