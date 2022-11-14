from unittest import *
import io
import seaborn as sns
import matplotlib.pyplot as plt
import PID
import Sensor
import Simulation


class TestingSensor(TestCase):
    def setUp(self):
        self.out = io.StringIO()
    def testdummydata(self):
        x = 1900
        y = Sensor.readSensor(0, Sensor.createTesData( x))
        self.assertEqual(x , y, "data not correct")

    def testdummyLowBit(self):
        x = 100
        y = Sensor.readSensor(0, Sensor.createTesData(x))
        self.assertEqual(x, y, "data not correct")

    def testdummyZero(self):
        x = 0
        y = Sensor.readSensor(0, Sensor.createTesData(x))
        self.assertEqual(x, y, "data not correct")



sensorTester = TestingSensor()
suite = TestLoader().loadTestsFromModule(sensorTester)
TextTestRunner().run(suite)
#hierbij wordt geken als er goede testData wordt gemaakt
# zodat ook de sensor goed virtueel getest kan worden


