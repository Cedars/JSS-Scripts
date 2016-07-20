#!/bin/python

import sys
import csv
import JSSLib


# This script takes in a CSV formatted in the following way:
#	username,device-serial-number
#
# The script will look up <username> and assign that user to <device-serial-number>.
# It will also set the device name to the <full_name> associated with <username>.

# Firstly, parse the CSV
with open('user_assignments.csv', 'rb') as csvfile:
	assignment_reader = csv.DictReader(csvfile, fieldnames=['username', 'serial'])
	for assignment in assignment_reader:
		# Get information about the user
		user = JSSLib.get_user_by_username(assignment['username'])
		user_id = user['id']
		user_full_name = user['full_name']
		
		# Get the JSS ID of the device
		device = JSSLib.get_mobile_device_info_by_serial(assignment['serial'])
		device_id = device['general']['id']
		
		# Here we want to set <location><username>username</username></location> on device
		print 'Assigning device %s to %s' % (assignment['serial'], user_full_name)
		JSSLib.assign_device_to_user(device_id, assignment['username'])
		
		# Rename Device to User's Full Name
		print 'Setting name of %s to %s' % (assignment['serial'], user_full_name)
		JSSLib.set_device_name(device_id, user_full_name)