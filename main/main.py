from text.response_text import ResponseText
from voice import response_voice
from image.response_image import ResponseImage

voice = response_voice
text = ResponseText()
image = ResponseImage()


def main(input_type_chosen):
    if input_type_chosen == 1:
        message = ''
        while message != '0':
            if message == '':
                message = input('Digite 0 para parar a conversa\nVocê: ')
                if message == '0':
                    break
                print(f'Gemini: {text.responseGeminai(message)}')
            else:
                message = input('Você: ')
                print(f'Gemini: {text.responseGeminai(message)}')
    # TODO: EM CONSTRUÇÃO
    # elif input_type_chosen == 2:
    #     voz = input(print('Fale o que você deseja'))
    #     voice.responseGeminai(voz)
    elif input_type_chosen == 3:
        image_path = ''
        print('Digite 0 para parar a conversa\nou')
        while image_path != '0':
            image_path = input('Digite o nome da imagem que deseja usar:\n')
            if image_path == '0':
                break
            message = input('O que deseja que o gemini faça com a imagem?\n')
            print(f'Gemini: {image.read_image(image_path, message)}')
    else:
        print('Entrada inválida')


input_type = int(input('Selecione o tipo de entrada:\n1 - Texto\n2 - Voz\n3 - Imagem\n'))
main(input_type)
