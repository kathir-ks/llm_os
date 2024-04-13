from dataclasses import dataclass

@dataclass
class llm_config:

    '''
    The llm_config class is the base class for all the llm configurations
    '''

    model_name: str
    open_source: bool


class llm():

    '''
    The llm class is the base class for all the llm models
    '''
    def __init__(self, config : llm_config):

        self.config = config
        self.model_name = config.model_name
        self.open_source = config.open_source
        self.__init__llm__(self, config)

    def __init__llm__(self, config : llm_config):
        
        if self.model_name == 'gemini-pro':
            try:
                    import google.generativeai as genai
                    gemini_api_key = get_from_env("GEMINI_API_KEY")
                    genai.configure(api_key=gemini_api_key)
                    self.model = genai.GenerativeModel(self.model_name)
                    self.tokenizer = None
                
            except:
                    raise ImportError(
                            "Could not import google.generativeai python package. "
                            "Please install it with `pip install google-generativeai`."
                        )    
            
    def generate(self, text):
         outputs = self.model.generate_content(
            text
        )
         try:
            return outputs.candidates[0].content.parts[0].text
         
         except IndexError:
              return f"Could not generate content for the given text: {text}"
    