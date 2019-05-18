class DataModel:
    # Keys for the each col in the database
    sID = "id"
    sDATE = "date_start"
    sSTART = "time_start"
    sEND = "time_end"
    sSESSION = "session"
    sSESSION_TITLE = "title"
    sLOCATION = "location"
    sDESCRIPTION = "description"
    sSPEAKERS = "speakers"

    def __init__(self, _id, date, start, end, session, session_title, location, description, speakers):
        self.data = {
            self.sID: _id,
            self.sDATE: date,
            self.sSTART: start,
            self.sEND: end,
            self.sSESSION: session,
            self.sSESSION_TITLE: session_title,
            self.sLOCATION: location,
            self.sDESCRIPTION: description,
            self.sSPEAKERS: speakers
        }




    def __str__(self):
        return "id: {}\n" \
               "date: {}\n" \
               "time_start: {}\n" \
               "time_end: {}\n" \
               "session: {}\n" \
               "title: {}\n" \
               "location: {}\n" \
               "description: {}\n" \
               "speakers: {}\n".format(self.data.sID, self.data.sDATE, self.data.sSTART, self.data.sEND, self.data.sSESSION, self.data.sSESSION_TITLE,
                                     self.data.sLOCATION, self.data.sDESCRIPTION, self.data.sSPEAKERS)


