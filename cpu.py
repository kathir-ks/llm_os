from file_system import FileSystem
from llm import Model
import google.generativeai as genai
from ram import RAM
from process import Process

class Cpu:
    
    def __init__(self, file_system : FileSystem,ram : RAM) -> None:
        self.file_system = file_system
        self.model = genai.GenerativeModel('gemini-pro')
        self.ram = ram

    def countTokens(self,text : str) -> int:
        return self.model.count_tokens(str)
    
    def freeRAMSpace(self) -> int:
        text = ""
        for instruction in self.ram.instructions:
            text += instruction
        return self.countTokens(text)
    
    def execute(self, process : Process):
        response = self.model.generate_content(process.instructions)
        
    
    