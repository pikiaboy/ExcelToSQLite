class Session:
    # Keys for the each col in the database
    sID = "id"
    sDATE = "date_start"
    sSTART = "time_start"
    sEND = "time_end"
    sSESSION = "isSession"
    sSESSION_TITLE = "title"
    sLOCATION = "location"
    sDESCRIPTION = "description"
    sSPEAKERS = "speakers"

    def __init__(self,  date, start, end, session_title, location, description):
        self.data = {
            self.sDATE: date,
            self.sSTART: start,
            self.sEND: end,
            self.sSESSION_TITLE: session_title,
            self.sLOCATION: location,
            self.sDESCRIPTION: description,
        }

    def __str__(self):
        return "date: {}\n" \
               "time_start: {}\n" \
               "time_end: {}\n" \
               "title: {}\n" \
               "location: {}\n" \
               "description: {}\n".format(self.data.sDATE, self.data.sSTART, self.data.sEND, self.data.sSESSION_TITLE,
                                     self.data.sLOCATION, self.data.sDESCRIPTION)

