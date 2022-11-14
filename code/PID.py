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