import JSSLib

apps = JSSLib.get_apps()

# Simply loop through all the records in the JSS
for app in apps:
    try:
        # Get the device ID then assemble the url to fetch the rest of the device record
        app_id = app['id']
        app_name = app['name'].encode('ascii', 'ignore')
        app_version = app['version']
        
        print '\"%s\",%s' % (app_name, app_version)

    except Exception as e:
        print(e)

