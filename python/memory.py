import pygame
from pygame.locals import *
import requests
import time
import random
import io
import os, pygame.mixer, pygame.time, string

WIDTH = 4
HEIGHT = 2


def get_key():
    while 1:
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            return event.key
        else:
            pass


def display_box(screen, message, x, y, background):
    fontobject = pygame.font.Font(None, 18)
    pygame.draw.rect(background, (250, 250, 250),
                     (x,
                      y,
                      200, 20), 0)
    pygame.draw.rect(background, (0, 0, 0),
                     (x - 2,
                      y - 2,
                      204, 24), 1)
    if len(message) != 0:
        background.blit(fontobject.render(message, 1, (0, 0, 0)),
                        (x, y))
    screen.blit(background, (0, 0))
    pygame.display.flip()


def ask(screen, question):
    pygame.font.init()
    current_string = []
    user2_string = []
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((55, 250, 250))
    display_box(screen, "user1" + ": " + "".join(current_string), 125, 700, background)
    display_box(screen, "user2" + ": " + "".join(user2_string), 400, 700, background)
    flag = 0
    while 1:
        inkey = get_key()
        if inkey == K_BACKSPACE:
            if flag == 0:
                current_string = current_string[0:-1]
            else:
                user2_string = user2_string[0:-1]
        elif inkey == K_RETURN and flag == 1:
            break
        elif inkey == K_RETURN and flag == 0:
            flag = 1
        elif inkey == K_MINUS:
            if flag == 0:
                current_string.append("_")
            else:
                user2_string.append("_")
        elif inkey <= 127:
            if flag == 0:
                current_string.append(chr(inkey))
            else:
                user2_string.append(chr(inkey))
        display_box(screen, "user1" + ": " + "".join(current_string), 125, 700, background)
        display_box(screen, "user2" + ": " + "".join(user2_string), 400, 700, background)
    return "".join(current_string)


# Checks if the cards match using their array indices
def match_check(deck, flipped):
    if deck[WIDTH * flipped[0][1] + flipped[0][0]] == deck[WIDTH * flipped[1][1] + flipped[1][0]]:
        return deck[WIDTH * flipped[0][1] + flipped[0][0]]


# Get mouse position, and check which card it's on using division
def card_check(mouse_pos):
    MouseX = mouse_pos[0]
    MouseY = mouse_pos[1]
    CardX = int(MouseX / 125)
    CardY = int(MouseY / 181)
    card = (CardX, CardY)
    return card


# Draw the cards. This is used after initialization and to rehide cards
def card_draw(cards):
    pygame.init()
    DISPLAY_SIZE = (125 * WIDTH, 181 * HEIGHT)
    screen = pygame.display.set_mode(DISPLAY_SIZE)

    # Place card images in their appropriate spots by multiplying card width & height
    for i in range(WIDTH):
        for j in range(HEIGHT):
            screen.blit(cards[i + WIDTH * j], (i * 125, j * 181))


# Load the main card images (used in cards_init())
def card_load(char):
    # card = "./pictures/%s.png" % char
    # url = "http://localhost:3000/pictures/%s" %char
    picture = requests.get("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/%s.png" % char,
                           verify=False)
    # picture = requests.get(url,verify=False)
    img = io.BytesIO(picture.content)
    card_load = pygame.image.load(img).convert()
    # card_load = games.Sprite(image = spaceship_image, x=350, y=235)
    card_load = pygame.transform.scale(card_load, (125, 181))

    return card_load
    # return card


def cards_init():
    cards = []
    for i in range(1, int((WIDTH * HEIGHT) / 2) + 1):
        cards.append(card_load(i))

    cards *= 2  # Python is great - just double the list to duplicate!

    # Shuffle the deck for a new game every time
    random.shuffle(cards)

    return cards


