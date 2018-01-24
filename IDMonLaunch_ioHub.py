# Took this script out of the main python script as it was getting cumbersome inside of psychopy builder

print "inside IDMonLaunch_ioHub.py"

# DETERMINE SCREEN WIDTH AND SIZE HERE
# DISABLE THIS EVENTUALLY IT DOESN'T WORK
#from sys import platform as _platform
#if _platform == "linux" or _platform == "linux2":
   # linux
#    print "linux!"
#elif _platform == "darwin":
   # MAC OS X
#    import AppKit
#    tmp=[(screen.frame().size.width, screen.frame().size.height) for screen in AppKit.NSScreen.screens()]
#    System_mon_width = tmp[0][0]
#    System_mon_height = tmp[0][1]
#    print "mac OS darwin detected"
#elif _platform == "win32":
#    from win32api import GetSystemMetrics
#    System_mon_width = GetSystemMetrics(0)
#    System_mon_height = GetSystemMetrics(1)
#    print "windows platform detected"
   # Windows
#print "System determined monitor Width =", System_mon_width
#print "System determined monitor height =", System_mon_height

#
# SYSTEM MONITOR SIZE BETTER TO CUSTOM MAKE IT FOR EACH CONFIGURATION
#
#It appears on my home PC that the mouse pixel location is 33x pixels per degree
#we'll make the fp windows 1.5 degrees error


import socket

if socket.gethostname() in ('LinerW10'):
    # I had to hard code this because 2nd monitor resolution wasn't able to be grabbed easily
    screen_width = 2560
    screen_height = 1440 #overlord monitor v pix
    print "Eye Tracker off at home W10"
    
    #
    # DETERMINE HERE IF WIN10 MACHINE AT HOME WILL USE IOHUBCONNECTION(EYETRACKER = TRUE) OR IOHUBSERVER(EYETRACKER = FALSE)
    #
    eyetracker=True # no trackder at home - but if True seems to run okay (doesn't crash but mouse is not recognized yet)

    if eyetracker == False:
        mxydiv_factor = 33 #mouse pixel units/degree
    else:
        mxydiv_factor = 1 #mouse pixel units/degree
    moe = 1 # mouse at home
    
    useRetinaBool = False
    print "LinerW10 PC: Eyetracker = " + str(eyetracker) + " moe = " + str(moe)
    psychopy_mon_name ='default'
    displayDevice = 0 #1 to display and calibrate eye position 2nd monitor. Keep at 0 to to display on primary monitor
    #
    # This configuration is for MacBookPros
    # 
elif 'Liner' in socket.gethostname()\
    or 'Alexanders' in socket.gethostname()\
    or 'Amalias' in socket.gethostname()\
    or 'Aryas-Macbook' in socket.gethostname()\
    or 'Kirsties' in socket.gethostname(): # Linus's Laptop
    mxydiv_factor = 25 #pixels/degree (good for home and mac laptop)
    # I had to hard code this because 2nd monitor resolution wasn't able to be grabbed easily
    screen_width = 2560
    screen_height = 1600 # vpix for MBP 13"
    eyetracker = False # no tracker attached to MBP, if it is True, iohub freezes the process and window never displays and this will cause iohubLaunchServer to run
    moe = 1 # mouse only for laptop
    useRetinaBool = True
    expInfo['Eye Tracker'] = 'NoEyeTracker_iohub_MBP.yaml'
    print "expInfo:"
    print expInfo
    psychopy_mon_name='PGLR' # unclear if this is necessary to use the monitor center
    print "MBP: Eyetracker = " + str(eyetracker) + " moe = " + str(moe)
    displayDevice = 0 #1 to display and calibrate eye position 2nd monitor. Keep at 0 to to display on primary monitor
elif 'HL8BRQT' in socket.gethostname()\
    or 'SurfacePro' in socket.gethostname(): # ZIkangs
    mxydiv_factor = 33 #pixels/degree (good for home and mac laptop)
    # I had to hard code this because 2nd monitor resolution wasn't able to be grabbed easily
    screen_width = 1366
    screen_height = 768 # vpix for MBP 13"
    eyetracker = False # no tracker attached to MBP
    moe = 1 # mouse only for laptop
    useRetinaBool = False
    psychopy_mon_name='PGL' # set up in Ryu's and Zikang's laptop
    print "Ryu: Eyetracker = " + str(eyetracker) + " moe = " + str(moe)
    displayDevice = 0 #1 to display and calibrate eye position 2nd monitor. Keep at 0 to to display on primary monitor
elif socket.gethostname() in ('latoya-palmers-imac.local'):
    mxydiv_factor = 25 #pixels/degree (good for home and mac laptop)
    # I had to hard code this because 2nd monitor resolution wasn't able to be grabbed easily
    screen_width = 1680
    screen_height = 1050
    psychopy_mon_name='iMac'
    useRetinaBool = False
    moe = 2
    eyetracker = True # yes there is an eye link attached to iMac
    displayDevice = 0 #1 to display and calibrate eye position 2nd monitor. Keep at 0 to to display on primary monitor
