import math
import PID
import Simulation
import  mockObjectsCpp
import Sensor
import numpy as np

#function to get new Angle of attack and update servo position
#set point should be the  output from the PID, it`s the angle the servo is set to
import hBridge
import servo


def runSimulation(positieX : float, positieY : float, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight,
                  intergralSpeed, previousErrorSpeed , intergralHeight, previousErrorHeight,lengt ):
    if (lengt > 0):

        # 'reading' sensors data


        positieY = mockObjectsCpp.read(5, (Sensor.createTesData(positieY)))
        speedX = mockObjectsCpp.read(5,  (Sensor.createTesData(speedX)))
        print("the height is ", positieY)
        print("the speed is", speedX)


        result = Simulation.updateObject(positieX, positieY, speedX, speedY, power, dt, weight, Simulation.UpdateAngleOfAttack(currentAngle, servoAngle, dt))
        #update all variables
        positieX = result[0]
        positieY = result[1]
        speedY = result[3]
        speedX = result[2]
        currentAngle = result[4]
        error = setpointSpeed - speedX
        errorheigt = setpointY - positieY

        #call the PID`s
        resultPidSpeed = PID.pid(3, 2, 0.8, dt, error, intergralSpeed, previousErrorSpeed)
        power = resultPidSpeed[0]
        #disable reverse thrust
        if (power < 0):
            power = 0
        previousErrorHeight = resultPidSpeed[1]
        intergralHeight = resultPidSpeed[2]

        resultPidHeight = PID.pid(3, 2, 0.8, dt, errorheigt, intergralHeight, previousErrorHeight)
        servoAngle = resultPidHeight[0]
        previousErrorHeight = resultPidHeight[1]
        intergralHeight = resultPidHeight[2]

        servo.servo(servoAngle)
        hBridge.hBridge(power)


        runSimulation(positieX, positieY, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight,
                      intergralSpeed, previousErrorSpeed , intergralHeight, previousErrorHeight,lengt -1 )

runSimulation(positieX= 10, positieY=5, speedX=25, setpointSpeed=30, setpointY=8,   speedY=0, currentAngle=0, servoAngle=0, power=10, dt=0.5, weight=0.2,
                      intergralSpeed=0, previousErrorSpeed=0 , intergralHeight=0, previousErrorHeight=0,lengt=100 )