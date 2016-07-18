#!/bin/python
#coding: utf-8

import JSSLib

groups = JSSLib.get_device_groups()

input = raw_input('%s groups will be deleted. Continue? [Y/n]' % len(groups))

if input == 'Y':
	for g in groups:
		print 'Deleting %s' % group['name']
		JSSLib.delete_device_group(g['id'])
