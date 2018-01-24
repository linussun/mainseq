Eye Tracking the Main Sequence (Sun/Goldberg Lab)

This is a Psychopy2 builder file (.psyexp extension) for use with standalone psychopy and should work in Windows or Mac OS X.  To make it work a few monitor settings in Psychopy needs to be set first:

Settings for Psychopy Preferences: 
	
	In the builder view, click on the 7th icon:
	(crossing monkey wrench and screwdriver)

	In the General Tab
		window type = pyglet
		units = deg
		audio Library should read: [‘sounddevice’,’pyo’,’pygame’]
		audio Driver should read: [‘Primary Sound’,’ASIO’,’Audigy’]
		audioDevice should be Primary Sound Driver or Output speaker on Mac

	In the Builder view, click on 8th icon

	Monitor Center (More instructions to be updated later)

In the very first routine (StartupInstr), in the Begin Experiment tab there is a call to execfile
script “IDMonLaunch_ioHub.py” where various monitor settings are stored, and settings
for using a mouse or eye tracker are hard coded for each PC/Laptop setup. 
In this tab, there is a final call to open a window full screen, thus the resolution
may or may not matter. The reporting of the mouse units since it is being queried
from the iohub process, should be determined by the SRR_eyelink_std.yaml configuration
file if eyetracker is set to TRUE. If eyetracker == False then the older launchHubServer function
runs.

The rest of the builder file (MainSequenceBeta1.psyexp file) is the experiment logic.

How to turn eye position/mouse position rendering on and off:

	This basic configuration can be found in the routine StartupInstr
	In the Begin Experiment Tab (for displaying window boxes or eye position rendering)


Make sure to set shapes to degFlatPos
And in experiment settings tab too (blue screen with white double ended arrows in it-tab 3-4)

======================================
Programmer notes: 

When activating the subroutine that captures eye movements 

io=iohubConnection() reports in Degrees (good!), the 
position of the eye rendering and units are in degrees which matches with the experiment
logic, even though pixels could be used and may be more accurate, the angle in degrees
is now consistent in every part of the code so control of eye position matches. 

The reduced simpler io=ioHubServer() seems to report mouse position in PIXELS ONLY, which
leads to a mismatch between the mouse position and the rendered eye position as expected. The mouse.getPosition fn returns in pixels which have to be divided by a number (17 or 33 depending on the platform/PC) so that the mouse position is approximate to the eye rendered in degrees. 

event.mouse.getPos() bugged if use pyglet for display, pygame doesn’t work either, stick with pyglet and submit bug report for line 558 in:
  File "/Applications/PsychoPy2.app/Contents/Resources/lib/python2.7/psychopy/event.py", line 558, in getPos
    lastPosPix = lastPosPix - self.win.size / 2

======================================
Known Bugs:
on Win 10 PC, if mouse does not respond, restart script or restart psychopy (probably iohub process not closed fully)

Ryu’s Screen
Screen Width 30.5 cm
Screen height 17cm
H 1366
V 768
‘DESKTOP-HL8BRQT’

Alex’s Linus Amritas 
MBP13.3” =  28.65H 17.9cmV
H 2560
V 1600
‘Amalias-macbook-pro’
‘Liner-MBP’
‘Alexanders-Macbook-Pro’

Kirstie 
28x15.5cm
H 2304
V 1440
‘Kirsties-Macbook’

Zikang
Screen Width
h 2736
v 1824
screen width 26cm
‘SurfacePro’

Arya - MBP 15
33.1 x 20.78
h 2880
v 1800
‘Aryas-MBP.local’
