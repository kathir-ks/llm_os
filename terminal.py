import os


class Terminal():

    '''
    A python class for interaction with the terminal
    '''

    def __init__(self):
        self.current_dir = os.getcwd()

    def change_dir(self, new_dir):
        assert os.path.exists(new_dir), "The directory does not exist"
        os.chdir(new_dir)
        self.current_dir = os.getcwd()

    def list_dir(self):
        return os.listdir(self.current_dir)
    
    def execute_command(self, command):
        os.system(command)