elif socket.gethostname() in ('PsyPyHuman'): # This was for Win10 on Mac machine 
    mxydiv_factor = 17.42 #mouse pixel units/degree
    # Gui to decide which monitor you want to do expt
    guititle = 'Which monitor for display? (1-primary) (2-secondary)?'  # from the Builder filename that created this script
    #guichoice = {'Win_tolerance':'3','Calibrate(Y/N)': 'N','Monitor(1/2)': '2','(2)EyeTracker/(1)Mouse?':'2'}
    guichoice = {'Calibrate(Y/N)': 'N','Monitor(1/2)': '2','(2)EyeTracker/(1)Mouse?':'2'}
    dlg = gui.DlgFromDict(dictionary=guichoice, title=guititle)
    if dlg.OK == False: core.quit()  # user pressed cancel
    # I had to hard code this because 2nd monitor resolution wasn't able to be grabbed easily
    #fpwin_all = guichoice['Win_tolerance']
    if guichoice['Monitor(1/2)'] == '1':
        screen_width = 2560
        screen_height = 1440
        psychopy_mon_name='BenQ'
        displayDevice = 0 #1 to display and calibrate eye position 2nd monitor. Keep at 0 to to display on primary monitor
    elif guichoice['Monitor(1/2)'] == '2':
        screen_width = 1024
        screen_height = 768
        psychopy_mon_name='testMonitor'
        displayDevice = 1 #1 to display and calibrate eye position 2nd monitor. Keep at 0 to to display on primary monitor
    if guichoice['(2)EyeTracker/(1)Mouse?'] == '1':
        moe = 1
    elif guichoice['(2)EyeTracker/(1)Mouse?'] == '2':
        moe = 2
else: # default computer screens
    mxydiv_factor = 33 #pixels/degree (good for home and mac laptop)
    # I had to hard code this because 2nd monitor resolution wasn't able to be grabbed easily
    screen_width = 1024
    screen_height = 768
    eyetracker = False # default no tracker
    useRetinaBool = False
    psychopy_mon_name='testMonitor'
    moe = 1 # default mouse
    displayDevice = 0 #1 to display and calibrate eye position 2nd monitor. Keep at 0 to to display on primary monitor


print "Custom Code determined python app display monitor Width =", screen_width
print "Custom Code determined python app display monitor height =", screen_height

# this will always run by default
if expInfo['Eye Tracker']:
    try:
        from psychopy.iohub import EventConstants,ioHubConnection,load,Loader
        from psychopy.iohub.util import NumPyRingBuffer
        from psychopy.data import getDateStr
        # Load the specified iohub configuration file converting it to a python dict.
        io_config=load(file(expInfo['Eye Tracker'],'r'), Loader=Loader)
        print "io_config here: "
        #print io_config
        # Add / Update the session code to be unique. Here we use the psychopy getDateStr() function for session code generation
        session_info=io_config.get('data_store').get('session_info')
        #print 'session_info: ' + str(session_info)
        session_info.update(code="S_%s"%(getDateStr()))
        print 'new sessioninfo:' 
        print session_info
        print 'here'
        print 'old filename:  '
        print io_config.get('data_store')
        print 'neither there'
        io_config['data_store']['filename'] = u'data' + os.sep + "S_%s"%(getDateStr())
    
        #print 'session_info:'
        #print session_info
        print 'eyetracker:' + str(eyetracker)
    
        sys.stdout.flush()
        
        # Create an ioHubConnection instance, which starts the ioHubProcess, and informs it of the requested devices and their configurations.
        if eyetracker == True:
            io=ioHubConnection(io_config)
            # mouse unit reports for position totally different if called by launchHubServer(need div myxypixperdegree) and ioHubConnection
        else:
            from psychopy.iohub import launchHubServer
            print "EXECUTING REDUCED io=launchHubServer instead of ioHubConnection because no eye tracker"
            # trouble with loading io_config tracker info in it. so load limited tracker
            sess_code='S_{0}'.format(long(time.mktime(time.localtime())))
            exp_code='data' + os.sep + sess_code
            #exp_code will be the file name for data
            print 'Current Session Code will be: ', sess_code    
            io=launchHubServer(psychopy_monitor_name=psychopy_mon_name, experiment_code=exp_code, session_code=sess_code)


        # access the iohub devices of the keyboard and mouse inputs
        iokeyboard=io.devices.keyboard
        # mouse unit reports for position totally different if called by launchHubServer(need div myxypixperdegree) and ioHubConnection (do not)
        # acutally the myxypixperdegree does need to be divided, perhaps it is an issue with the monitor center and reporting pix vs degrees.
        mouse=io.devices.mouse
        #if moe == 1:
        #    # if using mouse with ioHubConnection rather than older launchHubServer function, then don't divide
        #    mxydiv_factor = 1
        
        if (eyetracker==True) and io.getDevice('tracker'):
            eyetracker=io.getDevice('tracker')
            eyetracker.runSetupProcedure()

    except Exception, e:
       import sys
       print "!! Error starting ioHub: ",e," Exiting..."
       sys.exit(1)

    display_gaze=True
    x,y=0,0

