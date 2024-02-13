from text.response_text import ResponseText
from voice import response_voice
from image import response_image

voice = response_voice
text = ResponseText()
image = response_image


def main(input_type_chosen):
    if input_type_chosen == 1:
        message = input(print('O que você deseja?'))
        print(text.responseGeminai(message))
    # TODO: EM CONSTRUÇÃO
    # elif input_type_chosen == 2:
    #     voz = input(print('Fale o que você deseja'))
    #     voice.responseGeminai(voz)
    # TODO: EM CONSTRUÇÃO
    # elif input_type_chosen == 3:
    #     image.responseGeminai(output)
    else:
        print('Entrada inválida')


input_type = int(input(print('Selecione o tipo de entrada:\n1 - Texto\n2 - Voz\n3 - Imagem')))
main(input_type)
