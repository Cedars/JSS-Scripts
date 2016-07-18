#!/bin/python
#coding: utf-8

import sys
sys.path.insert(0, '../lib')

import JSSLib

users = JSSLib.get_users()
users = sorted(users, key=lambda u: u['name'])
for u in users:
	print '%s (%s)' % (u['name'], u['id'])
