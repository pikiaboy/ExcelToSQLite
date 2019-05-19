#!./venv/bin/python

import sys
import pprint

import db_table

col = sys.argv[1].split(",")
val = sys.argv[2].split(",")


searchParms = {}

for i in range(len(val)):
    searchParms[col[i]] = val[i]

session_table = db_table.db_table("sessions")
subsession_table = db_table.db_table("subsessions")
speaker_table = db_table.db_table("speakers")

# Find each session_id for the searched on column
results = []
if "speaker" in col:
    speakers = speaker_table.select(None, searchParms)
    for i in range(len(speakers)):
        session = session_table.select(None, {"session_id": speakers[i]['session_id']})[0]
        results.append(session)
else:
    results = session_table.select(None, searchParms)


# For each session id, check to see if it has any subsessions
for i in range(len(results)):
    result = results[i]
    session_id = result['session_id']

    subsessions = subsession_table.select(None, {"parent_id": session_id})
    newResults = []
    for j in range(len(subsessions)):
        newResults.append(session_table.select(None, {"session_id": subsessions[j]['child_id']}))

    print("Parent Session:")
    pprint.pprint (result)
    if len(newResults) != 0:
        print("\nChild sessions")
        pprint.pprint(newResults)

    print("=========================================")




