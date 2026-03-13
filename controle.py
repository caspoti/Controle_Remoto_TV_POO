from rich import print
from rich.panel import Panel

class ControleRemoto:
    """
    Cria um controle remoto que recebe canais e volume
    """
    def __init__(self):
        self.canal = 1
        self.volume = 1
        self.ligado = False
        self.volumes = f'[on green]   [/][on white]        [/]'

    def desligado(self):
        """
        Cria um painel para mostrar quando a TV está desligada
        :return: painel
        """
        painel = Panel('[red]A TV está desligada[/]', title='TV',width=30)
        return painel

    def ligar(self):
        """
        Cria um painel para mostrar a TV ligada
        :return: painel
        """
        painel = Panel(f'Canal {self.mostrar_canais()}\n'
                       f'Volume {self.mostrar_volumes()}',title='TV',width=30)
        return painel

    def mostrar_canais(self):
        """
        Cria uma lista que mostra os canais e canal atual
        :return: ' '.join(canais)
        """
        canais = []
        for i in range(1, 6):
            if i == self.canal:
                canais.append(f'[on yellow] {self.canal} [/]')
            else:
                canais.append(f' {i} ')
        return ' '.join(canais)

    def mudar_canal(self, c):
        """
        Muda de canal selecionado: Avança ou retorna o canal conforme possivel.
        :param c: Recebe '<' para voltar canal, '>' para avançar canal
        :return: None
        """
        if c == '>':
            if 1 <= self.canal < 5:
                self.canal += 1
            return None
        elif c == '<':
            if 1 < self.canal <= 5:
                if self.canal == 2:
                    self.canais = f'[on yellow] 1 [/]  2   3   4   5 '
                    self.canal -= 1
                elif self.canal == 3:
                    self.canais = f' 1  [on yellow] 2 [/]  3   4   5 '
                    self.canal -= 1
                elif self.canal == 4:
                    self.canais = f' 1   2  [on yellow] 3 [/]  4   5 '
                    self.canal -= 1
                else:
                    self.canais = f' 1   2   3  [on yellow] 4 [/]  5 '
                    self.canal -= 1
        return None

    def mostrar_volumes(self):
        """
        Cria uma lista que mostra os volumes
        :return: ''.join(volumes)
        """
        volumes = []
        for c in range(1, 6):
            if c == self.volume:
                volumes.append(f'[on green]  [/]')
            else:
                volumes.append(f'[on white]  [/]')
        return ''.join(volumes)

    def mudar_volume(self,v):
        """
        Altera o volume: '+' para aumentar e '-' para diminuir
        :param v: '+' para aumentar e '-' para diminuir
        :return: None
        """
        if v == '+':
            if 1 <= self.volume < 5:
                self.volume += 1
            return None
        elif v == '-':
            if 1 < self.volume <= 5:
                self.volume -= 1
        return None

    def menu(self):
        """
        Aparece um menu de escolha para alterar canal e volume
        :return: A escolha do usuario
        """
        s = str(input(f'< CH{self.canal} >  - Volume {self.volume} + '))
        return s

    def quebrar_linha(self,n):
        """
        Quebra a linha o número de vezes desejada
        :param n: número de vezes que quebra linha
        :return: None
        """
        for c in range(1,n):
            print('\n')

