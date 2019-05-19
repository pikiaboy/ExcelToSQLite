class Speaker:
    sNAME = "speaker" # Name of the speaker
    sSESSION_ID = "session_id" # Session id that the speaker is talking at

    def __init__(self, name, session_id):
        self.data = {
            self.sNAME: name,
            self.sSESSION_ID: session_id
        }