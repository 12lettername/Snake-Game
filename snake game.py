import pygame
from pygame.locals import *
import random

name = input("Enter your name: ")   # asking for player's name
pygame.init()  # Initialize pygame

# Window Size
height = 700
width = 600

# colours
RED = (255, 0, 0)
BLUE = (51, 153, 255)
ORANGE = (250, 160, 0)
GREEN = (51, 102, 0)
BLACK = (0, 0, 0)

# Setting up the game
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")


clock = pygame.time.Clock()

# setting up the fonts
font = pygame.font.SysFont("comicsansms", 20)
score_font = pygame.font.SysFont("gabriola", 32)
name_font = pygame.font.SysFont("gabriola", 36)


def nameplate(name):
    render = name_font.render(name, True, RED)
    win.blit(render, [250, 0])


def score_card(score):  # will update the scorecard
    num = score_font.render("SCORE :" + str(score), True, BLUE)
    win.blit(num, [0, 0])


def game(objects, objectlist):
    for i in objectlist:
        pygame.draw.rect(win, GREEN, [i[0], i[1], objects, objects])


def message(msg):
    mes = font.render(msg, True, RED)
    win.blit(mes, [width / 35, height / 3])


def check_game():
    gameOn = True
    gameClose = False

    gameObject = 10  # game object initialize
    objectSpeed = 15  # game object speed

    x = width / 2  # 300
    y = height / 2  # 350

    x_change = 0
    y_change = 0

    lengthTracker = []
    objectLength = 1
    food_x = round(random.randrange(0, width - gameObject) / 10.0) * 10.0
    food_y = round(random.randrange(0, height - gameObject) / 10.0) * 10.0
    while gameOn:
        while gameClose:  # will run when u lose
            win.fill(BLACK)
            message("You Lost!! Press P to play again or Q to quit")
            score_card(objectLength - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_p:
                        check_game()

        for event in pygame.event.get():  # running while game is on
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT:
                    x_change = -gameObject
                    y_change = 0
                if event.key == K_RIGHT:
                    x_change = gameObject
                    y_change = 0
                if event.key == K_UP:
                    x_change = 0
                    y_change = -gameObject
                if event.key == K_DOWN:
                    x_change = 0
                    y_change = gameObject

        if x > width or x < 0 or y > height or y < 0:
            gameClose = True

        x += x_change
        y += y_change
        win.fill(BLACK)
        pygame.draw.rect(win, ORANGE, [food_x, food_y, gameObject, gameObject])
        objectSize = [x, y]
        lengthTracker.append(objectSize)
        if len(lengthTracker) > objectLength:
            del lengthTracker[0]
        nameplate(name)
        game(gameObject, lengthTracker)
        score_card(objectLength - 1)
        pygame.display.update()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, width - gameObject) / 10.0) * 10.0
            food_y = round(random.randrange(0, height - gameObject) / 10.0) * 10.0
            objectLength += 1
            objectSpeed += 1
        clock.tick(objectSpeed)


check_game()
