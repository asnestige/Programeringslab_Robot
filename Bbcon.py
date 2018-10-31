class Bbcon:

    def __init__(self):
        self.behaviors = []  #list of all the behavior objects used by the bbcon
        self.active_behaviors = [] # list of all behaviors that are currently active
        self.sensobs = [] # list of all sensory objects used by the bbcon
        self.motobs = [] #list of all motor objects used by the bbcon
        self.arbitrator = None #the arbitrator object that will resolve actuator requests produced by the behaviors.








Other instance variables, such as the current timestep, the inactive behaviors, and the controlled agent/robot
may also prove useful in your implementation.
The method set for BBCON should include the following simple procedures:
1. add behavior - append a newly-created behavior onto the behaviors list.
2. add sensob - append a newly-created sensob onto the sensobs list.
3. activate behavior - add an existing behavior onto the active-behaviors list.
4. deactive behavior - remove an existing behavior from the active behaviors list.
In addition, BBCON must include a method named run one timestep, which constitutes the core BBCON
activity. It should perform (at least) the following actions on each call:
1. Update all sensobs - These updates will involve querying the relevant sensors for their values, along
with any pre-processing of those values (as described below)
2. Update all behaviors - These updates involve reading relevant sensob values and producing a motor
recommendation.
3. Invoke the arbitrator by calling arbitrator.choose action, which will choose a winning behavior and
return that behavior’s motor recommendations and halt request flag.
4. Update the motobs based on these motor recommendations. The motobs will then update the settings
of all motors.
5. Wait - This pause (in code execution) will allow the motor settings to remain active for a short period
of time, e.g., one half second, thus producing activity in the robot, such as moving forward or turning.
6. Reset the sensobs - Each sensob may need to reset itself, or its associated sensor(s), in some way.

