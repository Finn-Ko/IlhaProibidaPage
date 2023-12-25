from browser import document, window, html

class Canvas:
    def __init__(self):
        self.__canvas__ = document['gameCanvas']
        self.__ctx__ = self.__canvas__.getContext('2d')

    def draw_island(self, island):
        img = window.Image.new()
        img.src = island.image_src

        # Draw the image on the canvas when it's loaded
        def on_image_load(e):
            if island.afundado:
                self.__ctx__.globalAlpha = 0.4

            self.__ctx__.drawImage(img, island.posx * 100 + 5, island.posy * 100 + 5, 90, 90)
            self.__ctx__.globalAlpha = 1

        img.bind("load", on_image_load)

if __name__ == "__main__":
    Canvas().draw_rect()