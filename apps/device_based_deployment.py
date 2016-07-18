#!/bin/python
#coding: utf-8

import JSSLib

apps = JSSLib.get_apps()

user_assigned_apps = []

print 'Checking %s apps for user-assigned status' % len(apps)

for app in apps:
	print 'Checking %s' % app['name']
	app_id = app['id']
	app_info = JSSLib.get_app_info_subset(app_id, 'vpp')
	if app_info['vpp']['assign_vpp_device_based_licenses'] == False:
		user_assigned_apps.append((app_id, app['name']))
	
print '%s apps will be changed from user-based to device-based assignment:' % len(user_assigned_apps)
for app in user_assigned_apps:
	print app[1]
	

input = raw_input('Change device assignment for %s apps?' %  len(user_assigned_apps))
if input.lower() == 'y':
	for app in user_assigned_apps:
		print 'Changing status for %s' % app[1]
		try:
			JSSLib.set_device_assignment_for_app(app[0], True)
		except:
			print "WARNING: %s could not be device-assigned" % app[1]
	