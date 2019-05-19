#!./venv/bin/python

import sys
import xlrd

import db_table
from DataModel import Session, Subsession, Speaker

bookName = sys.argv[1]

book = xlrd.open_workbook(bookName)
sh = book.sheet_by_index(0)

# Objects used to insert into database
session_object = Session.Session(None, None, None, None, None, None)
subsession_object = Subsession.Subsession(None, None)
speaker_object = Speaker.Speaker(None, None)

session_schema = {
    session_object.sID: "integer PRIMARY KEY",
    session_object.sDATE: "date",
    session_object.sSTART: "datetime",
    session_object.sEND: "datetime",
    session_object.sSESSION_TITLE: "text",
    session_object.sLOCATION: "text",
    session_object.sDESCRIPTION: "text",
}

subsession_schema = {
    subsession_object.sID: "integer PRIMARY KEY",
    subsession_object.sPARENT_ID: "integer",
    subsession_object.sCHILD_ID: "integer"
}

speaker_schema = {
    speaker_object.sID: "integer PRIMARY KEY",
    speaker_object.sNAME: "text",
    speaker_object.sSESSION_ID: "integer"
}

session_table = db_table.db_table("sessions", session_schema)
subsession_table = db_table.db_table("subsessions", subsession_schema)
speaker_table = db_table.db_table("speakers", speaker_schema)

# Parent id increments iff "session" == "Session"
current_parent_id = 0

for rx in range(15, sh.nrows):
    session_id = rx - 15
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
