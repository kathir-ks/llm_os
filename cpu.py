from file_system import FileSystem
from llm import Model

class CPU:
    
    def __init__(self, file_system : FileSystem, llm : Model, ram) -> None:
        self.file_system = file_system
        self.llm = llm
        self.ram = ram