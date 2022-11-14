import seaborn as sns
import matplotlib.pyplot as plt
import PID
import Sensor
import Simulation




#volle intergratie test,
#alles in seaborn om te kijken als het syteem zich naar stabiele toestand kan bregen
def runSimulationSeaborn(positieX : float, positieY : float, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight,
                  intergralSpeed, previousErrorSpeed , intergralHeight, previousErrorHeight,lengt,
                    errorArray ,timeArray ,speedArray , powerArray , heightArray
                         ):
    if (lengt > 0):

        result = Simulation.updateObject(positieX, positieY, speedX, speedY, power, dt, weight, Simulation.UpdateAngleOfAttack(currentAngle, servoAngle, dt))
        #update all variables
        positieX = result[0]
        positieY = result[1]
        speedY = result[3]
        speedX = result[2]
        currentAngle = result[4]
        errorSpeed = setpointSpeed - speedX
        errorheigt = setpointY - positieY

        #call the PID`s
        resultPidSpeed = PID.pid(3, 2, 0.8, dt, errorSpeed, intergralSpeed, previousErrorSpeed)
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


        speedArray += [speedX]
        powerArray += [power]
        heightArray += [positieY]
        timeArray += [dt * lengt]



        runSimulationSeaborn(positieX, positieY, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight,
                      intergralSpeed, previousErrorSpeed , intergralHeight, previousErrorHeight,lengt -1 , errorArray ,timeArray ,speedArray , powerArray , heightArray)
errorArray = []
timeArray = []
speedArray = []
powerArray = []
heightArray = []

runSimulationSeaborn(positieX= 10, positieY=15, speedX=20, setpointSpeed=10, setpointY=30,   speedY=2, currentAngle=0, servoAngle=0, power=10, dt=0.5, weight=0.2,
                          intergralSpeed=0, previousErrorSpeed=0 , intergralHeight=0, previousErrorHeight=0,lengt=25,
                     errorArray = errorArray ,timeArray= timeArray ,speedArray = speedArray , powerArray = powerArray , heightArray = heightArray )



plot = sns.lineplot(x=timeArray, y=speedArray, label="speed")
plot = sns.lineplot(x=timeArray, y=powerArray, label="thrust")
plot = sns.lineplot(x=timeArray, y=heightArray, label="height")

plt.show()