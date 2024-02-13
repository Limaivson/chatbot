import google.generativeai as genai
import PIL.Image
from api_key import read_key


class ResponseImage:
    def __init__(self):
        self.api_key = read_key.get_api_key()
        self.genai = genai.configure(api_key=f'{self.api_key}')
        self.model = genai.GenerativeModel('gemini-pro-vision')

    def read_image(self, image_path, message):
        image = PIL.Image.open(f'/Users/Ivson/Documents/GitHub/chatbot/image/imgs/car.jpeg')
        response = self.model.generate_content([message, image])
        response.resolve()
        return response.text
