from config import Config
import camera_sensob


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

class Avoid_collisions(Behavior):  # Endre denne
    def __init__(self, distance, ir):
        super(Avoid_collisions, self).__init__(None)
        self.sensobs = [distance, ir]

        self.priority = Config['collisionPri']

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        dist = self.sensobs[0].get_value()

        reflect = self.sensobs[1].get_value()

        self.match_degree = 0
        self.motor_recommendations = None

        if reflect > Config['reflectThr'] or dist < Config['minDist']:
            self.match_degree = 1
            self.motor_recommendations = Config['J_turn']

class Go(Behavior): # Endre denne
    def __init__(self):
        super(Go, self).__init__(None)
        self.priority = Config['goPri']

    def consider_activation(self):
        self.active_flag = True

    def consider_deactivation(self):
        self.active_flag = True

    def sense_and_act(self):
        self.match_degree = 1
        self.motor_recommendations = Config['forward']


class StopSign(Behavior): # Endre denne
    def __init__(self, camera):
        super(StopSign, self).__init__(None)
        self.sensobs = [camera]

        self.priority = Config['stopSignPri']

        self.stopped = False

    def consider_deactivation(self):
        self.active_flag = True

    def consider_activation(self):
        self.active_flag = True

    def sense_and_act(self):
        rgb = self.sensobs[0].value

        self.match_degree = 0
        self.motor_recommendations = Config['stop']

        if self.stopped:
            self.match_degree = 1
            if rgb[1] > Config['grThr']:
                self.match_degree = 0
                self.stopped = False

        elif rgb[0] > Config['redThr']:
            self.stopped = True
            self.match_degree = 1