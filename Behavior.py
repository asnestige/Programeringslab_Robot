from Sensob import *

class Behavior:
    def __init__(self, bbcon):
        self.bbcon = bbcon
        self.sensobs = [] #alle sensobs som behavior bruker
        self.motor_recommendations = [] #en recommendation per motob, som behavior gir til arbitrator
        self.active_flag = False #indikerer om om behavior er aktiv/inaktiv
        self.halt_request = False #forespør om robot skal stanse
        self.priority = 0 #definerer betydningen av denne oppførselen
        self.match_degree = 0 #verdi mellom [0,1]:grad nåværende tilstand garanterer utførelsen av denne oppførselen
        self.weight = self.match_degree*self.priority


    #når behavior er aktiv, skal det testes om den skal være inaktiv
    #implementers i subklasse
    def consider_deactivation(self):
        pass

    #når behavior er inaktiv, skal det testes om den skal være aktiv
    #implementers i subklasse
    def consider_activation(self):
        pass

    #hovedaksjon i behavior
    #bruker info fra sensob for å lage motob recommendations (og halt requests)
    def sense_and_act(self):
        pass


    def update(self):
    # oppdaterer aktivitetsstatus
        if self.active_flag:
            self.consider_deactivation()
        else:
            self.consider_activation()

        self.sense_and_act()

        self.weight = self.match_degree * self.priority

class Dont_collide(Behavior):  # IR-Sensor og Ultrasonic, Sensor 2 og 3
    def __init__(self, ultrasonic, ir):
        super(Dont_collide, self).__init__(None)
        self.sensobs = [ultrasonic, ir]
        self.priority = 3

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        dist = self.sensobs[0].get_value()

        reflect = self.sensobs[1].get_value()

        self.match_degree = 0
        self.motor_recommendations = None

        if reflect[0] is True:
            self.match_degree = 1
            self.motor_recommendations = [[1, -0.5]]  # Høyre snu
        elif reflect[1] is True:
            self.match_degree = 1
            self.motor_recommendations = [[-0.5, 1]]  # Venstre snu
        elif dist < 10:
            self.match_degree = 1
            self.motor_recommendations = [[-0.5, 1]]

class Drive(Behavior): # Kjøre frem, ingen sensor
    def __init__(self):
        super(Drive, self).__init__(None)
        self.priority = 1 #lavest pri

    def consider_activation(self):
        self.active_flag = True

    def consider_deactivation(self):
        self.active_flag = True

    def sense_and_act(self):
        self.match_degree = 1
        self.motor_recommendations = [[0.5, 0.5]]  #Sender recommendations om at den skal kjøre 


class Stop(Behavior):  # Camera-sensor, Sensor 1
    def __init__(self, camera):
        super(Stop, self).__init__(None)
        self.sensobs = [camera]
        self.priority = 4 #Stop har den høyeste prioriteten 
        self.stopped = False  # Starter som false, da kjører den

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        rgb = self.sensobs[0].value
                          
        self.match_degree = 0

        if self.stopped:
            self.match_degree = 1
            if rgb[1] < 0.95:  #Lysere farger
                self.match_degree = 0
                self.stopped = False
                self.motor_recommendations = [[0.5, 0.5]] #Dersom det er en lysere farge, kan roboten kjøre igjen 

        elif rgb[1] > 0.95:  #Rød og mørke farger
            self.stopped = True  # Stopper
            self.match_degree = 1
            self.motor_recommendations = [[0, 0]] #Sender recommendations om å stoppe
