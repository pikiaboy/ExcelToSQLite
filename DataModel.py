class DataModel:
    # Keys for the each col in the database
    sID = "id"
    sDATE = "time_start"
    sSTART = "time_start"
    sEND = "end"
    sSESSION = "session"
    sSESSION_TITLE = "title"
    sLOCATION = "location"
    sDESCRIPTION = "description"
    sSPEAKERS = "speakers"

    def __init__(self, _id, date, start, end, session, session_title, location, description, speakers):
        self.dbid = _id
        self.date = date
        self.start = start
        self.end = end
        self.session = session
        self.session_title = session_title
        self.location = location
        self.description = description
        self.speakers = speakers

    def __str__(self):
        return "id: {}\n" \
               "date: {}\n" \
               "time_start: {}\n" \
               "time_end: {}\n" \
               "session: {}\n" \
               "title: {}\n" \
               "location: {}\n" \
               "description: {}\n" \
               "speakers: {}\n".format(self.dbid, self.date, self.start, self.end, self.session, self.session_title,
                                     self.location, self.description, self.speakers)


