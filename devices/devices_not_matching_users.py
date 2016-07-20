#!/bin/python

import JSSLib

# Get all devices
devices = JSSLib.get_mobile_devices()

for device in devices:
	device_name = device['name']
	user_name = device['username']
	
	if user_name == '':
		print 'Device id %s is not assigned to a user.' % device['id']
		continue
	
	
	full_name = JSSLib.get_user_by_username(user_name)['full_name']
	
	if device['name'] != full_name:
		print 'Device %s does not match user %s (%s).' % (device_name, full_name, device['id'])