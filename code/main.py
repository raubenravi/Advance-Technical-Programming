import math
import seaborn as sns
import matplotlib.pyplot as plt

def pid(Kp : float, ki : float, kd : float, dt : float , error : float, intergral: float, previousError : float) -> tuple:
    intergral = intergral + error * dt;
    derivative = (error - previousError) / dt;
    output = Kp * error + ki * intergral + kd * derivative;
    result = (output, error, intergral)
    return result

def pidheight(Kp : float, ki : float, kd : float, dt : float , error : float, intergral: float, previousError : float) -> tuple:
    intergral = intergral + error * dt;
    derivative = (error - previousError) / dt;
    output = Kp * error + ki * intergral + kd * derivative;
    result = (output, error, intergral)
    return result

def getSensorTesting():
    return None

def getSpeedX(speed, power):
    if (speed >= 0):
       dragForce = 0.5 * 1.225 * math.pow(speed, 2) * 0.1 * 1.5
    else:
        dragForce = 0
    weight = 0.200
    print(dragForce)
    Acceraltion =  (power * weight) - (dragForce * weight)
    speed += Acceraltion
   # print(speed)
    return speed

def getSpeedY(speed):
    weight = 0.200
    speed += get
   # print(speed)
    return speed

def getAngleOfAttack():
    return 0.26

def liftEquation(speed) -> float:
    A = 0.15
    r = 1.225
    Cl = getAngleOfAttack()
    L = Cl * ( r * pow(speed, 2) / 2 * A)
    weigth = 10
    #L -= 9,81 * weigth
    return L

def updatepos(positieX, positieY, speedX, speedY power, dt):
    speed = getSpeedX(speedX, power)
    positieX = positieX + speed * dt
    positieY = positieY +  liftEquation(speed) * 0.200 * dt
    positieY = positieY - 9.81 * 0.200 * dt
    return (positieX, positieY, speedX, speedY)

#function to get new Angle of attack and update servo position
#set point should be the  output from the PID, it`s the angle the servo is set to
def UpdateAngleOfAttack(currentAngle : float, CurrentAngleServo : float, setPoint : float, dt : float) -> tuple:
    if (setPoint > 45):
        setPoint = 45
    if (setPoint < -45):
        setPoint = -45
    error = setPoint - currentAngle
    CurrentAngleServo += error * dt
    currentAngle += CurrentAngleServo * dt
    result = (currentAngle, CurrentAngleServo)
    return result

def getHeight():
    return 0

def speedSensor():
    return 0


setpoint = 10
#Kp, Ki, Kd = 1
positieX = 5
positieY = 10
speed = 35
power= 0
dt= 0.5
error = setpoint - speed
resultPid = pid(3, 2, 0.8 , dt ,error, 0, 0)
output = resultPid[0]
previousError = resultPid[1]
intergral = resultPid[2]
error = setpoint - speed
time = 0
errorArray = []
timeArray = []
speedArray = []
powerArray = []
heightArray = []
for i in range(30):
    #print(currentPos)
    resultPid = pid(3, 2, 0.8 , dt, error, intergral, previousError)
    power = resultPid[0]
    if (power < 0):
        power = 0
    previousError = resultPid[1]
    intergral = resultPid[2]
    result = updatepos(positieX, positieY, speed, power, dt)
    positieX = result[0]
    positieY = result[1]
    speed = result[2]
    error = setpoint - speed
    errorArray += [error]
    speedArray += [speed]
    powerArray += [power]
    heightArray += [positieY]
    timeArray += [dt * i]



plot = sns.lineplot(x=timeArray, y=errorArray, label="error")
plot = sns.lineplot(x=timeArray, y=speedArray, label="speed")
plot = sns.lineplot(x=timeArray, y=powerArray, label="thrust")
plot = sns.lineplot(x=timeArray, y=heightArray, label="height")
plt.show()
#FD = 0.5 * 1.225 * speed ^ 2 * 0.1 * 1.5

#wing area = 0.36

#
#def runSimulation(length, setpoin, )