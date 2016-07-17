#!/bin/python
#coding: utf-8

import sys
sys.path.insert(0, '..')

import JSSLib
import csv

# This script takes in a CSV of user data and creates users in JSS to match.
#
# The expected format of the CSV is:
#
#	username,full-name,graduation-year,role,device-serial

# Firstly, parse the CSV
with open('limited_jss_users.csv', 'rb') as csvfile:
	user_reader = csv.DictReader(csvfile, fieldnames=['username', 'fullname', 'graduation_year', 'role', 'device_serial'])
	for user in user_reader:
		print 'Creating user %s with device %s' % (user['fullname'], user['device_serial'])
		email = '%s@cedars.inverclyde.sch.uk' % user['username']
		user_id = JSSLib.create_user(user['username'], email, user['fullname'], user['graduation_year'], user['role'])
		
		# Now assign the device to the users
		JSSLib.assign_device_to_user_by_serial(user['device_serial'], user['username'])
		JSSLib.modify_device_name_by_serial(user['device_serial'], user['fullname'])