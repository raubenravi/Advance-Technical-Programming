import seaborn as sns
import matplotlib.pyplot as plt
from PID import pid, callbePid, callbePidHeight
import Sensor
import Simulation
from typing import Callable, Tuple



def logger(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        x = args
        inner.data.insert(0,x)
        return result
    inner.data = []
    return inner

@logger
def takeOFf(positieX : float, positieY : float, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight, lengt,
                         thrustControl : Callable[[tuple], tuple] , thrustControlOutput : tuple,
                        heigtControl : Callable[[tuple], tuple] , heightControlOutput : tuple) :
    if (lengt > 0):
        result = Simulation.updateObject(positieX, positieY, speedX, speedY, power, dt, weight,
                                         Simulation.UpdateAngleOfAttack(currentAngle, servoAngle, dt))
        #update all variables
        positieX = result[0]
        positieY = result[1]
        speedY = result[3]
        speedX = result[2]
        currentAngle = result[4]

        power = power
        servoAngle = servoAngle


        takeOFf(positieX, positieY, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight,lengt -1 ,
                    thrustControl, thrustControlOutput, heigtControl, heightControlOutput)


takeOFf(positieX= 0, positieY=0, speedX=0, setpointSpeed=20, setpointY=15,   speedY=0, currentAngle=0, servoAngle=25, power=10, dt=0.5, weight=0.2,lengt=5,
            thrustControl=callbePid, thrustControlOutput= (0,0,0), heigtControl=callbePidHeight , heightControlOutput = (0,0,0)
                        )

def extract_element(lst: list[list], index) -> list:
    return list(map(lambda x: x[index], filter(lambda x: len(x) > 0, lst)))

plot = sns.lineplot( extract_element(takeOFf.data, 2), label="speed")
plot = sns.lineplot(extract_element(takeOFf.data, 8), label="thrust")
plot = sns.lineplot(extract_element(takeOFf.data, 7), label="angle servo")
plot = sns.lineplot(extract_element(takeOFf.data, 1), label="height")
takeOFf.data = []
plt.show()

#integratie test 2, "motor uit gezet"
takeOFf(positieX= 0, positieY=10, speedX=10, setpointSpeed=20, setpointY=15,   speedY=0, currentAngle=0, servoAngle=0, power=0, dt=0.5, weight=0.2,lengt=10,
            thrustControl=callbePid, thrustControlOutput= (0,0,0), heigtControl=callbePidHeight , heightControlOutput = (0,0,0) )

plot = sns.lineplot( extract_element(takeOFf.data, 2), label="speed")
plot = sns.lineplot(extract_element(takeOFf.data, 8), label="thrust")
plot = sns.lineplot(extract_element(takeOFf.data, 7), label="angle servo")
plot = sns.lineplot(extract_element(takeOFf.data, 1), label="height")

plt.show()