import math

#calculate the new speed
def getSpeedX(speed, power):
    if (speed >= 0):
       dragForce = 0.5 * 1.225 * math.pow(speed, 2) * 0.1 * 1.5
    else:
        dragForce = 0
    weight = 0.200
    Acceraltion =  (power * weight) - (dragForce * weight)
    speed += Acceraltion
   # print(speed)
    return speed




#lift equation
def liftEquation(speed, angleOfAttack) -> float:
    r = 1.225 #density of air
    A = 0.6 #wing Area
    CL = 2 * math.pi * math.radians(angleOfAttack)
    L = CL * ( r * pow(speed, 2) / 2 * A)
    return L

#function to update the plane, calculates the new speed en height by using physical fomrulas
def updateObject(positieX : float, positieY : float, speedX : float, speedY : float, power : float, dt : float, weight : float , angleOfAttack : float):
    speedX = getSpeedX(speedX, power)
    positieX = positieX + speedX * dt
    speedY = liftEquation(speedX, angleOfAttack) * weight
    positieY = positieY + speedY * dt
    positieY = positieY - 9.81 * weight * dt
    return (positieX, positieY, speedX, speedY, angleOfAttack)


#claculte new angle of attack
def UpdateAngleOfAttack(currentAngle : float, setPoint : float, dt : float) -> float:

    currentAngle += setPoint * dt * 0.2 #the 0.2 is to delay it beacuse the servo isn`t that fast
    if (currentAngle > 90):
        currentAngle = 90
    if (currentAngle < -90):
        currentAngle = -90
    return currentAngle

