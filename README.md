THIS REPOSITORY IS FOR Eye Movement Related Projects with Sun/Goldberg Lab

It is a Psychopy2 builder file for use with standalone psychopy and should work in Windows 
or Mac OS X.  To make it work a few monitor settings in Psychopy needs to be set first:

Settings for Psychopy Preferences
	In the builder view, click on the 7th icon:
	(crossing monkey wrench and screwdriver)

	In the General Tab
		audio Library should read: ['sounddevice','pyo','pygame']
		audio Driver should read: ['Primary Sound','ASIO','Audigy']
		audioDevice should be Primary Sound Driver or Output speaker on Mac

	In the Builder view, click on 8th icon
	Monitor Center 
		(TBD)


In StartupInstr Routine, Begin Experiment tab there is a call to execfile script
"IDMonLaunch_ioHub.py" where various monitor settings are stored, and settings
for using a mouse or eye tracker are hard coded for each PC/Laptop setup. 
In this tab, there is a final call to open a window full screen, thus the resolution
may or may not matter (unclear - may be cause for bug of mouse position).

The rest of the builder file (MainSequenceBeta1.psyexp file) is the experiment logic.

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
MBP13.3” =  33.8cm
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
