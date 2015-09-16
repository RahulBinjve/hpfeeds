#!/usr/bin/python

import sys
import database
import pprint

db_object = database.Database()
data = db_object.get_users()

pprint.pprint(data)
