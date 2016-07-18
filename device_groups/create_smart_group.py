#!/bin/python
#coding: utf-8

import JSSLib

# Devices Circumventing Restrictions
c1 = {'name' : 'Location Services for Self Service Mobile',
      'and_or' : 'or',
      'search_type' : 'is',
      'value' : 'Not Enabled/Unknown'}

c2 = {'name' : 'Jailbreak Detected',
      'and_or' : 'or',
      'search_type' : 'is',
      'value' : 'Yes'}

c3 = {'name' : 'Last Inventory Update',
      'and_or' : 'or',
      'search_type' : 'more than x days ago',
      'value' : 3}

criteria = [c1, c2, c3]

JSSLib.create_smart_device_group('CP - Devices Circumventing Restrictions', criteria)
