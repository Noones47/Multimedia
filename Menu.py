from main import *
from vid import *
from compressao import *
from audio import *

menu_options = {
    1: 'Audio',
    2: 'Video',
    3: 'Comressao',
    4: 'Imagem',
    5: 'Sair',
}
imagem_options = {
    1: 'Preto e Branco',
    2: 'Negativo',
    3: 'Adicionar',
    4: 'Subtrair',
    5: 'Or',
    6: 'Blue Filter',
    7: 'Voltar',
}
video_options = {
    1: 'Run',
    2: 'Voltar',

}
comp_options = {
    1: 'Resize',
    2: 'Cropping',
    3: 'Multipla Compressao',
    4: 'Voltar',

}
audio_options = {
    1: 'Concatenar',
    2: 'Sobrepor',
    3: 'LowPass',
    4: 'Highpass',
    5: 'Voltar',
}


def print_menu():
    for key in menu_options.keys():
        print(key, '--', menu_options[key])

    option = int(input('Escolha uma opcao: '))

    if option == 1:
        for key in audio_options.keys():
            print(key, '--', audio_options[key])
        option1 = int(input('Escolha uma opcao: '))

        if option1 == 1:
            soma()
        elif option1 == 2:
            multi()
        elif option1 == 3:
            lowpass()
        elif option1 == 4:
            highpass()
        elif option1 == 5:
            print_menu()

        else:
            print('Opcao Invalida!')

    elif option == 2:
        for key in video_options.keys():
            print(key, '--', video_options[key])
        option2 = int(input('Escolha uma opcao: '))

        if option2 == 1:
            mainvid()
        elif option2 == 2:
            print_menu()
        else:
            print('Opcao Invalida!')

    elif option == 3:
        for key in comp_options.keys():
            print(key, '--', comp_options[key])
        option3 = int(input('Escolha uma opcao: '))

        if option3 == 1:
            resize()
            print_menu()
        elif option3 == 2:
            cropping()
            print_menu()
        elif option3 == 3:
            multicompress()
            print_menu()
        elif option3 == 4:
            print_menu()
        else:
            print('Opcao Invalida!')

    elif option == 4:
        for key in imagem_options.keys():
            print(key, '--', imagem_options[key])
        option4 = int(input('Escolha uma opcao: '))

        if option4 == 1:
            blackwhite()
            print_menu()
        elif option4 == 2:
            negativo()
            print_menu()
        elif option4 == 3:
            add()
            print_menu()
        elif option4 == 4:
            sub()
            print_menu()
        elif option4 == 5:
            OR()
            print_menu()
        elif option4 == 6:
            blue()
            print_menu()
        elif option4 == 7:
            print_menu()

        else:
            print('Opcao Invalida!')

    elif option == 5:
        print('Adeus')
        exit()
    else:
        print('Opcao Invalida!')


print_menu()
