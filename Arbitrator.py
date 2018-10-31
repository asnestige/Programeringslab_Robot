from Behavior import Behavior

class Arbitrator:

    def __init__(self):
        pass

    """return a tuple containing:
        motor recommendations (one per motob) to move the robot
        a boolean indicating whether or not the run should be halted
    """
    def choose_action(self, behaviors):
        right_behavior = None
        max_weight = -1

        #Velger riktig oppførsel og sender dens motob anbefaling til Bbcon
        for behavior in behaviors:
            if behavior.weight > max_weight:
                max_weight = behavior.weight
                right_behavior = behavior

        return right_behavior.motor_recommendations, right_behavior.halt_request
