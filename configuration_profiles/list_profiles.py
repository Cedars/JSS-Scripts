#!/bin/python

import JSSLib

profiles = sorted(JSSLib.get_configuration_profiles(), key=lambda p:p['name'])
for profile in profiles:
	print profile['name']