def main(runs):
    DISPLAY_SIZE = (WIDTH * 125, HEIGHT * 181)
    GAME_TITLE = "Pokemon's Memory Match"
    DESIRED_FPS = 60

    # Setup preliminary pygame stuff
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY_SIZE)

    pygame.display.set_caption(GAME_TITLE)
    fps_clock = pygame.time.Clock()
    pygame.mixer.init()
    pygame.mixer.music.load("../python/song.mp3")
    pygame.mixer.music.set_volume(0.3)

    # Ensure the welcome message is displayed only on the first time through
    if runs == 0:
        # print (ask(screen, "user1") + " was entered")
        # screen.blit(screen, (0, 0))
        # pygame.display.flip()
        print("Welcome to Memory Match! Select two cards to flip them and find a match!")
        print("Press 'q' to quit at any time.")
    elif runs == 1:
        print("\n\nNew Game")

    card_deck = []
    card_deck = cards_init()  # initialize deck

    card_back = pygame.image.load('../pictures/back_card.png')
    visible_deck = []

    for x in range(WIDTH * HEIGHT):
        visible_deck.append(card_back)

    card_draw(visible_deck)

    game_run = True  # run the game
    # "Global" variables used throughout the while loop
    flips = []
    found = []
    missed = 0
    first_flip = 0
    second_flip = 0
    t = 1
    pygame.mixer.music.play()
    while game_run:
        user_input = pygame.event.get()
        pressed_key = pygame.key.get_pressed()

        # Retreives all user input
        for event in user_input:
            # Is the input mouse button pressed down?
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Get position of mouse and put it into card_check
                # to figure out which card mouse is on
                mouse_pos = pygame.mouse.get_pos()
                card_select = card_check(mouse_pos)
                # Make sure card has not been selected before
                if card_select not in flips and card_select not in found:
                    flips.append(card_select)
                    # Put the actual value of the card on the screen (vs just the back)
                    if len(flips) <= 2:
                        card_front = pygame.image.load('../pictures/front_card.png')
                        card_front = pygame.transform.scale(card_front, (125, 181))
                        screen.blit(card_front, (card_select[0] * 125, card_select[1] * 181))
                        screen.blit(card_deck[WIDTH * card_select[1] + card_select[0]],
                                    (125 * card_select[0], 181 * card_select[1]))
                        # screen.blit(pygame.image.load('./pictures/1.png'), (125*card_select[0],181*card_select[1]))
                        first_flip = time.time()  # First card has been flipped
                    if len(flips) == 2:
                        second_flip = time.time()  # Second card has been flipped
                        match = match_check(card_deck, flips)  # Are the two cards a match?
                        if match:
                            # If a match, append coordinates of two cards to found array,
                            # and have them permanently displayed by adding them to the visible deck
                            for i in range(2):
                                found.append(flips[i])
                                visible_deck[WIDTH * flips[i][1] + flips[i][0]] = card_deck[
                                    WIDTH * flips[i][1] + flips[i][0]]
                            print("Matches found: {}/{}".format(int(len(found) / 2), int(WIDTH * HEIGHT / 2)))
                            t = 0  # Allows user to immediately flip next card
                        else:
                            missed += 1

        # Show the cards only for one second
        if len(flips) >= 2 and time.time() - second_flip > t:
            t = 1
            card_draw(visible_deck)
            flips = []

        # If the user is slow, the card gets flipped back
        elif len(flips) == 1 and time.time() - first_flip > 3:
            card_draw(visible_deck)
            flips = []
            # Unsure if misseses += 1 belongs here - balance question

        # This comes before quitting to avoid video errors
        pygame.display.flip()
        fps_clock.tick(DESIRED_FPS)

        if pressed_key[K_q]:
            game_run = False

        if len(found) == HEIGHT * WIDTH:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("../python/claps.mp3")
            pygame.mixer.music.set_volume(1)
            pygame.mixer.music.play()
            found.append("WIN")
            print("YOU WIN!")
            print("Score: %d misses" % missed)
            print("\nPlay again? (y/n)")  # User presses "y" or "n" in the card window
            runs = 2

        if runs == 2:  # Win mode of main
            if pressed_key[K_y]:
                main(1)
            elif pressed_key[K_n]:
                game_run = False

    pygame.quit()


main(0)
