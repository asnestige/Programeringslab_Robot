from reflectance_sensors import ReflectanceSensors
from ultrasonic import Ultrasonic
from camera import Camera
from irproximity_sensor import IRProximitySensor

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

class IRProximity_sensob(Sensob):  # Nærhetssensor
    def __init__(self):
        super(IRProximity_sensob, self).__init__()
        self.sensors = [IRProximitySensor()]

    def update(self):
        self.value = self.sensors[0].update()
        print("IR", self.value)
        return self.value

class Reflectance(Sensob):  # Sensor under, sjekker farve
    def __init__(self):
        super(Reflectance, self).__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        self.value = sum(self.sensors[0].update())
        print("Reflectance", self.value)
        return self.value

class Ultrasonic_sensob(Sensob):  # Sjekker lyd, avstand forran
    def __init__(self):
        super(Ultrasonic_sensob, self).__init__()
        self.sensors = [Ultrasonic()]

    def update(self):
        for sensor in self.sensors:
            sensor.update()
        self.value = self.sensors[0].value
        print("Ultrasonic", self.value)
        return self.value

class Camera_sensob(Sensob):  # Kamera sansor
    def __init__(self):
        super(Camera_sensob, self).__init__()
        self.sensors = [Camera()]

    def rgb(self, img):
        rgb = [0, 0, 0]

        for x in range(40, 80):
            for y in range(40, 50):
                band = img.getpixel((x, y))
                rgb[0] += band[0]
                rgb[1] += band[1]
                rgb[2] += band[2]

        tot = sum(rgb)
        rgb[0] = rgb[0] / tot
        rgb[1] = rgb[1] / tot
        rgb[2] = rgb[2] / tot

        return rgb

    def update(self):
        self.value = self.rgb(self.sensors[0].update())
        print("Camera", self.value)
        return self.value
