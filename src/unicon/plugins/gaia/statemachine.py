from unicon.statemachine import Path, State, StateMachine
from .patterns import GaiaPatterns

g = GaiaPatterns()

class GaiaStateMachine(StateMachine):

    def __init__(self, hostname=None):
        super().__init__(hostname)

    def create(self):
        '''
        statemachine class's create() method is its entrypoint. This showcases
        how to setup a statemachine in Unicon. 
        '''
        #super().create()

        clish = State("enable", g.clish_prompt)
        #enabled = State("enable", g.clish_prompt)
        self.add_state(clish)
        #self.add_state(enabled)