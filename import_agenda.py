#!./venv/bin/python

import sys
import xlrd

import db_table
from DataModel import Session, Subsession, Speaker

bookName = sys.argv[1]

book = xlrd.open_workbook(bookName)
sh = book.sheet_by_index(0)

# Tables that we are creating for the SQLite DB
session_table = db_table.db_table("sessions")
subsession_table = db_table.db_table("subsessions")
speaker_table = db_table.db_table("speakers")

# Parent id increments iff "session" == "Session"
current_parent_id = 0

for rx in range(15, sh.nrows):
    session_id = rx - 14
    date = str(sh.cell_value(rowx=rx, colx=0)).replace("'", "")
    start = str(sh.cell_value(rowx=rx, colx=1)).replace("'", "")
    end = str(sh.cell_value(rowx=rx, colx=2)).replace("'", "")
    session = str(sh.cell_value(rowx=rx, colx=3)).replace("'", "")
    session_title = str(sh.cell_value(rowx=rx, colx=4)).replace("'", "")
    location = str(sh.cell_value(rowx=rx, colx=5)).replace("'", "")
    description = str(sh.cell_value(rowx=rx, colx=6)).replace("'", "")
    speakers = str(sh.cell_value(rowx=rx, colx=7)).replace("'", "")

    # Parse Speakers into individual speakers and insert into table
    if speakers != "":
        speakers = speakers.split("; ")
        for speaker in speakers:
            speaker_object = Speaker.Speaker(speaker, session_id)
            speaker_table.insert(speaker_object.data)

    if session == "Session":
        session_object = Session.Session(date, start, end, session_title, location, description)
        session_table.insert(session_object.data)
        current_parent_id = session_id
    elif session == "Sub":
        session_object = Session.Session(date, start, end, session_title, location, description)
        subsession_object = Subsession.Subsession(current_parent_id, session_id)
        session_table.insert(session_object.data)
        subsession_table.insert(subsession_object.data)
