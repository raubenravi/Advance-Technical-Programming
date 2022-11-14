

#https://www.renesas.com/eu/en/document/dst/fs1015-datasheet?r=343956
def readSensor(addres : int, testData : list) -> int:
    print("reading from device: " , 0x0f , " at adress: ", addres, " return data: ", testData[0] , " <- low, high-> ", testData[1])
    distance = (testData[0] << 8) | testData[1];
    return distance

def createTesData(data : int) -> list:
    testData = divmod(data, 256)
    return testData


