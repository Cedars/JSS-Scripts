#!/bin/python
#coding: utf-8

import sys
sys.path.insert(0, '..')

import JSSLib

# Get all Users in JSS
all_users = JSSLib.get_users()

input = raw_input('%s users will be deleted. Continue [Y/N]?' % len(all_users))

if input == 'Y':
	# Delete all users
	for user in all_users:
		print 'Deleting %s' % user['name']
		JSSLib.delete_user(user['id'])