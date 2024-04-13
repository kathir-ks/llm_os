from terminal import Terminal

class Agent():

    '''
    The Agent class is the base class for all the agents
    '''

    def __init__(self, config):

        self.name = config.name
        self.role = config.role
        self.llm_config = config.llm
        self.llm = llm(self.llm_config)
        self.instructions = config.instructions
        self.terminal = Terminal()
        self.instrution_prompt = f"Your are an agent named {self.name}. Your role is {self.role}.Follow the instructions below. {self.instructions}"
    
    def task(self, task):
        
        steps = llm.generate(self.instrution_prompt + f"Generate step by step task for the given task below. ###Task: {task}")

        for step in steps:
            pass
            