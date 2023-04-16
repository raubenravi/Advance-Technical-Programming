from unittest import *
import io
import seaborn as sns
import matplotlib.pyplot as plt
import PID
import Sensor
import mockObjectsCpp
import Simulation


class TestingSensor(TestCase):
    def setUp(self):
        self.out = io.StringIO()
    def testCreatingTesDataLow(self):
        height = 125
        data =  Sensor.createTesData(height)
        self.assertEqual(data[0] , 0)
        self.assertEqual(data[1], 125)

    def testCreatingTesDatahigh(self):
        height = 300
        data = Sensor.createTesData(height)
        self.assertEqual(data[0], 1)
        self.assertEqual(data[1], 300 - 256, "data not correct")


    def testdummydata(self):
        x = 1900
        y = mockObjectsCpp.read(0, Sensor.createTesData( x))
        self.assertEqual(x , y, "data not correct")

    def testdummyLowBit(self):
        x = 100
        y = mockObjectsCpp.read(0, Sensor.createTesData(x))
        self.assertEqual(x, y, "data not correct")

    def testdummyZero(self):
        x = 0
        y = mockObjectsCpp.read(0, Sensor.createTesData(x))
        self.assertEqual(x, y, "data not correct")



sensorTester = TestingSensor()
suite = TestLoader().loadTestsFromModule(sensorTester)
TextTestRunner().run(suite)
#hierbij wordt geken als er goede testData wordt gemaakt
# zodat ook de sensor goed virtueel getest kan worden


