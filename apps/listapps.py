#!/bin/python
#coding: utf-8

import sys
sys.path.insert(0, '..')
import JSSLib

all_apps = JSSLib.get_apps()
for app in all_apps:
	app_info=JSSLib.get_app_info(app['id'])
	manage_unmanaged = app_info['general']['take_over_management']
	print '%s : %s' % (manage_unmanaged, app['name'])
	if manage_unmanaged == 'True':
		print 'Changing management takeover state on %s' % app['name']
#		JSSLib.set_take_over_management(app['id'], 'false')
	else:
		print 'NOT Changing management takeover state on %s' % app['name']