from PySimpleGUI import PySimpleGUI as sg 

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário:'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha:'), sg.Input(key = 'senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Salvar Login')],
    [sg.Button('Entrar')]
]

layout2 = [
    [sg.Text('Seja Bem-vindo')]
]

#Janela
janela = sg.Window('Tela de Login', layout)
entrar = sg.Window('Seja Bem-vindo(a)', layout2)
#Ler os eventos
while True:
    eventos, valores = janela.read()
    eventos2 = entrar.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'pri' and valores['senha'] == '152342':
            print(eventos2)
            