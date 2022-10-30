from criptografia import *
import PySimpleGUI as sg
import tkinter as tk

def janela_login():
    sg.theme('Reddit')
    layout = [
        [sg.Text('Nº de usuario')],
        [sg.Input(enable_events=True, key='num_usuario',)],
        [sg.Text('USUARIO')],
        [sg.Input(key='USUARIO',)],
        [sg.Text('SENHA')],
        [sg.Input(key='SENHA', password_char='*')],
        [sg.Button('Login'),  sg.Button('Sair')],
        [sg.Text('', key='aviso')]
    ]
    return sg.Window('login', layout=layout, finalize=True)

def janela_registro():
    sg.theme('Reddit')
    layout_registro = [
        [sg.Text('NOVO USUARIO')],
        [sg.Text('Codigo de usuario: '), sg.Text(lista_num_usuario+1)],
        [sg.Text('Nome de usuario')],
        [sg.Input(key='USUARIO_n')],
        [sg.Text('SENHA (minimo 6 digitos)')],
        [sg.Input(key='SENHA', password_char='*')],
        [sg.Text('Confirmar senha')],
        [sg.Input(key='conf_senha', password_char='*')],
        [sg.Button('REGISTRAR'), sg.Button('Voltar ao menu')],
        [sg.Text('', key='aviso2')]
    ]
    return sg.Window('registrar', layout=layout_registro, finalize=True)

def janela_menu():
    sg.theme('Reddit')
    layout_menu = [
        [sg.Button('Enviar mensagem')],
        [sg.Button('Mensagens enviadas')],
        [sg.Button('Mensagens recebidas')],
        [sg.Button('Novo usuario')],
        [sg.Button('Voltar ao login')]
    ]
    return sg.Window('menu', layout=layout_menu, finalize=True)

def janela_menssagem():
    sg.theme('Reddit')
    layout_mensagem = [
        [sg.Text ('Mensagem:'), sg.Text(count_mensagem+1)],
        [sg.Input(key="mensagem_original")],
        [sg.Text('Informe o nome do remetente :')],
        [sg.Input(key='cod_nome')],
        [sg.Button('Enviar mensagem')],
        [sg.Text('', key='aviso3')],
        [sg.Button('Voltar')]

    ]
    return sg.Window('mensagem', layout=layout_mensagem, finalize=True)

def janela_enviados():
    sg.theme('Reddit')
    layout_enviados = [
        [sg.Text('Enviados')],
        [sg.Text('Informe o número da mensagem:')],
        [sg.Input(key='num_m', enable_events=True)],
        [sg.Button('Confirmar')],
        [sg.Button('Voltar ao menu')],
        [sg.Text('', key='aviso4')]

    ]
    return sg.Window('enviados', layout=layout_enviados, finalize=True)

def janela_recebidos():
    sg.theme('Reddit')
    layout_recebidos = [
        [sg.Text('Recebidos')],
        [sg.Button('Visualuizar nº')],
        [sg.Text('Informe o número da mensagem:')],
        [sg.Input(key='num_mr', enable_events=True)],
        [sg.Button('Confirmar vizualização')],
        [sg.Button('Retornar ao menu')],
        [sg.Text('', key='aviso5')]
    ]
    return sg.Window('recebidos', layout=layout_recebidos, finalize=True)

def janela_vizualiza_r():
    sg.theme('Reddit')
    layout_vizualizar = [
        [sg.Text(dicionario_recebido_vinculo.items())],
        [sg.Text('Digite a mensagem vinculada com seu Usuario')],
        [sg.Button('OKAY')]
    ]
    return sg.Window('vinculo', layout= layout_vizualizar, finalize=True)

#AÇÕES // variaveis
janela1, janela2, janela3, janela4 = janela_login(), None, None, None
cripto = ('', '', '')

#dicionario mensagens
count_mensagem = 0
dicionario_enviados = {count_mensagem: ""}
dicionario_chave1 = {count_mensagem: 0}
dicionario_chave2 = {count_mensagem: 0}

#Dicionario usuarios
n_dicionario_nome_senha = 1
lista_num_usuario = 1
n_login = 1
dicionario_nome = {n_dicionario_nome_senha: 'root'}
dicionario_senha = {n_dicionario_nome_senha: 'mestre123'}
dicionario_enviado_vinculo = {n_login: count_mensagem}
nome_remetente = ' '
dicionario_recebido_vinculo = {nome_remetente: count_mensagem}