#hack to eliminate strange divide factor
#mxydiv_factor = 1

# Start the ioHub process. The return variable is what is used
# during the experiment to control the iohub process itself,
# as well as any running iohub devices.
#io=launchHubServer()
#io=launchHubServer(psychopy_monitor_name=psychopy_mon_name, experiment_code=exp_code, session_code=sess_code)

#display = io.devices.display

#from pprint import pprint
#pprint(vars(display))

# print(the display's physical characteristics, showing they have
# been updated based on the settings in the PsychoPy monitor config.
#print('Display Psychopy displaycount: ', display.getDisplayCount())
#print('Display Psychopy device number: ', display.getDeviceNumber())
#print('Display Psychopy Monitor Name: ', display.getPsychopyMonitorName())
#print('Display Default Eye Distance: ', display.getDefaultEyeDistance())
#print('Display Physical Dimensions: ', display.getPhysicalDimensions())
#print('Display Physical pixels per degree: ', display.getPixelsPerDegree())

#pixperdegree = display.getPixelsPerDegree()
#HACK I know it's 17.42 for psychopy upstairs on 8th
pixperdegree = 17.24



# By default, ioHub will create Keyboard and Mouse devices and
# start monitoring for any events from these devices only.
#keyboard=io.devices.keyboard
#mouse=io.devices.mouse



if moe == 200: # this may be deprecated for eyelink
    # ---------------------------------------------
    #---- connect to iView
    # ---------------------------------------------
    from iViewXAPI import  *               #iViewX library
    import PIL

    res = iViewXAPI.iV_SetLogger(c_int(1), c_char_p("iViewXSDK_Python_GazeContingent_Demo.txt"))
    print res

    #OLD tracker ip address?
    #res=iViewXAPI.iv_Connect(c_char_p('169.254.20.13'),c_int(4444), c_char_p('169.254.34.44'),c_int(5555))

    res = iViewXAPI.iV_Connect(c_char_p('169.254.20.13'), c_int(4444), c_char_p('169.254.20.100'), c_int(5555))
    #set 20.10 to port 5555 8/2015

    print res
    if res == 100:
        print 'failed to establish connection'

    #print dir(iViewXAPI)

    res = iViewXAPI.iV_GetSystemInfo(byref(systemData))
    print "iV_GetSystemInfo: " + str(res)
    print "Samplerate: " + str(systemData.samplerate)
    print "iViewX Version: " + str(systemData.iV_MajorVersion) + "." + str(systemData.iV_MinorVersion) + "." + str(systemData.iV_Buildnumber)
    print "iViewX API Version: " + str(systemData.API_MajorVersion) + "." + str(systemData.API_MinorVersion) + "." + str(systemData.API_Buildnumber)

    # ---------------------------------------------
    #---- configure and start calibration
    # ---------------------------------------------
    # the second monitor needs displayDevice = 1
    # on Windows 7 Mac upstairs 8th floor set this to 0 and mirror screen in Windows7
    # OR SET displayDevice = 1 which allows calibration to occur on the dual monitor (CRT)
    #calibrationData = CCalibration(5, 1, displayDevice, 0, 1, 20, 239, 1, 10, b"")
    #calibrationData = CCalibration(13, 1, displayDevice, 0, 1, 20, 239, 1, 10, b"")
    calibrationData = CCalibration(13, 1, displayDevice, 0, 1, 239, 20, 1, 10, b"")
    # 13 points calibration instead of 5 is much more accurate

    #CalibrationStruct Datafields: 
    #method (5 or 13)
    #visualization (0:viz by ext stim program 1: viz by SDK (default)
    #displayDevice (set Display Device [0: primary device (default), 1: secondary device]
    #speed: set Calibration/Validation speed [0: slow (default), 1: fast]
    #autoAccept: set Calibration/Validation point acceptance [1: automatic (default) 0: manual]
    #foregroundBrightness: set Calibration/Validation target brightness [0..255] (default: 20)
    #backgroundBrightness: set Calibration/Validation background brightness [0..255] (default: 239)
    #targetShape: set Calibration/Validation target shape [IMAGE = 0,CIRCLE1 = 1 (default), CIRCLE2 = 2, CROSS = 3]
    #targetSize: set Calibration/Validation target size (default: 10 pixels)
    #targetFilename: select custom Calibration/Validation target

    #CALIBRATION SCRIPT HERE:
    if guichoice['Calibrate(Y/N)'] == 'Y':
        res = iViewXAPI.iV_SetupCalibration(byref(calibrationData))
        print "iV_SetupCalibration " + str(res)
        res = iViewXAPI.iV_Calibrate()
        print "iV_Calibrate " + str(res)

    if res == 131:
        print "ERR_NO_RESPONSE_FROM_IVIEWX iView X (eyetracking server) application was not able to response to current request"


