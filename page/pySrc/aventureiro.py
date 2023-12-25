"""Página Jogador do jogo Ilha Proibida Equipe Fogo.

EQUIPE FOGO

.. codeauthor:: Fernanda Araujo <fernandacsaraujo@gmail.com>
.. codeauthor:: Finn Kockelke <finn_kockelke@gmx.net>
.. codeauthor:: Vanessa M Vianna <vanmvianna@gmail.com>
.. codeauthor:: Anderson Amorim da Silva <anderson.amorix@gmail.com>


Changelog
---------


|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023, Fernanda Araujo** <fernandacsaraujo@gmail.com>, Finn Kockelke** <finn_kockelke@gmx.net>, Vanessa M Vianna** <vanmvianna@gmail.com>
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

class Aventureiro:
    def __init__(self, nome, habilidade):
        """
        Inicializa a instância do cartão de aventureiro.

        :param nome: Nome do aventureiro.
        :param habilidade: Descrição da habilidade especial do aventureiro.
        """
        self.nome = nome
        self.habilidade = habilidade

    def usar_habilidade(self):
        """
        Método que representa o uso da habilidade especial do aventureiro durante o jogo.
        """
        print(f"{self.nome}: {self.habilidade}")

    def trocar_habilidades(self, outro_aventureiro):
        """
        Troca as habilidades especiais com outro aventureiro.

        :param outro_aventureiro: Instância de outro aventureiro.
        """
        self.habilidade, outro_aventureiro.habilidade = outro_aventureiro.habilidade, self.habilidade

# Exemplos de instância de cartões de aventureiro
aventureiro1 = Aventureiro("Explorador", "Pode se mover para qualquer terreno adjacente")
aventureiro2 = Aventureiro("Engenheiro", "Pode secar dois terrenos por ação")

# Exemplos de uso das habilidades especiais
aventureiro1.usar_habilidade()
aventureiro2.usar_habilidade()
