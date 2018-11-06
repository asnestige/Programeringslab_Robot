from reflectance_sensors import ReflectanceSensors
from ultrasonic import Ultrasonic
from camera import Camera
from irproximity_sensor import IRProximitySensor



class Sensob:  # Superklasse
    def __init__(self):
        self.sensors = []
        self.value = None

    def update(self):  # Henter ut relevant verdi fra sensor og omgjor de til en verdi
        pass

    def get_value(self):  # Returnerer verdien
        return self.value

    def reset(self):  # For hver sensor resettes de
        for sensor in self.sensors:
            sensor.reset()


class IRProximity_sensob(Sensob):  # Nærhetssensor
    def __init__(self):
        super(IRProximity_sensob, self).__init__()
        self.sensors = [IRProximitySensor()]

    def update(self):
        self.value = self.sensors[0].update()
        print("IRProximity", self.value)
        return self.value


class Reflectance_sensob(Sensob):  # Sensor under, sjekker farve
    def __init__(self):
        super(Reflectance_sensob, self).__init__()
        self.sensors = [ReflectanceSensors()]

    def update(self):
        self.value = sum(self.sensors[0].update())
        print("Infrared_belly", self.value)
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

    def update(self):
        self.value = self.rgb(self.sensors[0].update())
        print("Camera", self.value)
        return self.value

    def rgb(self, image):
        rgb = [0, 0, 0]

        for i in range(40, 80):
            for j in range(40, 50):
                band = image.getpixel((i, j))
                rgb[0] = rgb[0] + band[0]
                rgb[1] = rgb[1] + band[1]
                rgb[2] = rgb[2] + band[2]

        total = sum(rgb)
        rgb[0] = rgb[0] / total
        rgb[1] = rgb[1] / total
        rgb[2] = rgb[2] / total
        return rgb

