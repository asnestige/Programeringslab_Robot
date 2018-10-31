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








