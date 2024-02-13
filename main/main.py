from text.response_text import ResponseText
from voice import response_voice
from image import response_image

voice = response_voice
text = ResponseText()
image = response_image


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
    # TODO: EM CONSTRUÇÃO
    # elif input_type_chosen == 3:
    #     image.responseGeminai(output)
    else:
        print('Entrada inválida')


input_type = int(input('Selecione o tipo de entrada:\n1 - Texto\n2 - Voz\n3 - Imagem\n'))
main(input_type)
