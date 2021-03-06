#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.85.6),
    on January 24, 2018, at 13:25
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'mainseq'  # from the Builder filename that created this script
expInfo = {u'Eye Tracker': u'SRR_eyelink_std.yaml', u'Participant': u'1'}
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' %(expInfo['Participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=False,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.WARNING)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(2560, 1440), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor='default', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='degFlatPos')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "StartupInstr"
StartupInstrClock = core.Clock()
#BUG in iohub having window initiate before iohub does forces us to do this:
win.close() # is used to close the current window so it won't interfere/block calibration API
#import pylink
import time

RoutineSpeedup = 1 #multiplier 1=1x speed, if 0.5 will run 2x as fast.
#Timer for minimum amount of time eye must be in window FP0,FP1,FP2 
EYEWINTIMECONST = 0.5*RoutineSpeedup # 500ms
FPMINFPTIME = 1*RoutineSpeedup #1 second minimum fixation time x a constant
FP2MINFIXTIME = 1*RoutineSpeedup

fpwin_all = 4 #degrees window allowed to reach target
debugflag = 0 # turn this to 1 to show xy position output in shell
showwin   = 1 # 1 to show window boundaries
#moe = 2 # 1 = mouse OR 2 = eye tracker by default
rendeye = 1 # renders the eye position info 1 = on; 0 = off
mxy = [0,0]
# some default variable declarations:
polyColor = "white" # default
fpwinx = 1
fpwiny = 1
fp2winx = 1
fp2winy = 1
trialtype = 1

#
# RUN SCRIPT WHICH IDENTIFIES WHICH PC/MAC is being used to adjust screen/settings
# creates variables e.g. moe=1/2, eyetracker=true/false, monitor screen width, etc..
#
execfile("IDMonLaunch_ioHub.py")
#
# ALSO LAUNCH IOHUB SERVER IN TWO DIFFERENT METHODS (All to be done by "MS_IDidentify.py")
#

# Now that iohub has been launched by the eye tracker code, open a window:
win = visual.Window(
    size=(screen_width,screen_height), fullscr=True, screen=0,
    allowGUI=True, allowStencil=False,
    monitor=psychopy_mon_name, color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True, useRetina=True,
    units='degFlatPos')

#set up event tracking by built in psychopy fn (NOT IOHUB process) for mouse position
ppmouse = event.Mouse()

#Define the first time instructions are seen
instr_rep_cont = 1

#Define instruction sets (according to trialtype) that have been displayed already
ttype1_instr = 0
ttype2_instr = 0
ttype3_instr = 0

# setup eye position shape here so don't have to recreate it for FP0, FP, FP2
# to move it with the eye, which is given in pixels, use unit pix

