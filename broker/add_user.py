#!/usr/bin/python

import database
import json
import sys

def handle_list(arg):
    if arg:
        return arg.split(",")
    else:
        return []

if len(sys.argv) < 5:
    print >> sys.stderr, "Usage: %s <ident> <secret> <publish> <subscribe>"%sys.argv[0]
    sys.exit(1)

ident = sys.argv[1]
secret = sys.argv[2]
publish = handle_list(sys.argv[3])
subscribe = handle_list(sys.argv[4])

#insert into authkeys (ident, secret, pubchans, subchans)
data = (ident, secret, json.dumps(publish), json.dumps(subscribe))

db = database.Database()
done = db.add_user(data)

if done:
    print "Inserted successfull!"
else:
    print "Error"
