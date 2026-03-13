from controle import *

tv = ControleRemoto()
while True:
    if not tv.ligado:
        print(tv.desligado())
        escolha = tv.menu()
        tv.quebrar_linha(100)
        if escolha == '0':
            break
        elif escolha == '@':
            tv.ligado = True
    else:
        print(tv.ligar())
        escolha = tv.menu()
        tv.quebrar_linha(100)
        if escolha == '0':
            break
        elif escolha == '@':
            tv.ligado = False
        elif escolha in '<>':
            tv.mudar_canal(escolha)
        elif escolha in '-+':
            tv.mudar_volume(escolha)