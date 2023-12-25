"""Página Montagem do Tabulheiro (Ilha) do jogo Ilha Proibida Equipe Fogo.

.. codeauthor:: Fernanda Araujo <fernandacsaraujo@gmail.com>
.. codeauthor::  Finn Kockelke <finn_kockelke@gmx.net>
.. codeauthor:: Vanessa M Vianna <vanmvianna@gmail.com>
.. codeauthor:: Anderson Amorim da Silva <anderson.amorix@gmail.com>

Changelog
---------
.. versionadded::    5.12
    montagem do tabuleiro.

.. versionadded::    23.11
    criação da ilha.py.

.. versionadded::    21.12
    criação da Carta de Troca de Terrenos

"""
from browser import window
import javascript
import random

NOMES = list(map(lambda x: x.replace("_", " "), ("PISTA_POUSO PORTAO_BRONZE PALACIO_CORAL VALE_TENEBROSO PORTAO_OURO PORTAO_PRATA PORTAO_COBRE "
         "PORTAO_FERRO ATALAIA JARDIM_SUSSUROS JARDIM_UIVOS TEMPLO_SOL "
         "TEMPLO_LUA CAVERNA_LAVA CAVERNA_SOMBRAS OBSERVATORIO PANTANO_BRUMAS ROCHA_FANTASMA "
         "PALACIO_MARES PENEDO_BALDIO BOSQUE_CARMESIM DUNAS_ENGANO PONTE_SUSPENSA LAGOA_PERDIDA").split()))

LINKS = ("CU3TLYh BL6lB7H tLDbzd2 OZE1myn J6ow4jR v0g7eGm 45aU3nf "
"yKU6ngz sdJ4W5O pjVcyoy ZNuPWqZ O0OSVFt "
"J160xpm 2j1IAyf b4xtltc E9MflTP NDioDZg TCmLjeT "
"rYxQaTa MvN7kTU Uni02EK cG5UYCf GC8V8CQ 7o1qq10").split()

__TABLE_SPACES__ = 21


class IlhaProibida:
    """
    Classe principal que representa o jogo Ilha Proibida.
    """

    def __init__(self, jogadores=None):
        """
        Inicializa a instância do jogo Ilha Proibida.

        :param jogadores: Lista de jogadores.
        """

        if jogadores is None:
            jogadores = []
        self.terrenos = []

        self.cartas_tesouro = [CartaTesouro(face=carta) for carta in list("tafv" * 5 + "dd" + "hhh")]
        self.cartas_tesouro += [CartaAlagamento(face=carta) for carta in "eee"]

        print("Bem-vindos à Ilha Poibida - montagem do tabuleiro")
        self.monta_tabuleiro_oceano(jogadores)

        # abaixa um terreno que fica alagado ou afunda no oceano
        self.terrenos[random.randrange(0, len(self.terrenos))].afundar()

    def trocar_terrenos(self, terreno1, terreno2):
        """
        Troca a posição de dois terrenos no tabuleiro.


        :param terreno1: Instância de um terreno.
        :param terreno2: Instância de outro terreno.
        """
        index1, index2 = self.terrenos.index(terreno1), self.terrenos.index(terreno2)
        self.terrenos[index1], self.terrenos[index2] = self.terrenos[index2], self.terrenos[index1]

    def monta_tabuleiro_oceano(self, jogadores):
        """
        Monta o tabuleiro em forma de diamante.

        :param jogadores: Lista de jogadores.
        """
        tafv = [" "] * 15 + list("tafv") * 2
        random.shuffle(tafv)

        # o primeiro é o helicoptero, deve ser sem tafv
        tafv = [" "] + tafv
        pss = [
            (2, 0), (3, 0),
            (1, 1), (2, 1), (3, 1), (4, 1),
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
            (1, 4), (2, 4), (3, 4), (4, 4),
            (2, 5), (3, 5),
        ]

        self.terrenos = [
            Terreno(
                nome=NOMES.pop(0),
                tafv=tafv.pop(0),
                posx=pss[0][0], posy=pss.pop(0)[1],
                image_src=f"https://imgur.com/{LINKS.pop(0)}.jpg")
            for _ in range(24)
        ]
        random.shuffle(self.terrenos)

        for jogador in jogadores:
            self.terrenos[random.randrange(0, len(self.terrenos))].colocar_jogador(jogador)

    def imprimir_tabuleiro_ilha(self):
        """
        Imprime o tabuleiro da Ilha Proibida no console.

        O tabuleiro é exibido em forma de diamante, com terrenos representados por seus nomes,
        valores de face (tafv) e a presença de jogadores. Cada linha do tabuleiro é separada por
        linhas horizontais, e cada coluna é delimitada por barras verticais.

        :return: None
        """
        print(" " * (__TABLE_SPACES__ * 2 + 3) + "-" * (__TABLE_SPACES__ * 2 + 1))
        tabuleiro = " " * (__TABLE_SPACES__ * 2 + 2) + "| "
        for ter in self.terrenos[:2]:
            tabuleiro += ter.string_rep() + " | "
        print(tabuleiro)
        print(" " * (__TABLE_SPACES__ + 2) + "-" * (__TABLE_SPACES__ * 4 + 3))

        tabuleiro = " " * (__TABLE_SPACES__ + 1) + "| "
        for ter in self.terrenos[2:6]:
            tabuleiro += ter.string_rep() + " | "
        print(tabuleiro)
        print(" " + "-" * (__TABLE_SPACES__ * 6 + 5))

        tabuleiro = "| "
        for ter in self.terrenos[6:12]:
            tabuleiro += ter.string_rep() + " | "
        print(tabuleiro)
        print(" " + "-" * (__TABLE_SPACES__ * 6 + 5))

        tabuleiro = "| "
        for ter in self.terrenos[12:18]:
            tabuleiro += ter.string_rep() + " | "
        print(tabuleiro)
        print(" " + "-" * (__TABLE_SPACES__ * 6 + 5))

        tabuleiro = " " * (__TABLE_SPACES__ + 1) + "| "
        for ter in self.terrenos[18:22]:
            tabuleiro += ter.string_rep() + " | "
        print(tabuleiro)
        print(" " * (__TABLE_SPACES__ + 2) + "-" * (__TABLE_SPACES__ * 4 + 3))

        tabuleiro = " " * (__TABLE_SPACES__ * 2 + 2) + "| "
        for ter in self.terrenos[22:]:
            tabuleiro += ter.string_rep() + " | "
        print(tabuleiro)
        print(" " * (__TABLE_SPACES__ * 2 + 3) + "-" * (__TABLE_SPACES__ * 2 + 1))


