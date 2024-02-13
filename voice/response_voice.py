import google.generativeai as genai
import pyttsx3
import speech_recognition as sr


class ResponseVoice:
    def __init__(self):
        self.genai = genai.configure(api_key='api_key')
        self.model = genai.GenerativeModel('gemini-pro')
        self.chat = self.model.start_chat(history=[])
        self.assistant = True
        self.microphone = True

    def read_voice(self):
        global mic, r, engine
        if self.assistant:
            engine = pyttsx3.init()

            voices = engine.getProperty('voices')
            engine.setProperty('rate', 180)

            for index, voice in enumerate(voices):
                print(index, voice.name)

            voice = 1
            engine.setProperty('voice', voices[voice].id)

        if self.microphone:
            r = sr.Recognizer()
            mic = sr.Microphone()

        bem_vindo = "Bem vindo ao Gemini!"
        print("")
        print(len(bem_vindo) * "#")
        print(bem_vindo)
        print(len(bem_vindo) * "#")
        print("###   Digite 'desligar' para encerrar    ###")
        print("")

        while True:
            if self.microphone:
                with mic as fonte:
                    r.adjust_for_ambient_noise(fonte)
                    print("Fale alguma coisa (ou diga 'desligar')")
                    audio = r.listen(fonte)
                    print("Enviando para reconhecimento")
                    try:
                        texto = r.recognize_google_cloud(audio, language="pt-BR")
                        print("Você disse: {}".format(texto))
                    except Exception as e:
                        print("Não entendi o que você disse. Erro", e)
                        texto = ""
            else:
                texto = input("Escreva sua mensagem (ou #sair): ")

            if texto.lower() == "desligar":
                break

            response = self.chat.send_message(texto)
            print("Gemini:", response.text, "\n")

            if self.assistant:
                engine.say(response.text)
                engine.runAndWait()
