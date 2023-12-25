import math

from browser import document, window, html

class Canvas:
    def __init__(self):
        self.__canvas__ = document['gameCanvas']
        self.__ctx__ = self.__canvas__.getContext('2d')

    def draw_island(self, island):
        img = window.Image.new()
        img.src = island.image_src

        def on_image_load(e):
            if island.afundado:
                self.__ctx__.globalAlpha = 0.4

            self.__ctx__.drawImage(img, island.posx * 100 + 5, island.posy * 100 + 5, 90, 90)
            self.__ctx__.fillStyle = "black"
            self.__ctx__.fillRect(island.posx * 100 + 5, island.posy * 100 + 80, 90, 15)
            self.__ctx__.fillStyle = "white"
            self.__ctx__.font = "8px Luminari"
            self.__ctx__.fillText(island.nome, island.posx * 100 + 10, island.posy * 100 + 90, 90, 20)

            for x, player in enumerate(island.jogadores):
                self.__ctx__.beginPath()
                self.__ctx__.arc(island.posx * 100 + 5 + x * 30 + 15, island.posy * 100 + 20, 15, 0, 2 * math.pi, False)
                self.__ctx__.fillStyle = player.cor
                self.__ctx__.fill()
                self.__ctx__.lineWidth = 1
                self.__ctx__.strokeStyle = "black"
                self.__ctx__.stroke()
                self.__ctx__.fillStyle = "black"
                self.__ctx__.font = "15px Luminari"
                self.__ctx__.fillText(player.nome[0], island.posx * 100 + 15 + x * 30, island.posy * 100 + 25, 30, 30)

            self.__ctx__.globalAlpha = 1

        img.bind("load", on_image_load)

if __name__ == "__main__":
    Canvas().draw_rect()