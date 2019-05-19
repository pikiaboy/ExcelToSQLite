class Subsession:
    sPARENT_ID = "parent_id"
    sCHILD_ID = "child_id"

    def __init__(self, parent_id, child_id):
        self.data = {
            self.sPARENT_ID: parent_id,
            self.sCHILD_ID: child_id
        }