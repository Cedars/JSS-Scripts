#coding: utf-8
import json
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Quieten down insecure request warnings due to unverified SSL
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

######################################################
#mark Settings
######################################################

# This function should return https://my.jss.com:8443/JSSResource 
# The base URL for JSS API interactions
def jssURL():
	url = os.environ.get('JSS_URL')
	if url == None:
		print 'Please define $MDM_URL or override jssURL()'
	else:
		return url

def jssUser():
	user = os.environ.get('MDM_USER')
	if user == None:
		user = 'mdmadmin'
	return user

def jssPassword():
	password = os.environ.get('MDM_PASSWORD')
	if password == None:
		print 'Please define $MDM_PASSWORD or override jssPassword()'
	else:
		return password

def verifySSL():
	return False
	
	
######################################################
#mark JSS Primitives
######################################################
def jsonHeaders():
	requestHeaders = {
		'Content-Type': 'application/json',
		'Accept': 'application/json',
	}
	return requestHeaders

def xmlHeaders():
	requestHeaders = {
		'Content-Type': 'application/xml',
		'Accept': 'application/json',
	}
	return requestHeaders

def runGetCommand(cmd, result_key):
	try:
		result = json.loads(requests.get('%s/%s' % (jssURL(), cmd), headers=jsonHeaders(), verify=verifySSL(), auth=(jssUser(), jssPassword())).text)
		return result[result_key]
	except Exception as e:
		print(e)
		sys.exit(0)

# command_url should be the command after the DNS name, omitting leading /
def runPostCommand(command_url, command_data = None):
	request = requests.post('%s/%s' % (jssURL(), command_url), data=command_data, headers=xmlHeaders(), verify=verifySSL(), auth=(jssUser(), jssPassword()))

	if request.status_code == 201:
		return request.status_code
	else:
		raise Exception(
			request.text
		)

def runPutCommand(command_url, command_data):
	request = requests.put('%s/%s' % (jssURL(), command_url), data=command_data, headers=xmlHeaders(), verify=verifySSL(), auth=(jssUser(), jssPassword()))
	if request.status_code == 201:
		return request.status_code
	else:
		raise Exception(
			request.text
		)

def runDeleteCommand(command_url):
	request = requests.delete('%s/%s' % (jssURL(), command_url),  headers=xmlHeaders(), verify=verifySSL(), auth=(jssUser(), jssPassword()))
	if request.status_code == 200:
		return request.status_code
	else:
		raise Exception(
			request.text
		)
	
######################################################
#mark Mobile Devices
######################################################
# Returns a list of all mobile devices in the JSS
def get_mobile_devices():
	return runGetCommand("mobiledevices", "mobile_devices")

# Returns info for a mobile device given a JSS ID
def mobile_device_info(device_id):
	return runGetCommand('mobiledevices/id/%s' % device_id, 'mobile_device')

# Returns info for a mobile device given a Serial Number
def get_mobile_device_info_by_serial(serial):
	return runGetCommand('mobiledevices/serialnumber/%s' % serial, 'mobile_device')

# Modifies the name of the a mobile device given a JSS ID and new name
def set_device_name(device_id, new_name):
	deviceNameURL = 'mobiledevicecommands/command/DeviceName/%s/id/%s' % (new_name, device_id)
	runPostCommand(deviceNameURL)

def modify_device_name_by_serial(device_serial, new_name):
	device_info = get_mobile_device_info_by_serial(device_serial)
	set_device_name(device_info['general']['id'], new_name)

# Assigns a device to a user given a JSS ID for the device and a username
def assign_device_to_user(device_id, username):
	username_xml = '<mobile_device><location><username>%s</username></location></mobile_device>' % username
	runPutCommand('mobiledevices/id/%s' % device_id, username_xml)

def assign_device_to_user_by_serial(device_serial, username):
	device_info = get_mobile_device_info_by_serial(device_serial)
	assign_device_to_user(device_info['general']['id'], username)

def get_device_storage_used_percentage(device_id):
	device_info = mobile_device_info(device_id)
	return device_info['general']['percentage_used']

def get_device_capacity(device_id):
	device_info = mobile_device_info(device_id)
	return device_info['general']['capacity']

def get_device_assigned_user(device_id):
	device_info = mobile_device_info(device_id)
	return device_info['location']['username']
	
######################################################
#mark JSS Users
######################################################
# Returns a list of all users in the JSS
def get_users():
	return runGetCommand('users', 'users')

# Returns a user by username
def get_user_by_username(username):
	userURL = 'users/name/%s' % username
	return runGetCommand(userURL, 'user')

# Returns a user's extension attributes as a dictionary of {name, value}
def get_user_extension_attributes(user_id):
	userURL = 'users/id/%s' % user_id
	user = runGetCommand(userURL, 'user')
	eas = user['extension_attributes']
	dictionary_atts = {}
	for e in eas:
		dictionary_atts[e['name']] = e['value']
	return dictionary_atts

# Delete User by ID
def delete_user(user_id):
	userDeleteURL = 'users/id/%s' % user_id
	runDeleteCommand(userDeleteURL)

# Create User
def create_user(username, email, fullname, graduation_year, role):
	userCommand = 'users/id/0'
	extensionAttributesXML = '<user><name>%s</name><email>%s</email><full_name>%s</full_name><extension_attributes><attribute><name>Graduation Year</name><value>%s</value></attribute><attribute><name>Role</name><value>%s</value></attribute></extension_attributes></user>' % (username, email, fullname, graduation_year, role)
	return runPostCommand(userCommand, extensionAttributesXML)
	
######################################################
#mark Mobile Apps
######################################################
def get_apps():
	return runGetCommand('mobiledeviceapplications', 'mobile_device_applications')

def get_app_info(app_id):
	return runGetCommand('mobiledeviceapplications/id/%s' % app_id, 'mobile_device_application')

def set_take_over_management(app_id, state):
	command = 'mobiledeviceapplications/id/%s' % app_id
	data = '<mobile_device_application><general><take_over_management>%s</take_over_management></general></mobile_device_application>'
	return runPutCommand(command, data)