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
def makeAFlight(positieX : float, positieY : float, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight, lengt,
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
        errorSpeed = setpointSpeed - speedX
        errorheigt = setpointY - positieY


        thrustControlOutput =   thrustControl((errorSpeed,thrustControlOutput[1],thrustControlOutput[2]))
        heightControlOutput = heigtControl((errorheigt, heightControlOutput[1], heightControlOutput[2]))
        power = thrustControlOutput[0]
        if (power < 0):
            power = 0

        servoAngle = heightControlOutput[0]

        makeAFlight(positieX, positieY, speedX, setpointSpeed, setpointY,  speedY, currentAngle, servoAngle, power, dt, weight,lengt -1 ,
                    thrustControl, thrustControlOutput, heigtControl, heightControlOutput)


makeAFlight(positieX= 0, positieY=13, speedX=17, setpointSpeed=20, setpointY=15,   speedY=2, currentAngle=0, servoAngle=0, power=10, dt=0.5, weight=0.2,lengt=40,
            thrustControl=callbePid, thrustControlOutput= (0,0,0), heigtControl=callbePidHeight , heightControlOutput = (0,0,0)
                        )

def extract_element(lst: list[list], index) -> list:
    return list(map(lambda x: x[index], filter(lambda x: len(x) > 0, lst)))

plot = sns.lineplot( extract_element(makeAFlight.data, 2), label="speed")
plot = sns.lineplot(extract_element(makeAFlight.data, 8), label="thrust")
plot = sns.lineplot(extract_element(makeAFlight.data, 7), label="angle servo")
plot = sns.lineplot(extract_element(makeAFlight.data, 1), label="height")
makeAFlight = []
plt.show()