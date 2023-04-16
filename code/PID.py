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
    result = (output,  intergral. error)
    return result


#Deze PID voor debug reden vooral gemaakt
def callbePid(input : tuple) -> tuple:
    dt = 0.5
    result = pid(3, 2, 0.8, dt, input[0], input[1], input[2])
    return result

def callbePidHeight(input : tuple) -> tuple:
    dt = 0.5
    result = pid(3, 2, 0.8, dt, input[0], input[1], input[2])
    return result

