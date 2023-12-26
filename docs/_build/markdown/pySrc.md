# pySrc package

## Submodules

## pySrc.aventureiro module

### *class* pySrc.aventureiro.Aventureiro(nome, habilidade)

Bases: `object`

#### \_\_init_\_(nome, habilidade)

Inicializa a instância do cartão de aventureiro.

* **Parâmetros:**
  * **nome** – Nome do aventureiro.
  * **habilidade** – Descrição da habilidade especial do aventureiro.

#### trocar_habilidades(outro_aventureiro)

Troca as habilidades especiais com outro aventureiro.

* **Parâmetros:**
  **outro_aventureiro** – Instância de outro aventureiro.

#### usar_habilidade()

Método que representa o uso da habilidade especial do aventureiro durante o jogo.

## pySrc.canvas module

### *class* pySrc.canvas.Canvas

Bases: `object`

#### \_\_init_\_()

Inicializa a instância da classe Canvas.

Cria uma instância do Canvas, obtendo o elemento canvas do documento HTML
e o contexto 2D associado para desenho.

#### draw_island(island)

Desenha uma ilha no canvas.

Args:
: island (objeto): Instância da classe que representa uma ilha.

## pySrc.ilha module

### *class* pySrc.ilha.CartaAlagamento(face)

Bases: [`CartaTesouro`](#pySrc.ilha.CartaTesouro)

Classe que representa uma carta de alagamento no jogo Ilha Proibida.

#### \_\_init_\_(face)

Inicializa a instância da carta de alagamento.

* **Parâmetros:**
  **face** – Face da carta.

### *class* pySrc.ilha.CartaTesouro(face)

Bases: `object`

Classe que representa uma carta de tesouro no jogo Ilha Proibida.

#### \_\_init_\_(face)

Inicializa a instância da carta de tesouro.

* **Parâmetros:**
  **face** – Face da carta.

### *class* pySrc.ilha.Carta_Troca_Terrenos(face)

Bases: [`CartaTesouro`](#pySrc.ilha.CartaTesouro)

Classe que representa uma carta que troca os terrenos

#### \_\_init_\_(face)

Inicializa a instância da carta troca de terrenos

* **Parâmetros:**
  **face** – Face da carta.

### *class* pySrc.ilha.Carta_troca_habilidades(face)

Bases: [`CartaTesouro`](#pySrc.ilha.CartaTesouro)

Classe que representa uma carta de troca de habilidades

#### \_\_init_\_(face)

Inicializa a instância da carta de troca habilidades.

* **Parâmetros:**
  **face** – Face da carta.

### *class* pySrc.ilha.IlhaProibida(jogadores=None)

Bases: `object`

Classe principal que representa o jogo Ilha Proibida.

#### \_\_init_\_(jogadores=None)

Inicializa a instância do jogo Ilha Proibida.

* **Parâmetros:**
  **jogadores** – Lista de jogadores.

#### imprimir_tabuleiro_ilha()

Imprime o tabuleiro da Ilha Proibida no console.

O tabuleiro é exibido em forma de diamante, com terrenos representados por seus nomes,
valores de face (tafv) e a presença de jogadores. Cada linha do tabuleiro é separada por
linhas horizontais, e cada coluna é delimitada por barras verticais.

* **Retorno:**
  None

#### monta_tabuleiro_oceano(jogadores)

Monta o tabuleiro em forma de diamante.

* **Parâmetros:**
  **jogadores** – Lista de jogadores.

#### trocar_terrenos(terreno1, terreno2)

Troca a posição de dois terrenos no tabuleiro.

* **Parâmetros:**
  * **terreno1** – Instância de um terreno.
  * **terreno2** – Instância de outro terreno.

### *class* pySrc.ilha.Terreno(nome, tafv, posx, posy, image_src)

Bases: `object`

Classe que representa um terreno no tabuleiro do jogo Ilha Proibida.

#### \_\_init_\_(nome, tafv, posx, posy, image_src)

Inicializa a instância do terreno.

* **Parâmetros:**
  * **nome** – Nome do terreno.
  * **tafv** – Valor da face do terreno.
* **Param:**
  posx: X position on a grid (6x6)
* **Param:**
  posy: Y position on a grid (6x6)

#### afundar()

Afundar o terreno.

#### colocar_jogador(jogador)

Coloca um jogador no terreno.

* **Parâmetros:**
  **jogador** – Instância do jogador a ser colocado no terreno.

#### string_rep()

Retorna uma representação em string do terreno.

* **Retorno:**
  String representando o terreno.

## pySrc.jogador module

### *class* pySrc.jogador.Jogador(cor, nome='DefaultPlayer', habilidade='')

Bases: `object`

#### \_\_init_\_(cor, nome='DefaultPlayer', habilidade='')

Inicializa a instância do jogador.

* **Parâmetros:**
  * **cor** – Cor do jogador.
  * **nome** – Nome do jogador, padrão é «DefaultPlayer».
  * **habilidade** – Habilidade especial do jogador, padrão é uma string vazia.

#### trocar_habilidades(outro_jogador)

Troca as habilidades especiais com outro aventureiro.

* **Parâmetros:**
  **outro_jogador** – Instância de outro aventureiro.

### *class* pySrc.jogador.MaoJogador(dono, cartas=None)

Bases: `object`

#### \_\_init_\_(dono, cartas=None)

Inicializa a mão do jogador.

* **Parâmetros:**
  * **dono** – Instância do jogador dono da mão.
  * **cartas** – Lista de cartas na mão, padrão é uma lista vazia.

## pySrc.main module

Página de Entrada do jogo Ilha Proibida Equipe Fogo.

WORKFLOWY - [http://bit.ly/Dev_Agile_23](http://bit.ly/Dev_Agile_23)

EQUIPE FOGO

### Changelog

#### Versionadded
Novo na versão 23.11: Divisão de equipes (07).
Adicao do modulo ilha e jogador.

#### Versionadded
Novo na versão 23.10: Classes Ilha, Terreno, Peao (10).

#### Versionadded
Novo na versão 23.09: Versão Inicial (26).

**Open Source Notification:** This file is part of open source program **Ilha Proibida**
<br/>
**Copyright © 2023, Fernanda Araujo** <[fernandacsaraujo@gmail.com](mailto:fernandacsaraujo@gmail.com)>, Finn Kockelke\*\* <[finn_kockelke@gmx.net](mailto:finn_kockelke@gmx.net)>, Vanessa M Vianna\*\* <[vanmvianna@gmail.com](mailto:vanmvianna@gmail.com)>
<br/>
**SPDX-License-Identifier:** [GNU General Public License v3.0 or later](http://is.gd/3Udt).
<br/>
[Labase](http://labase.selfip.org/) - [NCE](https://portal.nce.ufrj.br) - [UFRJ](https://ufrj.br/).
<br/>

## Module contents
