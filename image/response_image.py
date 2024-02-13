import google.generativeai as genai
import PIL.Image
from api_key import read_key


class ResponseImage:
    def __init__(self, image_path, message=''):
        self.api_key = read_key.get_api_key()
        self.genai = genai.configure(api_key=f'{self.api_key}')
        self.model = genai.GenerativeModel('gemini-pro-vision')
        self.image_path = image_path
        self.image = PIL.Image.open(f'images/{self.image_path}.jpg')
        self.message = message

    def read_image(self):
        response = self.model.generate_content([self.message, self.image])
        return response.resolve()