Shape01 = visual.Polygon(win=win, name='FP0_circle',units='degFlatPos', 
    edges = 10, size=[1,1],
    ori=0, pos=[0, 0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[0.7,0.7,0.7], fillColorSpace='rgb',
    opacity=0.5,depth=0.0, 
    interpolate=True)

Shape01.setAutoDraw(rendeye)

Text01 = visual.TextStim(win=win, text='', font='',
    pos=(0.0, 0.0), depth=0, rgb=None, color=(1.0, 1.0, 1.0),
    colorSpace='rgb', opacity=1.0, contrast=1.0, units='degFlatPos',
    ori=0.0, height=None, antialias=True, bold=False,
    italic=False, alignHoriz='center', alignVert='center',
    fontFiles=(), wrapWidth=None, flipHoriz=False, flipVert=False,
    name=None, autoLog=None)

Text01.setAutoDraw(True)


instrText = visual.TextStim(win=win, name='instrText',
    text='Main Sequence Test\n\nClick on Window Once Then\nPress Any Key to Continue',
    font='Arial',
    units='degFlatPos', pos=[0, 0], height=1.5, wrapWidth=800, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()

text = visual.TextStim(win=win, name='text',
    text='Any text\n\nincluding line breaks',
    font='Arial',
    units='degFlatPos', pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-1.0);

# Initialize components for Routine "ITI"
ITIClock = core.Clock()
trialnum = 0;

# Initialize components for Routine "FP0"
FP0Clock = core.Clock()
FP0_circle = visual.Polygon(
    win=win, name='FP0_circle',units='degFlatPos', 
    edges=10, size=(0.2, 0.2),
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=polyColor, lineColorSpace='rgb',
    fillColor=polyColor, fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
FP0_window = visual.Rect(
    win=win, name='FP0_window',units='degFlatPos', 
    width=[fpwin_all*2,fpwin_all*2][0], height=[fpwin_all*2,fpwin_all*2][1],
    ori=0, pos=[fpwinx*2, fpwiny*2],
    lineWidth=0, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.3, depth=-1.0, interpolate=True)
#this will set the polygon to draw after each call of win.flip()
#polygon.setAutoDraw(True)
#

# create handy time for FP0
routineTimer = core.CountdownTimer() # Fixation Point General timer (routine fixed)
windowTimer = core.CountdownTimer() # Fixation Window Timer
# more FP0 constants
FP0_window_color = 'white'

# Initialize components for Routine "FP1"
FP1Clock = core.Clock()
#FP1 default variables
FP1_window_color = 'green' #  set default color green


FP1_square = visual.Rect(
    win=win, name='FP1_square',units='degFlatPos', 
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
FP1_window = visual.Rect(
    win=win, name='FP1_window',units='degFlatPos', 
    width=[fpwin_all*2,fpwin_all*2][0], height=[fpwin_all*2,fpwin_all*2][1],
    ori=0, pos=[fpwinx*2, fpwiny*2],
    lineWidth=1, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.4, depth=-2.0, interpolate=True)

# Initialize components for Routine "FP2"
FP2Clock = core.Clock()
#default FP2 variables
FP2_window_color = [255,255,255]

#timer for FP2 FIXATION WINDOW MIN TIME maybe redundant can use window timer.
FP2_fbk_timer = core.CountdownTimer()

sound_win = sound.Sound(u'A', secs=0.2)
sound_win.setVolume(0.5)

sound_fail = sound.Sound(u'F', secs=0.2)
sound_fail.setVolume(0.5)
FP2_square = visual.Rect(
    win=win, name='FP2_square',units='degFlatPos', 
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0, pos=(0, 0),
    lineWidth=0, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)
FP2_window = visual.Rect(
    win=win, name='FP2_window',units='degFlatPos', 
    width=[fpwin_all*2,fpwin_all*2][0], height=[fpwin_all*2,fpwin_all*2][1],
    ori=0, pos=[fp2winx*2,fp2winy*2],
    lineWidth=0, lineColor=1.0, lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=0.4, depth=-2.0, interpolate=True)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!!! :)',
    font='arial',
    units='degFlatPos', pos=[0, 0], height=1.5, wrapWidth=800, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "StartupInstr"-------
t = 0
StartupInstrClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat

ready = event.BuilderKeyResponse()
# keep track of which components have finished
StartupInstrComponents = [instrText, ready]
for thisComponent in StartupInstrComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "StartupInstr"-------
while continueRoutine:
    # get current time
    t = StartupInstrClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    
    # *instrText* updates
    if t >= 0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *ready* updates
    if t >= 0 and ready.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready.tStart = t
        ready.frameNStart = frameN  # exact frame index
        ready.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in StartupInstrComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "StartupInstr"-------
for thisComponent in StartupInstrComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)

# the Routine "StartupInstr" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'FPtrialTypes5.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    # set up handler to look after randomisation of conditions etc
    instr_rep = data.TrialHandler(nReps=instr_rep_cont, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='instr_rep')
    thisExp.addLoop(instr_rep)  # add the loop to the experiment
    thisInstr_rep = instr_rep.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisInstr_rep.rgb)
    if thisInstr_rep != None:
        for paramName in thisInstr_rep.keys():
            exec(paramName + '= thisInstr_rep.' + paramName)
    
    for thisInstr_rep in instr_rep:
        currentLoop = instr_rep
        # abbreviate parameter names if possible (e.g. rgb = thisInstr_rep.rgb)
        if thisInstr_rep != None:
            for paramName in thisInstr_rep.keys():
                exec(paramName + '= thisInstr_rep.' + paramName)
        
        # ------Prepare to start Routine "instructions"-------
        t = 0
        instructionsClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(4.000000)
        # update component parameters for each repeat
        # First decide which ttype it is from trialtype variable
        # once trialtype is decided, ask if instructions have been displayed
        # if not display them once, and set ttype1_instr = 1; then next time won't be displayed
        
        if (trialtype == 1 and ttype1_instr == 0):
            ttype1_instr = 1
            text.text = "Look at the white dot"
        elif (trialtype == 2 and ttype2_instr == 0):
            ttype2_instr = 1
            text.text = "When red dot disappears, hold your gaze at the opposite mirror location of the white dot."
        elif (trialtype == 3 and ttype3_instr == 0):
            ttype3_instr = 1
            text.text = "Follow the dot as it moves."
        else:
        #    #intstr_rep.finished=1 # this did not work to end routine
            text.text = ""
            continueRoutine = False
            text.finished = 1
        
        
        
        # keep track of which components have finished
        instructionsComponents = [text]
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "instructions"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = instructionsClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if (trialtype == 1 and ttype1_instr == 1):
                continueRoutine = False
            elif (trialtype == 2 and ttype2_instr == 1):
                continueRoutine = False
            
            # *text* updates
            if t >= 0.0 and text.status == NOT_STARTED:
                # keep track of start time/frame for later
                text.tStart = t
                text.frameNStart = frameN  # exact frame index
                text.setAutoDraw(True)
            frameRemains = 0.0 + 4- win.monitorFramePeriod * 0.75  # most of one frame period left
            if text.status == STARTED and t >= frameRemains:
                text.setAutoDraw(False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in instructionsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "instructions"-------
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
    # completed instr_rep_cont repeats of 'instr_rep'
    
    
    # ------Prepare to start Routine "ITI"-------
    t = 0
    ITIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    print 'inside ITI now'
    
    #fp windows set
    fpwinx = fpwin_all # in degrees
    fpwiny = fpwin_all
    
    if eyetracker:
        #heldFixation = True #unless otherwise
        io.clearEvents('all')
        eyetracker.setRecordingState(True)
        print "FP0: eyetracker.setRecordingState(True)"
    
    # smooth pursuit starting location at eccentricity
    if trialtype == 3:
        FP0_circle.pos = fp2loc
        # get new location of FP2 for window
        fp0x = fp2loc[0]
        fp0y = fp2loc[1]
    else: #center 0,0 is starting FP0
        fp0x = 0
        fp0y = 0
    
    #if showwin == 1:
    #    print "inside FPx_window show: %d %d" % (fp0x, fp0y)
    #if showwin == 0:
    #    FPx_window.opacity = 0
    #    FPx_window.draw()
    # keep track of which components have finished
    ITIComponents = []
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ITI"-------
    while continueRoutine:
        # get current time
        t = ITIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        if moe == 1:
            mxy = mouse.getPosition() # used ppmouse instead of iohub's mouse.
            #mxy = ppmouse.getPos() # used ppmouse instead of iohub's mouse.
            # could try using numpy np. instead but this for now:
            mxy = [mxy[0]/mxydiv_factor,mxy[1]/mxydiv_factor]
            x=mxy[0] # this in degrees now
            y=mxy[1]
        elif moe == 2:
            # get /eye tracker gaze/ position 
            gpos=eyetracker.getPosition()
            if type(gpos) in [list,tuple]:
                x,y=gpos[0], gpos[1]
        elif moe == 200:
            res = iViewXAPI.iV_GetSample(byref(sampleData))
            mxy[0] = sampleData.leftEye.gazeX
            mxy[1] = sampleData.leftEye.gazeY
            x = (mxy[0] - screen_width/2)/pixperdegree
            y = ((screen_height/2) - mxy[1])/pixperdegree
        
        if rendeye == 1 :
        #    Image.setImage(images[index])
        #    Image.draw(window)
            #annoyingly eye position is returned as pixels, not degrees, upper left is 0,0.
            Shape01.setFillColor([0, 0, 0])
            #sampleData.leftEye.gazeX = sampleData.leftEye.gazeX - screen_width/2
            #sampleData.leftEye.gazeY = -1 * (sampleData.leftEye.gazeY - screen_height/2)
            #x= mxy[0]- (screen_width/2)
            #y= (-1 * mxy[1])
        
            #Shape01.setPos([sampleData.leftEye.gazeX, sampleData.leftEye.gazeY])
            Shape01.setPos([x, y]) 
            Shape01.draw()
            #tmptxt = 'x=%0.1f  y=%0.1f' %(x,y)
            #tmptxt = 'dx=%0.1f  dy=%0.1f' %(x-fp0x,y-fp0y)
            dispcountdown1 = 0 # routineTimer.getTime()
            dispcountdown2 = 0 #windowTimer.getTime()
            #if dispcountdown2 < 0:
            #    Text01.setColor((128,128,128),'rgb255') # set color to gray when count is <0
            #else:
            #    Text01.setColor((254,254,254),'rgb255')
            tmptxt = 'FP0: dx=%0.1f  dy=%0.1f\n   rT=%0.2f  wT=%0.2f' %(x-fp0x,y-fp0y,dispcountdown1,dispcountdown2)
            Text01.setText(text=tmptxt) # using setTextsuppresses logmsg
            Text01.setPos([x,y])
            Text01.draw()
            #update eye position
        
        
        
        #determine diff between eye/mouse and fp
        diffx = x-fp0x
        diffy = y-fp0y
        
        if debugflag == 1:
            ansx = abs(diffx)<fpwinx
            ansy = abs(diffy)<fpwiny
            #print "fp0: x:%d-%d=%d y:%d-%d=%d" % (mxy[0],fp0x,diffx,mxy[1],fp0y,diffy)
            print "fp0: x:%d-%d=%d < %d:%d y:%d-%d=%d < %d:%d" % (mxy[0],fp0x,diffx,fpwinx,ansx,mxy[1],fp0y,diffy,fpwiny,ansy)
            print "fp0: abs(mxy[0]-fp0x)=%d abs(mxy[1]-fp0y)=%d)" % (abs(mxy[0]-fp0x), abs(mxy[1]-fp0y))
        
        
        #if showwin == 1:
        #    FPx_window.pos = (fp0x, fp0y)
        #    FPx_window.draw()
        #elif showwin == 0:
        #    FPx_window.opacity = 0
            #FPx_window.draw()
        
        #no Need for this in ITI:
        # test if eye is in window
        #if ( abs(diffx) < fpwinx and abs(diffy) < fpwiny):
        #    FP0_rep.finished=1
        #    FPx_window.setColor = ((255,0,0), 'rgb255')
        #    if debugflag == 1:
        #        print "fp0: should exit"
        #elif (abs(diffx) > fpwinx or abs(diffy) > fpwiny):
        #    FPx_window.setColor = ((255,255,255), 'rgb255')
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ITIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ITI"-------
    for thisComponent in ITIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    FP0_rep = data.TrialHandler(nReps=999, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='FP0_rep')
    thisExp.addLoop(FP0_rep)  # add the loop to the experiment
    thisFP0_rep = FP0_rep.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFP0_rep.rgb)
    if thisFP0_rep != None:
        for paramName in thisFP0_rep.keys():
            exec(paramName + '= thisFP0_rep.' + paramName)
    
    for thisFP0_rep in FP0_rep:
        currentLoop = FP0_rep
        # abbreviate parameter names if possible (e.g. rgb = thisFP0_rep.rgb)
        if thisFP0_rep != None:
            for paramName in thisFP0_rep.keys():
                exec(paramName + '= thisFP0_rep.' + paramName)
        
        # ------Prepare to start Routine "FP0"-------
        t = 0
        FP0Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        
        print 'inside FP0 now'
        routineTimer.reset(1) # 1 second routine timer must manually set this here to match FP0_circle and FPx_window time lengths
        windowTimer.reset(EYEWINTIMECONST) # reset eye window timer
        
        #fp windows set
        fpwinx = fpwin_all # in degrees
        fpwiny = fpwin_all
        
        # smooth pursuit starting location at eccentricity
        if trialtype == 3:
            FP0_circle.pos = fp2loc
            # get new location of FP2 for window
            fp0x = fp2loc[0]
            fp0y = fp2loc[1]
        else: #center 0,0 is starting FP0
            fp0x = 0
            fp0y = 0
        
        #if showwin == 1:
        #    print "inside FPx_window show: %d %d" % (fp0x, fp0y)
        #if showwin == 0:
        #    FPx_window.opacity = 0
        #    FPx_window.draw()
        
        
        #print mouse
        # keep track of which components have finished
        FP0Components = [FP0_circle, FP0_window]
        for thisComponent in FP0Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "FP0"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FP0Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *FP0_circle* updates
            if t >= 0.5 and FP0_circle.status == NOT_STARTED:
                # keep track of start time/frame for later
                FP0_circle.tStart = t
                FP0_circle.frameNStart = frameN  # exact frame index
                FP0_circle.setAutoDraw(True)
            frameRemains = 0.5 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FP0_circle.status == STARTED and t >= frameRemains:
                FP0_circle.setAutoDraw(False)
            
            # *FP0_window* updates
            if t >= 0.0 and FP0_window.status == NOT_STARTED:
                # keep track of start time/frame for later
                FP0_window.tStart = t
                FP0_window.frameNStart = frameN  # exact frame index
                FP0_window.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FP0_window.status == STARTED and t >= frameRemains:
                FP0_window.setAutoDraw(False)
            if FP0_window.status == STARTED:  # only update if drawing
                FP0_window.setFillColor(FP0_window_color, log=False)
                FP0_window.setLineColor(FP0_window_color, log=False)
            #if mouse 
            if moe == 1:
                mxy = mouse.getPosition() #iohub
                #mxy = ppmouse.getPos() # psychopy built in mouse position tracker
                # could try using numpy np. instead but this for now:
                mxy = [mxy[0]/mxydiv_factor,mxy[1]/mxydiv_factor]
                x=mxy[0] # this in degrees now
                y=mxy[1]
            #else if not mouse then eye tracker:
            elif moe == 2:
                # get /eye tracker gaze/ position 
                gpos=eyetracker.getPosition()
                if type(gpos) in [list,tuple]:
                    x,y=gpos[0], gpos[1]
            elif moe == 200:
                res = iViewXAPI.iV_GetSample(byref(sampleData))
                mxy[0] = sampleData.leftEye.gazeX
                mxy[1] = sampleData.leftEye.gazeY
                x = (mxy[0] - screen_width/2)/pixperdegree
                y = ((screen_height/2) - mxy[1])/pixperdegree
            
            #determine distance between eye/mouse and fp
            diffx = x-fp0x
            diffy = y-fp0y
            
            # test if eye is in window
            if ( abs(diffx) < fpwinx and abs(diffy) < fpwiny):
                FP0_window_color = 'blue'
                if debugflag == 1:
                    print "fp0: should exit"
            elif (abs(diffx) > fpwinx or abs(diffy) > fpwiny):
                FP0_window_color = 'white'
                windowTimer.reset(EYEWINTIMECONST) # if outside of the window reset the timer
                
            
            # Display Code:
            if showwin == 1:
                FP0_window.pos = (fp0x, fp0y)
                #FP0_window.draw()
            elif showwin == 0:
                FP0_window.opacity = 0
                #FP0_window.draw()
            
            if rendeye == 1 :
            #    Image.setImage(images[index])
            #    Image.draw(window)
                #annoyingly eye position is returned as pixels, not degrees, upper left is 0,0.
                Shape01.setFillColor([0, 0, 0])
                #sampleData.leftEye.gazeX = sampleData.leftEye.gazeX - screen_width/2
                #sampleData.leftEye.gazeY = -1 * (sampleData.leftEye.gazeY - screen_height/2)
                #x= mxy[0]- (screen_width/2)
                #y= (-1 * mxy[1])
            
                #Shape01.setPos([sampleData.leftEye.gazeX, sampleData.leftEye.gazeY])
                Shape01.setPos([x, y]) 
                Shape01.draw()
                #tmptxt = 'x=%0.1f  y=%0.1f' %(x,y)
                #tmptxt = 'dx=%0.1f  dy=%0.1f' %(x-fp0x,y-fp0y)
                dispcountdown1 = routineTimer.getTime()
                dispcountdown2 = windowTimer.getTime()
                #if dispcountdown2 < 0:
                #    Text01.setColor((128,128,128),'rgb255') # set color to gray when count is <0
                #else:
                #    Text01.setColor((254,254,254),'rgb255')
                tmptxt = 'FP0: dx=%0.1f  dy=%0.1f\n   rT=%0.2f  wT=%0.2f' %(x-fp0x,y-fp0y,dispcountdown1,dispcountdown2)
                Text01.setText(text=tmptxt) # using setTextsuppresses logmsg
                Text01.setPos([x,y])
                Text01.draw()
                #update eye position
            
            if debugflag == 1:
                ansx = abs(diffx)<fpwinx
                ansy = abs(diffy)<fpwiny
                #print "fp0: x:%d-%d=%d y:%d-%d=%d" % (mxy[0],fp0x,diffx,mxy[1],fp0y,diffy)
                print "fp0: x:%d-%d=%d < %d:%d y:%d-%d=%d < %d:%d" % (mxy[0],fp0x,diffx,fpwinx,ansx,mxy[1],fp0y,diffy,fpwiny,ansy)
                print "fp0: abs(mxy[0]-fp0x)=%d abs(mxy[1]-fp0y)=%d)" % (abs(mxy[0]-fp0x), abs(mxy[1]-fp0y))
            
            # if eye is in window for 500ms*RoutineSpeedup then exit Routine
            if windowTimer.getTime()<0:
                continueRoutine = False
            
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FP0Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FP0"-------
        for thisComponent in FP0Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #Only if eye has been in the window for the last EYEWINDOWTIMECONT time then do you move on
        if windowTimer.getTime()<0:
            FP0_rep.finished=1
        else:
            FP0_rep.finished=0
        thisExp.nextEntry()
        
    # completed 999 repeats of 'FP0_rep'
    
    
    # set up handler to look after randomisation of conditions etc
    FP1_rep = data.TrialHandler(nReps=1, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='FP1_rep')
    thisExp.addLoop(FP1_rep)  # add the loop to the experiment
    thisFP1_rep = FP1_rep.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFP1_rep.rgb)
    if thisFP1_rep != None:
        for paramName in thisFP1_rep.keys():
            exec(paramName + '= thisFP1_rep.' + paramName)
    
    for thisFP1_rep in FP1_rep:
        currentLoop = FP1_rep
        # abbreviate parameter names if possible (e.g. rgb = thisFP1_rep.rgb)
        if thisFP1_rep != None:
            for paramName in thisFP1_rep.keys():
                exec(paramName + '= thisFP1_rep.' + paramName)
        
        # ------Prepare to start Routine "FP1"-------
        t = 0
        FP1Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(1.000000)
        # update component parameters for each repeat
        
        print 'inside FP now'
        
        #resettimer must  set routineTimer to same as time as long as routine is
        routineTimer.reset(FPMINFPTIME)
        windowTimer.reset(EYEWINTIMECONST)
        
        #fp windows set
        fpwinx = fpwin_all
        fpwiny = fpwin_all
        
        # smooth pursuit starting location at eccentricity
        if trialtype == 3:
            FP_square.pos = fp2loc
            # get new location of FP2 for window
            fp1x = fp2loc[0]
            fp1y = fp2loc[1]
        else: #center 0,0 is starting FP0
            fp1x = 0
            fp1y = 0
        
        
        
        
        FP1_square.setFillColor(polyColor)
        FP1_square.setLineColor(polyColor)
        # keep track of which components have finished
        FP1Components = [FP1_square, FP1_window]
        for thisComponent in FP1Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "FP1"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FP1Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if moe == 1:
                mxy = mouse.getPosition() #iohub
                #mxy = ppmouse.getPos() # psychopy built in mouse function
                # could try using numpy np. instead but this for now:
                mxy = [mxy[0]/mxydiv_factor,mxy[1]/mxydiv_factor]
                x=mxy[0] # this in degrees now
                y=mxy[1]
            elif moe == 2:
                # get /eye tracker gaze/ position 
                gpos=eyetracker.getPosition()
                if type(gpos) in [list,tuple]:
                    x,y=gpos[0], gpos[1]
            elif moe == 200:
                res = iViewXAPI.iV_GetSample(byref(sampleData))
                mxy[0] = sampleData.leftEye.gazeX # returns info in pixels
                mxy[1] = sampleData.leftEye.gazeY
                x = (mxy[0] - screen_width/2)/pixperdegree
                y = ((screen_height/2) - mxy[1])/pixperdegree
            
            
            if rendeye == 1 :
            #    Image.setImage(images[index])
            #    Image.draw(window)
                #annoyingly eye position is returned as pixels, not degrees, upper left is 0,0.
                Shape01.setFillColor([0, 0, 0])
                #sampleData.leftEye.gazeX = sampleData.leftEye.gazeX - screen_width/2
                #sampleData.leftEye.gazeY = -1 * (sampleData.leftEye.gazeY - screen_height/2)
                #x= mxy[0]- (screen_width/2)
                #y= (-1 * mxy[1])
                #Shape01.setPos([sampleData.leftEye.gazeX, sampleData.leftEye.gazeY])
                Shape01.setPos([x, y]) 
                Shape01.draw()
                # display timers and mouse/eye position
                dispcountdown1 = routineTimer.getTime()
                dispcountdown2 = windowTimer.getTime()
                #if dispcountdown2 < 0:
                #    Text01.setColor((128,128,128),'rgb255') # set color to gray when count is <0
                #else:
                #    Text01.setColor((254,254,254),'rgb255')
                tmptxt = 'FP1: dx=%0.1f  dy=%0.1f\n   rT=%0.2f  wT=%0.2f' %(x-fp0x,y-fp0y,dispcountdown1,dispcountdown2)
                #tmptxt = 'x=%0.1f  y=%0.1f' %(x,y)
                Text01.setText(text=tmptxt) # using setTextsuppresses logmsg
                Text01.setPos([x,y])
                Text01.draw()
                #update eye position
            
            # determine distsance between eye/mouse and fp1
            diffx= x-fp1x
            diffy= x-fp1y
            
            if debugflag == 1:
                print "fp1: x:%d-%d=%d y:%d-%d=%d" % (mxy[0],fp1x,diffx,mxy[1],fp1y,diffy)
            
            if showwin == 1:
                FP1_window.pos = (fp1x, fp1y)
                #FP1_window.draw()
            elif showwin == 0:
                FP1_window.opacity = 0
            
            # if leave the box, then start over
            # These flags will complete FP and FP2 loop and return to ITI
            if ( abs(diffx) > fpwinx or abs(diffy) > fpwiny):
                FP1_window_color = 'red'
                FP1_rep.finished = 1
                FP2cont = 0
                # if you lose fixation within a second, start again.
                # test if eye is in window
            elif ( abs(diffx) < fpwinx or abs(diffy) < fpwiny):
                FP1_window_color = 'green'
                
            
            #note FPcont is a variable used by FP2, if FPcont = 0
            #then FP2 will never be displayed and routine will repeat
            
            
            # *FP1_square* updates
            if t >= 0.0 and FP1_square.status == NOT_STARTED:
                # keep track of start time/frame for later
                FP1_square.tStart = t
                FP1_square.frameNStart = frameN  # exact frame index
                FP1_square.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FP1_square.status == STARTED and t >= frameRemains:
                FP1_square.setAutoDraw(False)
            
            # *FP1_window* updates
            if t >= 0.0 and FP1_window.status == NOT_STARTED:
                # keep track of start time/frame for later
                FP1_window.tStart = t
                FP1_window.frameNStart = frameN  # exact frame index
                FP1_window.setAutoDraw(True)
            frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FP1_window.status == STARTED and t >= frameRemains:
                FP1_window.setAutoDraw(False)
            if FP1_window.status == STARTED:  # only update if drawing
                FP1_window.setFillColor(FP1_window_color, log=False)
                FP1_window.setLineColor(FP1_window_color, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FP1Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FP1"-------
        for thisComponent in FP1Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        
        # Need minimum of 1 second stay in FP then can continue
        
        #if ( abs(mxy[0]-fp1x) < fpwinx and abs(mxy[1]-fp1y) < fpwiny ):
        #    FP2cont=1
        #    FP1_rep.finished=1
            # this last command presentationLoop.finished, exits the FP repeating loops
        
        # If eye is in the window (don't need windowtimer really) then continue
        if ( abs(diffx) < fpwinx and abs(diffy) < fpwiny):
            FP2cont = 1
            FP1_rep.finished=1
        else:
            FP2cont=0
        
        if eyetracker:
            #eyetracker.setRecordingState(False) # don't 
            #add eye-track data to data file
            trials.addData("FP1:heldFixation",True)
        
        thisExp.nextEntry()
        
    # completed 1 repeats of 'FP1_rep'
    
    
    # set up handler to look after randomisation of conditions etc
    FP2_rep = data.TrialHandler(nReps=FP2cont, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='FP2_rep')
    thisExp.addLoop(FP2_rep)  # add the loop to the experiment
    thisFP2_rep = FP2_rep.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisFP2_rep.rgb)
    if thisFP2_rep != None:
        for paramName in thisFP2_rep.keys():
            exec(paramName + '= thisFP2_rep.' + paramName)
    
    for thisFP2_rep in FP2_rep:
        currentLoop = FP2_rep
        # abbreviate parameter names if possible (e.g. rgb = thisFP2_rep.rgb)
        if thisFP2_rep != None:
            for paramName in thisFP2_rep.keys():
                exec(paramName + '= thisFP2_rep.' + paramName)
        
        # ------Prepare to start Routine "FP2"-------
        t = 0
        FP2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(5.000000)
        # update component parameters for each repeat
        print 'made it to FP2'
        
        
        #resettimer must  set routineTimer to same as time as long as routine is
        routineTimer.reset(5) # total time let for FP2 5 secs is long enough
        #windowTimer.reset(EYEWINTIMECONST) # is this redundant?
        windowTimer.reset(FP2MINFIXTIME) # is this redundant?
        #FP2_fbk_timer.reset(FP2MINFIXTIME) # 1 second of fixation required for FP2
        
        #LDS EDIT:
        #need to add this to move the fixation point other wise bug in menu of change on repeat taking $fp2loc does not work
        
        FP2_square.setPos(fp2loc)
        
        # get new location of FP2 for window
        fp2x = fp2loc[0]
        fp2y = fp2loc[1]
        
        #if showwin == 1:
        #    print "inside FP2_window show: %d %d" % (fp2loc[0], fp2loc[1])
        
        
        # if trialtype==2 (antisaccade task) make the window at the opposite location of the FP2
        if trialtype == 1:
            if showwin == 1:
                FP2_window.setPos(fp2loc)
                FP2_window.draw()
        elif trialtype == 2:
            fp2x = -fp2x
            fp2y = -fp2y
            if showwin == 1:
                FP2_window.setPos([fp2x,fp2y])
                FP2_window.draw()
        
        if showwin == 0:
            FP2_window.opacity = 0
            FP2_window.draw()
        
        #fp windows set here
        fp2winx = fpwin_all
        fp2winy = fpwin_all
        
        # adjust window size based on eccentricity of fp2 location
        # so small 
        #fp2winx = max(fp2loc)/3;
        #fp2winy = max(fp2loc)/3;
        #but a minimum of 1 degree
        #if fp2winx < 1:
        #    fp2winx = 1
        #    fp2winy = 1
        
        FP2_end_flag = 0 # set flag to 0 to add visual pause/color delay and sound
        
        if trialtype == 3:
            dps = 10 # 10 degrees per second
            spdist = 20 # 20 degrees distance for smooth pursuit analysis
            spstarttime = StartupClock.getTime()
            spendtime = spstarttime + (spdist / dps)
            spendtime_rel = spdist/dps
            if fp2x < 0:
                spdirx = 1; spdiry = 0;
            elif fp2x > 0:
                spdirx = -1; spdiry = 0;
            elif fp2y > 0:
                spdirx = 0; spdiry = -1;
            elif fp2y < 0:
                spdirx = 0; spdiry = 1;
            # give one degree extra for 'catchup saccade'
            fp2x = fp2x -spdirx*1;
            fp2y = fp2y -spdiry*1;
        
        
        
        
        # add a timer for feedback timer for FP2 (at least 1 sec of fixation requested)
        if trialtype == 3:
            FP2_fbk_timer = core.CountdownTimer(spendtime_rel)
        #else: # just fixation/saccade events so no delay for starting feedback timer
        #    FP2_fbk_timer = core.CountdownTimer(1)
        # keep track of which components have finished
        FP2Components = [FP2_square, FP2_window]
        for thisComponent in FP2Components:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "FP2"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = FP2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            if moe == 1:
                mxy = mouse.getPosition() #io hub mouse function
                #mxy = ppmouse.getPos() # psychopy mouse function
                # could try using numpy np. instead but this for now:
                mxy = [mxy[0]/mxydiv_factor,mxy[1]/mxydiv_factor]
                x=mxy[0] # this in degrees now
                y=mxy[1]
            elif moe == 2:
                # get /eye tracker gaze/ position 
                gpos=eyetracker.getPosition()
                if type(gpos) in [list,tuple]:
                    x,y=gpos[0], gpos[1]
            elif moe == 200:
                res = iViewXAPI.iV_GetSample(byref(sampleData))
                mxy[0] = sampleData.leftEye.gazeX
                mxy[1] = sampleData.leftEye.gazeY
                x = (mxy[0] - screen_width/2)/pixperdegree
                y = ((screen_height/2) - mxy[1])/pixperdegree
            #update eye position
            
            #determine diff between eye/mouse and fp
            diffx = x-fp2x
            diffy = y-fp2y
            
            if debugflag == 1:
                print "fp2b: x:%d-%d=%d y:%d-%d=%d" % (mxy[0],fp2x,diffx,mxy[1],fp2y,diffy)
            
            #if showwin == 1:
            #    FP2_window.setPos(fp2loc)
            #    FP2_window.draw()
            
            # if inside window then end routine
            if trialtype is not 3: # just fixations then look for eye position window, if it's a smooth pursuit don't use a window until the end (FP3-final)
                if (  abs(diffx) < fp2winx and abs(diffy) < fp2winy ):
                    FP2_window_color = 'green'
                    #FP2_square.setFillColor((1,0,0),'rgb')
                    # not inside window yet, but if first time inside, then start timer 1 second
                    if FP2_end_flag == 0: 
                        windowTimer.reset(FP2MINFIXTIME) #require 1 second of fixation
                        FP2_end_flag = 1
                    else: #countdowntimer
                        if windowTimer.getTime() < 0:
                            FP2_rep.finished = 1 # this flag will end the routine from repeating
                else: # if outside of window reset the timer
                    windowTimer.reset(FP2MINFIXTIME)
                    FP2_window_color = 'red'
                    
            
            elif trialtype is 3: # smooth pursuit trial
                spnowtime_rel = StartupClock.getTime() - spstarttime
                newFP2pos = [fp2x+spnowtime_rel*dps*spdirx, fp2y+spnowtime_rel*dps*spdiry]
                print newFP2pos
                FP2_square.pos = newFP2pos 
                if showwin == 1:
                    FP2_window.pos = newFP2pos
                    FP2_window.draw()
                if spnowtime_rel > spendtime_rel:
                    FP2_rep.finished = 1
                    continueRoutine = False
            
            if (FP2_rep.finished == 1):
                if (FP2_fbk_timer.getTime() > 0):
                    continueRoutine = True
                else:# ran out of feedback time
                    continueRoutine = False # try to force end of routine if eye is in window of FP2
            
            
            if rendeye == 1 :
            #    Image.setImage(images[index])
            #    Image.draw(window)
                #annoyingly eye position is returned as pixels, not degrees, upper left is 0,0.
                Shape01.setFillColor([0, 0, 0])
                #sampleData.leftEye.gazeX = sampleData.leftEye.gazeX - screen_width/2
                #sampleData.leftEye.gazeY = -1 * (sampleData.leftEye.gazeY - screen_height/2)
                #x= mxy[0]- (screen_width/2)
                #y= (-1 * mxy[1])
                #x = mxy[0] - screen_width/2
                #y = (screen_height/2) - mxy[1]
                #Shape01.setPos([sampleData.leftEye.gazeX, sampleData.leftEye.gazeY])
                Shape01.setPos([x, y]) 
                Shape01.draw()
                dispcountdown1 = routineTimer.getTime()
                dispcountdown2 = FP2_fbk_timer.getTime()
                #if dispcountdown2 < 0:
                #    Text01.setColor((128,128,128),'rgb255') # set color to gray when count is <0
                #else:
                #    Text01.setColor((254,254,254),'rgb255')
                tmptxt = 'FP2: dx=%0.1f  dy=%0.1f\n   rT=%0.2f  wT=%0.2f' %(x-fp0x,y-fp0y,dispcountdown1,dispcountdown2)
                Text01.setText(text=tmptxt) # using setTextsuppresses logmsg
                Text01.setPos([x,y])
                Text01.draw()
                #update eye position
                if debugflag == 1:
                    diffx= mxy[0]-fp2x
                    diffy= mxy[1]-fp2y
                    print "fp2a: x:%d-%d=%d y:%d-%d=%d" % (mxy[0],fp2x,diffx,mxy[1],fp2y,diffy)
            
            
            
            
            # *FP2_square* updates
            if t >= 0.0 and FP2_square.status == NOT_STARTED:
                # keep track of start time/frame for later
                FP2_square.tStart = t
                FP2_square.frameNStart = frameN  # exact frame index
                FP2_square.setAutoDraw(True)
            frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FP2_square.status == STARTED and t >= frameRemains:
                FP2_square.setAutoDraw(False)
            
            # *FP2_window* updates
            if t >= 0.0 and FP2_window.status == NOT_STARTED:
                # keep track of start time/frame for later
                FP2_window.tStart = t
                FP2_window.frameNStart = frameN  # exact frame index
                FP2_window.setAutoDraw(True)
            frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
            if FP2_window.status == STARTED and t >= frameRemains:
                FP2_window.setAutoDraw(False)
            if FP2_window.status == STARTED:  # only update if drawing
                FP2_window.setFillColor(FP2_window_color, log=False)
                FP2_window.setLineColor(FP2_window_color, log=False)
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in FP2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # check for quit (the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "FP2"-------
        for thisComponent in FP2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        #play sound according to win or fail
        
        #print 'mxy[0]:',mxy[0],'mxy[1]:',mxy[1]
        #print 'fp2x:',fp2x,'fp2y:',fp2y
        #print 'fp2winx:',fp2winx,'fp2winy:',fp2winy
        #print '==========='
        
        if ( abs(diffx) > fp2winx or abs(diffy) > fp2winy ): #and FP2_rep.finished == 1:
            sound_fail.play()
        
        if ( abs(diffx) <= fp2winx or abs(diffy) <= fp2winy ): #and FP2_rep.finished == 1:
            sound_win.play()
            windowTimer.add(0.50000)
        
        if eyetracker:
            eyetracker.setRecordingState(False)
            print "FP2: eyetracker.setRecordingState(False)"
            #add eye-track data to data file
            trials.addData("FP2:completedJumptoFP2", True)
        
        thisExp.nextEntry()
        
    # completed FP2cont repeats of 'FP2_rep'
    
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksText.status == STARTED and t >= frameRemains:
        thanksText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
if eyetracker:
    eyetracker.setConnectionState(False)
    io.quit()





# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
