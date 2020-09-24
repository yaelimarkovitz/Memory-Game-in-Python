import pygame
from pygame.locals import *


# class card(pygame.sprite.Sprite):
#     def __init__(self,pos)
def card_load(char):
    print("hi")
    card = "./pictures/%s.png" % char
    card_load = pygame.image.load(card)
    return card_load


def cards_init():
    cards = []
    for i in range(1, 16):
        cards.append(card_load)
    cards *= 2  # Python is great - just double the list to duplicate!

    # random.shuffle(cards)

    return cards


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((1000, 600))
    pygame.display.set_caption('memory game')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # fps_clock = pygame.time.Clock()

    card_deck = cards_init()
    url = "C:/Users/RENT/Desktop/python/python_project/python/back.png"
    card_back = pygame.image.load(url)
    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__': main()
