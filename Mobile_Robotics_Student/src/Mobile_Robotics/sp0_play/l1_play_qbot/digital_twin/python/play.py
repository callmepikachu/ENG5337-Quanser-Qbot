#-----------------------------------------------------------------------------#
#-----------------------Skills Progression 0 - Play---------------------------#
#-----------------------------------------------------------------------------#
#----------------------------Lab 1 - QBot Platform----------------------------#
#-----------------------------------------------------------------------------#

# Imports
from pal.products.qbot_platform import QBotPlatformDriver,Keyboard,\
    QBotPlatformCSICamera, QBotPlatformRealSense, QBotPlatformLidar
from quanser.hardware import HILError
from pal.utilities.probe import Probe
from pal.utilities.gamepad import LogitechF710
import time
import numpy as np
from qlabs_setup import setup

# Section A - Setup
setup(locationQBotP=[0, -0.042, 0.05], verbose=True)
time.sleep(2)
ipHost, ipDriver = 'localhost', 'localhost'
commands, arm, noKill = np.zeros((2), dtype = np.float64), 0, True
frameRate, sampleRate = 60.0, 1/60.0
endFlag, counter, counterRS, counterDown, counterLidar = False, 0, 0, 0, 0
simulationTime = 90.0
startTime = time.time()
def elapsed_time():
    return time.time() - startTime
timeHIL, prevTimeHIL = elapsed_time(), elapsed_time() - 0.017

try:
    # Section B - Initialization
    myQBot       = QBotPlatformDriver(mode=1, ip=ipDriver)
    downCam      = QBotPlatformCSICamera(exposure = 10)
    realSenseCam = QBotPlatformRealSense()
    lidar        = QBotPlatformLidar()
    keyboard     = Keyboard()

    # Section C - Initialization to send data to main computer
    probe        = Probe(ip = ipHost)
    # probe.add_display(imageSize = [400, 640, 1], scaling = True,
    #                   scalingFactor= 2, name="Downward Camera Image")
    probe.add_display(imageSize = [480, 640, 3], scaling = True,
                      scalingFactor= 2, name="RealSense RGB Image")
    # probe.add_display(imageSize = [480, 640, 1], scaling = True,
    #                   scalingFactor= 2, name="RealSense Depth Image")
    # probe.add_plot(numMeasurements=1680, scaling=True,
    #                   scalingFactor= 8, name='Leishen Lidar')
    startTime = time.time()
    time.sleep(0.5)

    # Main loop
    while noKill and not endFlag:
        t = elapsed_time()

        if not probe.connected:
            probe.check_connection()

        if probe.connected:

            # Section D - Send and Receive Data
            # QBot Hardware
            newHIL = myQBot.read_write_std(timestamp = time.time() - startTime,
                                            arm = arm,
                                            commands = commands)
            if newHIL:
                timeHIL = time.time()

                # Downward camera, RealSense camera & Lidar acquisition
                newDownCam = downCam.read()
                newRealSenseDepth = realSenseCam.read_depth(dataMode='M')
                newRealSenseRGB = realSenseCam.read_RGB()
                newLidar = lidar.read()

                # Section E - Sending data to Observer in main computer
                # Remote probe
                if newDownCam: counterDown += 1
                if newRealSenseDepth or newRealSenseRGB: counterRS += 1
                if newLidar: counterLidar += 1
                # if counterDown%4 == 0:
                    # sending = probe.send(name="Downward Camera Image",
                    #                      imageData=downCam.imageData)
                # if counterRS%4 == 2:
                #     sending = probe.send(name="RealSense Depth Image",
                #                          imageData=cv2.convertScaleAbs(realSenseCam.imageBufferDepthM, alpha=(255.0/3.0)))
                elif counterRS%4 == 0:
                    sending = probe.send(name="RealSense RGB Image",
                                         imageData=realSenseCam.imageBufferRGB)
                # if counterLidar%6 == 0:
                #     sending = probe.send(name="Leishen Lidar",
                #                          lidarData=(lidar.distances, (np.pi/2 - lidar.angles)) )
                prevTimeHIL = timeHIL

            # End condition
            endFlag = t > simulationTime
            if endFlag:
                print("Application completed successfully")

            # Section F - Keyboard to commands
            newkeyboard = keyboard.read()
            if newkeyboard:
                (forSpd,turnSpd) = keyboard.bodyCmd
                arm = keyboard.k_space
                commands = np.array([forSpd, turnSpd], dtype = np.float64)
                if keyboard.k_u:
                    print("Operator: Emergency Stop")
                    noKill = False 

except KeyboardInterrupt:
    print('User interrupted.')
except HILError as h:
    print(h.get_error_message())
finally:
    # Termination
    downCam.terminate()
    myQBot.terminate()
    realSenseCam.terminate()
    lidar.terminate()
    keyboard.terminate()
    probe.terminate()