import csv
import datetime


cdr = {}

with open("cdr.csv", "r") as cdr_csv:
    rows = csv.DictReader(cdr_csv)
    for row in rows:
        #print(datetime.datetime.fromtimestamp(int(row['dateTimeOrigination'])), row['globalCallID_callId'], row['callingPartyNumber'], row['originalCalledPartyNumber'], row['finalCalledPartyNumber'], row['lastRedirectDn'], row['origDeviceName'], row['destDeviceName'])
        cdr[row['dateTimeOrigination']]={"DateTime": str(datetime.datetime.fromtimestamp(int(row['dateTimeOrigination']))), "CallingParty": row['callingPartyNumber'], "CalledParty": row['finalCalledPartyNumber'], "Duration": row['duration']}

cdr_sorted = sorted(cdr)

with open('cdrupdated.csv', 'w', newline="") as cdr_csv_updated:
    fieldnames = ['DateTime', 'CallingParty', 'CalledParty', 'Duration']
    writer = csv.DictWriter(cdr_csv_updated, fieldnames=fieldnames)
    writer.writeheader()
    for cdr_record in cdr_sorted:
        writer.writerow(cdr[cdr_record])