while True:
    window, event, values = sg.read_all_windows()

    # janela login #
    if window == janela1 and event == sg.WIN_CLOSED:
        break

    if window == janela1 and event == 'Sair':
        break

    if event == 'num_usuario' and len(values['num_usuario']) and values['num_usuario'][-1] not in ('0123456789'):
        window['num_usuario'].update(values['num_usuario'][:-1])

    if event == 'Login':
        if values['num_usuario'] != '':
            n = int(values['num_usuario'])
            for k in dicionario_nome.keys():
                if n == k:
                    if values['USUARIO'] == dicionario_nome[n] and values['SENHA'] == dicionario_senha[n]:
                        janela1.hide()
                        janela2 = janela_menu()
                        window['USUARIO'].update('')
                        window['SENHA'].update('')
                        window['aviso'].update('')
                        window['num_usuario'].update('')
                        n_login = n
                        nome_user = values['USUARIO']
                    else:
                        window['aviso'].update('Invalido')
                else:
                    window['aviso'].update('Invalido')
        else:
            window['aviso'].update('Verifique os campos')

    # janela menu

    if window == janela2 and event == sg.WIN_CLOSED:
        janela2.hide()
        janela1.un_hide()

    if window == janela2 and event == 'Enviar mensagem':
        janela3 = janela_menssagem()
        janela2.hide()

    if window == janela2 and event == 'Mensagens enviadas':
        janela3 = janela_enviados()
        janela2.hide()

    if window == janela2 and event == 'Mensagens recebidas':
        janela3 = janela_recebidos()
        janela2.hide()

    if window == janela2 and event == 'Novo usuario':
        janela3 = janela_registro()
        janela2.hide()

    if window == janela2 and event == 'Voltar ao login':
        janela2.hide()
        janela1.un_hide()


    # janela mensagem

    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == sg.WIN_CLOSED:
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Enviar mensagem':
        if values["mensagem_original"] != '':
            if values['cod_nome'] != '':
                for v in dicionario_nome.values():
                    if values['cod_nome'] == v:
                        rsa(values["mensagem_original"])
                        cripto = rsa(values["mensagem_original"])
                        sg.popup('Mensagem nº:', count_mensagem + 1, 'conteudo:', cripto[0], 'enviada com sucesso!')
                        dicionario_enviados[count_mensagem] = cripto[0]
                        dicionario_chave1[count_mensagem] = cripto[1]
                        dicionario_chave2[count_mensagem] = cripto[2]
                        dicionario_enviado_vinculo[n_login] = count_mensagem
                        nome_remetente = values['cod_nome']
                        dicionario_recebido_vinculo[nome_remetente] = count_mensagem
                        count_mensagem += 1
                        window["mensagem_original"].update("")
                        window['cod_nome'].update("")
                        window['aviso3'].update('')
                        janela3.hide()
                        janela2.un_hide()
                    else:
                        window['aviso3'].update('Remetente invalido')
            else:
                window['aviso3'].update('Informe remetente')
        else:
             window['aviso3'].update('Inválido')

    # janela_enviados

    if window == janela3 and event == sg.WIN_CLOSED:
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Voltar ao menu':
        janela3.hide()
        janela2.un_hide()

    if event == 'num_m' and len(values['num_m']) and values['num_m'][-1] not in ('0123456789'):
        window['num_m'].update(values['num_m'][:-1])


    if window == janela3 and event == 'Confirmar':
        if values['num_m'] != '':
            n_men_ev = int(values['num_m']) - 1
            for k in dicionario_enviados.keys():
                if n_men_ev == k:
                    for k, v in dicionario_enviado_vinculo.items():
                        print(k, v)
                    if n_login == k and n_men_ev == v:
                        decifrar(dicionario_enviados[n_men_ev], dicionario_chave1[n_men_ev],
                                     dicionario_chave2[n_men_ev])
                        mostra = decifrar(dicionario_enviados[n_men_ev], dicionario_chave2[n_men_ev],
                                              dicionario_chave1[n_men_ev])
                        sg.popup('Enviados: ', mostra)
                    else:
                        window['aviso4'].update('Nº de mensagem invalida ')
                else:
                    window['aviso4'].update('Nº de mensagem invalida ')
        else:
            window['aviso4'].update('Nº de mensagem invalida ')

    #janela recebidos
    if window == janela3 and event == sg.WIN_CLOSED:
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Retornar ao menu':
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Visualuizar nº':
        janela4 = janela_vizualiza_r()

    if window == janela4 and event == 'OKAY':
        janela4.hide()




    if event == 'num_mr' and len(values['num_mr']) and values['num_mr'][-1] not in ('0123456789'):
        window['num_mr'].update(values['num_mr'][:-1])

    if window == janela3 and event == 'Confirmar vizualização':
        if values['num_mr'] != '':
            n_men_ev = int(values['num_mr']) - 1
            for v in dicionario_recebido_vinculo.values():
                if n_men_ev == v:
                    for k, v in dicionario_recebido_vinculo.items():
                        print(k, v)
                    if nome_user == k and n_men_ev == v:
                        decifrar(dicionario_enviados[n_men_ev], dicionario_chave1[n_men_ev],
                                     dicionario_chave2[n_men_ev])
                        mostra = decifrar(dicionario_enviados[n_men_ev], dicionario_chave2[n_men_ev],
                                              dicionario_chave1[n_men_ev])
                        sg.popup('Enviados: ', mostra)
                    else:
                        window['aviso5'].update('Nº de mensagem invalida ')
                else:
                    window['aviso5'].update('Nº de mensagem invalida ')
        else:
            window['aviso5'].update('Nº de mensagem invalida ')




# janela_registro

    if window == janela2 and event == sg.WIN_CLOSED:
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'Voltar ao menu':
        janela3.hide()
        janela2.un_hide()

    if window == janela3 and event == 'REGISTRAR':
        for v in dicionario_nome.values():
            print(v)
        if values['USUARIO_n'] != v:
            if values['SENHA'] == values['conf_senha']:
                if len(values['SENHA']) > 5:
                    lista_num_usuario += 1
                    n_dicionario_nome_senha += 1
                    dicionario_nome[n_dicionario_nome_senha] = values['USUARIO_n']
                    dicionario_senha[n_dicionario_nome_senha] = values['SENHA']
                    window['SENHA'].update('')
                    window['USUARIO_n'].update('')
                    window['conf_senha'].update('')
                    janela3.hide()
                    janela2.un_hide()
                else:
                    sg.popup_error('Número de caracteres minimo não atendido')
            else:
                sg.popup_error('Senhas não conferem')
        else:
            sg.popup_error('Nome já ultilizado')



