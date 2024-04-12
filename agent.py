

class Agent():

    '''
    The Agent class is the base class for all the agents
    '''

    def __init__(self, config):

        self.name = config.name
        self.role = config.role
        