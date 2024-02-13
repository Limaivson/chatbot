import google.generativeai as genai
from api_key import read_key


class ResponseText:
    def __init__(self):
        self.api_key = read_key.get_api_key()
        self.genai = genai.configure(api_key=f'{self.api_key}')
        self.model = genai.GenerativeModel('gemini-pro')

    def responseGeminai(self, text):
        response = self.model.generate_content(str(text))
        return response.text
