from reflectance_sensors import ReflectanceSensors
from ultrasonic import Ultrasonic

class Sensob:

    def __init__(self):
        self.sensors = []
        self.value = None

    def update(self):
        # Fetch relevant sensor value(s) and convert them into one value
        return

    def get_value(self):
        return self.value

    def reset(self):
        for sensor in self.sensors:
            sensor.reset()


class IRProximity_sensob(Sensob):  #FRA JONAS
    def __init__(self):
        super(IRProximity_sensob, self).__init__()
        self.sensors = [IRProximitySensor()]

    def update(self):
        self.value = self.sensors[0].update()
        print("IR", self.value)
        return self.value

class Reflectance(Sensob): #FRA JONAS
    def __init__(self):
        super(Reflectance, self).__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        self.value = sum(self.sensors[0].update())
        print("Reflectance", self.value)
        return self.value

class Ultrasonic_sensob(Sensob): #FRA JONAS
    def __init__(self):
        super(Ultrasonic_sensob, self).__init__()
        self.sensors = [Ultrasonic()]

    def update(self):
        for sensor in self.sensors:
            sensor.update()
        self.value = self.sensors[0].value
        print("Ultrasonic", self.value)
        return self.value
