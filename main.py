# # 2
# 15/10/2021 - 22/10/2021
# RUNNER.SV
import pygame
import random
import math
import sys
import os
from pygame.locals import *
from pygame import mixer

pygame.init()
screen = pygame.display.set_mode((1300, 600))  # (326, 195)

pygame.display.set_caption(os.path.join("RUNNER.SV"))
icon = pygame.image.load(os.path.join('game_files/character_files/RanRy.jpg'))
pygame.display.set_icon(icon)


class Runner(object):
    run = [pygame.image.load(os.path.join('game_files', 'character_files', str(x) + '.png')) for x in range(1, 13)]
    jump = [pygame.image.load(os.path.join('game_files', 'character_files', 'j1.png')),pygame.image.load(os.path.join('game_files', 'character_files', 'j2.png')) , pygame.image.load(os.path.join('game_files', 'character_files', 'j2.png')),pygame.image.load(os.path.join('game_files', 'character_files', 'j3.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j3.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j4.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j4.png')),  pygame.image.load(os.path.join('game_files', 'character_files', 'j5.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j5.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j6.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j7.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j7.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j8.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j8.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'j9.png')),  pygame.image.load(os.path.join('game_files', 'character_files', 'j9.png'))]#, pygame.image.load(os.path.join('game_files', 'character_files', 's1.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's2.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's3.png'))]
    slide = [pygame.image.load(os.path.join('game_files', 'character_files', 's3.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's2.png')),pygame.image.load(os.path.join('game_files', 'character_files', 's3.png')),pygame.image.load(os.path.join('game_files', 'character_files', 's2.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's2.png')),pygame.image.load(os.path.join('game_files', 'character_files', 's3.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's3.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's2.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's3.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's2.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's2.png')), pygame.image.load(os.path.join('game_files', 'character_files', 's3.png'))]
    hit = [pygame.image.load(os.path.join('game_files', 'character_files', 'c1.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'c2.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'c3.png')), pygame.image.load(os.path.join('game_files', 'character_files', 'c4.png'))]
    jumpList = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4,
                4, 4, 4, 4, 4, 4, 4, 4, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1,
                -1, -1, -1, -1, -1, -1, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -2, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3, -3,
                -3, -3, -3, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4, -4]

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.jumping = False
        self.sliding = False
        self.slideUp = False
        self.hitting = False
        self.jumpCount = 0
        self.slideCount = 0
        self.runCount = 0

    def runner(self, screen):
        if self.hitting:
            screen.blit(self.hit[1], (self.x, self.y))

        elif self.jumping:
            self.y -= self.jumpList[self.jumpCount + 8] * 2
            screen.blit(self.jump[self.jumpCount // 8], (self.x, self.y))
            self.jumpCount += 1
            if self.jumpCount > 117:
                self.jumpCount = 0
                self.jumping = False
                self.runCount = 0
            self.hitbox = (self.x + 40, self.y, self.w - 90, self.h - 30)
            # pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)
        elif self.sliding or self.slideUp:
            if self.slideCount < 20:
                self.y += 0
                self.hitbox = (self.x + 55, self.y + 43, self.w - 40, self.h - 50)
                # pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)
            elif self.slideCount == 80:
                self.y -= 0
                self.sliding = False
                self.slideUp = True
            elif (self.slideCount > 20) and (self.slideCount < 80):
                self.hitbox = (self.x + 55, self.y + 43, self.w - 40, self.h - 50)
                # pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)

            if self.slideCount >= 120:
                self.slideCount = 0
                self.runCount = 0
                self.slideUp = False
                self.hitbox = (self.x + 55, self.y + 43, self.w - 40, self.h - 50)
            screen.blit(self.slide[self.slideCount // 10], (self.x, self.y))
            self.slideCount += 1
            # pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)

        else:
            if self.runCount > 78:
                self.runCount = 0
            screen.blit(self.run[self.runCount // 7], (self.x, self.y))
            self.runCount += 1
            self.hitbox = (self.x + 65, self.y + 10, self.w - 90, self.h - 75)
            self.hitbox_2 = (self.x + 40, self.y + 80, self.w - 100, self.h - 80)
            # pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)
            # pygame.draw.rect(screen, (255, 255, 255), self.hitbox_2, 1)
            # runs = mixer.Sound(os.path.join('game_files', 'game sounds', "running.mp3"))
            # runs.play()




class AC(object):
    ac1 = pygame.image.load(os.path.join('game_files','game_obstacles',"air-conditioner.png"))
    ac_1 = pygame.transform.scale(ac1, (90, 80))
    ac2 = pygame.image.load(os.path.join('game_files','game_obstacles', "ac1.png"))
    ac_2 = pygame.transform.scale(ac2, (90, 70))
    ac3 = pygame.image.load(os.path.join('game_files','game_obstacles', "ac2.png"))
    ac_3 = pygame.transform.scale(ac3, (90, 80))
    acImages = [ac_1, ac_2, ac_3]
    ac = random.choice(acImages)
    screen.blit(ac, (1000, 430))

    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hitbox = (x, y, w, h)

    def draw(self, screen):
        self.hitbox = (self.x + 8, self.y + 5, self.w - 10, self.h)
        screen.blit(self.ac, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)

    def collide(self, rect):
        if (rect[1] + rect[3] < self.hitbox[1] + self.hitbox[3]) and (rect[1] + rect[3] > self.hitbox[1]) and (rect[0] + rect[2] > self.hitbox[0]) and (rect[0] < self.hitbox[0] + self.hitbox[2]):
            return True

        return False

        # if rect[0] == self.hitbox[0] and rect[1] == self.hitbox[1]
        #     return True
        # else:
        #     return False
        # distance = math.sqrt(math.pow(rect[2] - self.hitbox[0], 2) + (math.pow(rect[3] - self.hitbox[1], 2)))
        # if distance < 50:
        #     return True
        # else:
        #     return False
        # # if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
        # #     if rect[1] < self.hitbox[3]:
        # #         return True
        # # return False




class Antenna(AC):
    an_1 = pygame.image.load(os.path.join('game_files','game_obstacles',  "an1.png"))
    an_2 = pygame.image.load(os.path.join('game_files','game_obstacles', "an2.png"))
    an_Images = [an_1, an_2]
    antenna = random.choice(an_Images)

    def draw(self, screen):
        self.hitbox = (self.x + 10, self.y + 5, self.w - 15, self.h - 8)
        screen.blit(self.antenna, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)

    # def collide(self, rect):
    #     pass
    #     if rect[0] + rect[2] > self.hitbox[0] and rect[0] < self.hitbox[0] + self.hitbox[2]:
    #         if rect[1] + rect[3] > self.hitbox[1]:
    #             return True
    #     return False


class slide_1(AC):
    s_1 = pygame.image.load(os.path.join('game_files','game_obstacles', 'Slide.png'))

    def draw(self, screen):
        self.hitbox = (self.x, self.y + 5 , self.w, self.h)
        screen.blit(self.s_1, (self.x, self.y))
        # pygame.draw.rect(screen, (255, 255, 255), self.hitbox, 1)


class slide_2(slide_1):
    s_1 = pygame.image.load(os.path.join('game_files','game_obstacles', 'Slide2.png'))


# ac_1 = pygame.image.load("air-conditioner.png")
# ac = pygame.transform.scale(ac_1, (90, 80))
# ac_2 = pygame.image.load("window-ac.png")
# ac2 = pygame.transform.scale(ac_2, (90, 80))

background = pygame.image.load(os.path.join('game_files', "background.jpg"))
bg = pygame.transform.scale(background, (1300, 500))
bgX = 0
bgX2 = bg.get_width()
clock = pygame.time.Clock()

mixer.music.load(os.path.join('game_files', 'game sounds', "theme_song.mp3"))
mixer.music.play(-1)

# mixer.music.load(os.path.join('game_files', 'game sounds', "running.mp3"))
# mixer.music.play(-1)



c_x = 1200
c_y = 80
radius = 50
radius2 = 40
radius3 = 30
sun_X = -0.02
sun_Y = 0


def sun(x, y):
    pygame.draw.circle(screen, (255, 170, 0), (c_x, c_y), radius)
    pygame.draw.circle(screen, (255, 200, 50), (c_x, c_y), radius2)
    pygame.draw.circle(screen, (255, 220, 100), (c_x, c_y), radius3)


def movement():
    screen.blit(bg, (bgX, 0))
    screen.blit(bg, (bgX2, 0))
    # Player.runner(screen)
    largeFont = pygame.font.SysFont('comicsans', 30)
    text = largeFont.render('Score: ' + str(score), 1, (255, 255, 255))
    for obj in obstacle:
        obj.draw(screen)
    # screen.blit(character, (100, 370))
    character.runner(screen)
    screen.blit(text, (40, 20))
    # screen.blit(ac, (600, 430))
    # screen.blit(ac2, (500, 430))
    # pygame.display.update()


def hiScore():
    f = open('scores.txt', 'r')
    file = f.readlines()
    last = int(file[0])

    if last < int(score):
        f.close()
        file = open('scores.txt', 'w')
        file.write(str(score))
        file.close()

        return score

    return last


def endScreen():
    global pause, score, speed, obstacles
    pause = 0
    speed = 30
    obstacles = []
    ove = mixer.Sound(os.path.join('game_files', 'game sounds', "game_over.mp3"))
    ove.play()

    run = True
    while run:
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                character.hitting = False
                character.sliding = False
                character.jumping = False



        screen.blit(bg, (0, 0))
        largeFont = pygame.font .SysFont('comicsans', 80)
        smallFont = pygame.font.SysFont('comicsans', 40)
        lastScore = largeFont.render('Best Score: ' + str(hiScore()), 1, (255, 255, 255))
        currentScore = largeFont.render('Score: ' + str(score), 1, (255, 255, 255))
        playAgain = smallFont.render('Click left mouse button to play again', 1, (255, 255, 255))
        screen.blit(playAgain, (650 - playAgain.get_width() / 2, 430))
        screen.blit(lastScore, (650 - lastScore.get_width() / 2, 150))
        screen.blit(currentScore, (650 - currentScore.get_width() / 2, 240))
        pygame.display.update()
    score = 0


width = 1300
speed = 100
# character = pygame.image.load(os.path.join("game_files", 'character_files', '1.png'))
character = Runner(100, 365, 135, 145)
pause = 0
fallSpeed = 0
score = 0
pygame.time.set_timer(USEREVENT + 1, 500)
pygame.time.set_timer(USEREVENT + 2, random.randrange(1500, 5000))
obstacle = []
runtime = True
while runtime:
    screen.fill((0, 0, 0))
    if pause > 0:
        pause += 1
        if pause > fallSpeed * 2:
            endScreen()

    score = speed // 10 - 3

    for obj in obstacle:
        if obj.collide(character.hitbox) :#or obj.collide(character.hitbox_2):
            character.hitting = True

            if pause == 0:
                pause = 1
                fallSpeed = 50

        obj.x -= 1.4
        if obj.x < - 100:
            obstacle.pop(obstacle.index(obj))
    bgX -= 1.4
    bgX2 -= 1.4
    movement()
    if bgX < bg.get_width() * -1:
        bgX = bg.get_width()
    if bgX2 < bg.get_width() * -1:
        bgX2 = bg.get_width()

    sun(c_x, c_y)
    c_x += sun_X
    if c_x < -100:
        c_x = 1400

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
        if not (character.jumping):
            character.jumping = True
            jum = mixer.Sound(os.path.join('game_files', 'game sounds',"jump.mp3"))
            jum.play()

    if keys[pygame.K_DOWN]:
        if not (character.sliding):
            character.sliding = True
            slide = mixer.Sound(os.path.join('game_files', 'game sounds', "slide.mp3"))
            slide.play()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runtime = False
        if event.type == USEREVENT + 1:
            speed += 3
        if event.type == USEREVENT + 2:
            r = random.randint(0, 4)
            # print(r)
            if r == 0:
                obstacle.append(Antenna(1400, 435, 64, 64))
                Antenna(1400, 430, 64, 64)

            elif r == 1:
                obstacle.append(AC(1700, 430, 64, 64))
                AC(1700, 430, 64, 64)

            elif r == 4:
                obstacle.append(slide_1(1700, 380, 64, 64))
                slide_1(1700, 380, 64, 64)

            elif r == 3:
                obstacle.append(slide_2(1700, 380, 64, 64))
                slide_2(1700, 380, 64, 64)

            # for r in range(0,2):
            #     if r == 0:
            #         obstacle.append(Antenna(1400, 430, 64, 64))
            #     else:
            #         obstacle.append(AC(1700, 430, 64, 64))

    clock.tick(speed)
    pygame.display.update()



