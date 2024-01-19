import vertexai
from vertexai.preview.generative_models import GenerativeModel

class RAM:

    def __init__(self, context_window:int, processes:list, memory : str) -> None:
        self.context_window = context_window
        self.processes = processes
        self.memory = memory
        self.max_words = 24000
        self.available_words = self.max_words - self._count_words(memory)
        self.model = GenerativeModel('gemini-pro')
        self.max_tokens = 32768
        self.available_tokens = self.max_tokens - self._count_tokens(memory)

    def _count_words(self, text : str):
        return len(text.split())
    
    def _count_tokens(self, text : str):
        return self.model.count_tokens(text)
    

