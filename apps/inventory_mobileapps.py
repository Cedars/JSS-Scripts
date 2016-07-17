##
# This is used to update device names to be the same as the username assigned to the device
#
# You can run this by typing the following:
#       python update_devicename.py
#
# If you have any issues, please submit an issue on this GitHub Repo and
# I can try to help you at the next chance I get.
#
# Set the URL, Username and Password where stated below.
# They currently have placeholders in there, just replace them with your information
#
# For this script, the user you enter must have the following permissions:
#   - Mobile Devices
#       - Read
#       - Write
##

import requests, sys, json, urllib

# Set this to False if you have any errors
verifySSL = False

# Set this so it only goes through one device for testing
debug = True
debug_username = 'ls'

# Set JSS Variables here
# JSS URL must end with / like so:
# https://jss.example.com:8443/
jssURL = 'https://mdm.cedars.inverclyde.sch.uk:8443/'
jssAPIUsername = 'mdmadmin'
jssAPIPassword = 'k32-ZKg-MDa-AkX'

# I have my own JSS Module for easy code publishing
try:
    from vcpmodule import credentials as jssCred
    credentials_loaded = jssCred.isLoaded()
    creds = jssCred.getJSS()
    jssURL = creds.url
    jssAPIUsername = creds.username
    jssAPIPassword = creds.password
except:
    credentials_loaded = False

##                              ##
# DO NOT CHANGE ANY OF THE BELOW #
##                              ##

error_reached = False

jssAPIURL = jssURL + "JSSResource"

requestHeaders = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}

try:
    result = json.loads(requests.get('%s/mobiledeviceapplications' % jssAPIURL, headers=requestHeaders, verify=verifySSL, auth=(jssAPIUsername, jssAPIPassword)).text)
    apps = result['mobile_device_applications']
except Exception as e:
    print(e)
    sys.exit(0)

# Simply loop through all the records in the JSS
for app in apps:
    try:
        # Get the device ID then assemble the url to fetch the rest of the device record
        app_id = app['id']
        app_name = app['name'].encode('ascii', 'ignore')
        app_version = app['version']
        
        print '\"%s\",%s' % (app_name, app_version)

    except Exception as e:
        error_reached = True
        print(e)

if error_reached:
    print('Error renaming devices')
else:
    print('Finished renaming devices')
