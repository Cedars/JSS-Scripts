#!/bin/python

import sys
import JSSLib
from time import sleep

# Get all devices in JSS
devices = JSSLib.get_mobile_devices()

stats = {}

print 'Getting storage stats for %s devices.' % len(devices)

progress=0.0
each_device = len(devices)/100.0

for d in devices:
	sys.stdout.write('\r')
	percent_used = JSSLib.get_device_storage_used_percentage(d['id'])
	user_name = JSSLib.get_device_assigned_user(d['id'])
	
	if user_name == '':
		continue
	
	user_id = JSSLib.get_user_by_username(user_name)['id']
	graduation_year = JSSLib.get_user_extension_attributes(user_id)['Graduation Year']
	
	if not graduation_year in stats.keys():
		stats[graduation_year] = (0,0)
	
	percent = stats[graduation_year][0] + percent_used
	denominator = stats[graduation_year][1] + 1
	
	stats[graduation_year] = (percent, denominator)

	progress += each_device
	sys.stdout.write("Device %s - %d%%" % (d['id'], progress))
	sys.stdout.flush()
	sleep(0.25)

# Compute stats
overall_percent = 0
total_denominators = 0

for year in sorted(stats.keys()):
	percent = stats[year][0]
	overall_percent += percent
	denominator = stats[year][1]
	total_denominators += denominator
	average = percent / denominator
	
	print 'Average storage for Class of %s is %s%%.' % (year, average)

final = overall_percent / total_denominators
print 'Overall average storage is %s%%.' % final