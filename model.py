import json
from datetime import datetime


GUESTBOOK_ENTRIES_FILE = "entries.json"
entries = []
next_id=0

def init():
    global entries,next_id
    try:
        f = open(GUESTBOOK_ENTRIES_FILE)
        entries = json.loads(f.read())
        for i in range(len(entries)):
            entries[i]['id']=i
        next_id+=len(entries)
        f.close()
    except:
        print('Couldn\'t open', GUESTBOOK_ENTRIES_FILE)
        entries = []

def get_entries():
    global entries
    return entries


def delete_entry(the_id):
    global entries, GUESTBOOK_ENTRIES_FILE
    for e in entries:
        if str(e['id']) == str(the_id):
            entries.remove(e)
            break
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


def add_entry(name, text):
    global entries, GUESTBOOK_ENTRIES_FILE,next_id
    now = datetime.now()
    time_string = now.strftime("%b %d, %Y %-I:%M %p")
    entry = {"author": name, "text": text, "timestamp": time_string}
    entries.insert(0, entry) ## add to front of list
    entries[0]['id']=next_id
    next_id+=1
    try:
        f = open(GUESTBOOK_ENTRIES_FILE, "w")
        dump_string = json.dumps(entries)
        f.write(dump_string)
        f.close()
    except:
        print("ERROR! Could not write entries to file.")


