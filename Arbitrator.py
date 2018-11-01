from Behavior import Behavior


class Arbitrator:

    def __init__(self):
        pass

    #Vi bruker deterministisk oppførsel
    #hver av de regner ut sin egen vekt og vi velger den som "sier den er viktigst"
    def choose_action(self, behaviors):
        maximum_weight = 0
        chosen_behavior = None

        #Velger riktig oppførsel og sender dens motob anbefaling til Bbcon
        for behavior in behaviors:
            if behavior.weight >= maximum_weight:
                maximum_weight = behavior.weight
                chosen_behavior = behavior
        #Return tuple containing motor recommendations and a boolean if it should halt or not. 
        return (chosen_behavior.motor_recommendations, chosen_behavior.halt_request)
