"""Página Jogador do jogo Ilha Proibida Equipe Fogo.

EQUIPE FOGO 

.. codeauthor:: Fernanda Araujo <fernandacsaraujo@gmail.com>
.. codeauthor::  Finn Kockelke <finn_kockelke@gmx.net>
.. codeauthor:: Vanessa M Vianna <vanmvianna@gmail.com>
.. codeauthor:: Anderson Amorim da Silva <anderson.amorix@gmail.com>


Changelog
---------
.. versionadded::    23.11
    classe jogador e MaoJogador (07).
.. versionadded::    21.12
   funcionalidade troca de habilidades do jogador (07).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023, Fernanda Araujo** <fernandacsaraujo@gmail.com>, Finn Kockelke** <finn_kockelke@gmx.net>, Vanessa M Vianna** <vanmvianna@gmail.com>
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""
class MaoJogador:
    def __init__(self, dono, cartas=None):
        """
        Inicializa a mão do jogador.

        :param dono: Instância do jogador dono da mão.
        :param cartas: Lista de cartas na mão, padrão é uma lista vazia.
        """
        if cartas is None:
            cartas = []
        self.dono = dono
        self.cartas = cartas
        print(f"A mão do {self.dono.nome} possui {len(self.cartas)} cartas")

class Jogador:
    def __init__(self, cor, nome="DefaultPlayer", habilidade=""):
        """
        Inicializa a instância do jogador.

        :param cor: Cor do jogador.
        :param nome: Nome do jogador, padrão é "DefaultPlayer".
        :param habilidade: Habilidade especial do jogador, padrão é uma string vazia.
        """
        self.cor = cor
        self.nome = nome
        self.habilidade = habilidade
        self.mao = MaoJogador(dono=self)
        print(f"{self.nome} se apresentando")

    def trocar_habilidades(self, outro_jogador):
        """
        Troca as habilidades especiais com outro aventureiro.

        :param outro_jogador: Instância de outro aventureiro.
        """
        self.habilidade, outro_jogador.habilidade = outro_jogador.habilidade, self.habilidade

# ilha.py (exemplo de uso da Carta de Troca de Habilidades)
Jogador1 = Jogador("Explorador", "Pode se mover para qualquer terreno adjacente")
Jogador2 = Jogador("Engenheiro", "Pode secar dois terrenos por ação")

# Uso da Carta de Troca de Habilidades
Jogador1.trocar_habilidades(Jogador2)



        
        
if __name__ == "__main__":
    Jogador()
    