class CartaTesouro:
    """
    Classe que representa uma carta de tesouro no jogo Ilha Proibida.
    """

    def __init__(self, face):
        """
        Inicializa a instância da carta de tesouro.

        :param face: Face da carta.
        """
        self.face = face


class CartaAlagamento(CartaTesouro):
    """
    Classe que representa uma carta de alagamento no jogo Ilha Proibida.
    """

    def __init__(self, face):
        """
        Inicializa a instância da carta de alagamento.

        :param face: Face da carta.
        """
        super().__init__(face)


class Carta_Troca_Terrenos(CartaTesouro):
    """
    Classe que representa uma carta que troca os terrenos
    """

    def __init__(self, face):
        """
        Inicializa a instância da carta troca de terrenos

        :param face: Face da carta.
        """
        super().__init__(face)


class Carta_troca_habilidades(CartaTesouro):
    """
    Classe que representa uma carta de troca de habilidades
    """

    def __init__(self, face):
        """
        Inicializa a instância da carta de troca habilidades.

        :param face: Face da carta.
        """
        super().__init__(face)


class Terreno:
    """
    Classe que representa um terreno no tabuleiro do jogo Ilha Proibida.
    """

    def __init__(self, nome, tafv, posx, posy, image_src):
        """
        Inicializa a instância do terreno.

        :param nome: Nome do terreno.
        :param tafv: Valor da face do terreno.
        :param: posx: X position on a grid (6x6)
        :param: posy: Y position on a grid (6x6)
        """
        self.nome = nome
        self.tafv = tafv
        self.jogadores = []
        self.afundado = False
        self.image_src = image_src
        self.posx = posx
        self.posy = posy

    def string_rep(self):
        """
        Retorna uma representação em string do terreno.

        :return: String representando o terreno.
        """
        result = self.nome.lower() if self.afundado else self.nome
        if len(self.jogadores) > 0:
            result += " " + ''.join([jog.nome[0] for jog in self.jogadores])

        faltam = __TABLE_SPACES__ - 3 - len(result)
        return result + " " * faltam + self.tafv

    def colocar_jogador(self, jogador):
        """
        Coloca um jogador no terreno.

        :param jogador: Instância do jogador a ser colocado no terreno.
        """
        self.jogadores.append(jogador)

    def afundar(self):
        """
        Afundar o terreno.
        """
        self.afundado = True


if __name__ == "__main__":
    ilha = IlhaProibida()
    ilha.imprimir_tabuleiro_ilha()

