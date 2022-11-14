import math
import seaborn as sns
import matplotlib.pyplot as plt
import PID
import Simulation
import  Sensor

#function to get new Angle of attack and update servo position
#set point should be the  output from the PID, it`s the angle the servo is set to


#run 1 tik of the complete simulation
def runSimulation(positieX : float, positieY : float, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight,
                  intergralSpeed, previousErrorSpeed , intergralHeight, previousErrorHeight,lengt ):
    if (lengt > 0):


        # 'reading' sensors data
        positieY = Sensor.readSensor(addres=0x05, testData= Sensor.createTesData(int(positieY * 100)  )) / 100 # converting from meter to cenimters and back
        speedX = Sensor.readSensor(addres=0x05, testData= Sensor.createTesData(int(math.floor(speedX))))


        result = Simulation.updateObject(positieX, positieY, speedX, speedY, power, dt, weight, Simulation.UpdateAngleOfAttack(currentAngle, servoAngle, dt))
        #update all variables
        positieX = result[0]
        positieY = result[1]
        speedX = result[2]
        speedY = result[3]
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



        runSimulation(positieX, positieY, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight,
                      intergralSpeed, previousErrorSpeed , intergralHeight, previousErrorHeight,lengt -1 )

runSimulation(positieX= 10, positieY=5, speedX=5, setpointSpeed=10, setpointY=8,   speedY=0, currentAngle=0, servoAngle=0, power=10, dt=0.5, weight=0.2,
                      intergralSpeed=0, previousErrorSpeed=0 , intergralHeight=0, previousErrorHeight=0,lengt=30 )

