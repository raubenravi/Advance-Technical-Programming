
cdef extern from "sensor.cpp":
    int readSensor( int adresss, int high_bit, int low_bit )

def read(int adresss, testData):
    return readSensor(adresss, int(testData[0]), int(testData[1]))
