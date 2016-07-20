#!/bin/python
#coding: utf-8

import sys
import JSSLib

#
# This script prints a sorted list of all the user objects in your JSS
# and their internal JSS ID.
#

users = JSSLib.get_users()
users = sorted(users, key=lambda u: u['name'])
for u in users:
	print '%s (%s)' % (u['name'], u['id'])
