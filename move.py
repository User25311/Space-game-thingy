from tokenize import String
from matplotlib.backend_bases import MouseButton
import pygame
from random import randint

from sqlalchemy import false
from sympy import O
pygame.init()  # Used to initalize all the rquired modules of pygame
screenWidth = 800
screenHeight = 800
dead = False

# Used to display a window of the desired size
window = pygame.display.set_mode((screenWidth, screenHeight))

pygame.display.set_caption("Space Game")  # Sets the window title

x = 400  # starting x coordinate
y = 600  # Starting y coordinate
radius = 50
width = 100  # Dimensions of the object (width)
height = 100  # Dimesions of the object (height)


# Starting alien properities
alien_x = 400  # starting x coordinate
alien_y = 100  # Starting y coordinate
# Starting speed of alien
alien_speed_x = 50
alien_speed_y = 50
# Creating variable for alien starting direction
direction = 1

# Used to control the frames per second and thus the game speed
clock = pygame.time.Clock()
run = True  # Indiciate that pygame is running and 'while' loop is used
ship = pygame.image.load("./assets/rocket.png")
ship = pygame.transform.scale(ship, (width, height))
ufo = pygame.image.load("./assets/ufo.png")
ufo = pygame.transform.scale(ufo, (width, height))
ufo2 = pygame.image.load("./assets/ufo#2.png")
ufo2 = pygame.transform.scale(ufo2, (width, height))
space = pygame.image.load("./assets/Space.jpeg")
space = pygame.transform.scale(space, (screenWidth, screenHeight))
oof = False
bullets = []
aliens = []
#music = pygame.mixer.music.load('./assets/universe-space-sounds-3595.mp3')
# pygame.mixer.music.play(-1)


class rocket(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        # Predefined properties
        self.vel = 30

    def draw(self, window):
        window.blit(ship, (self.x, self.y))


class alien(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, window):
        window.blit(ufo, (self.x, self.y))

    def selfMove(self):
        # add some custom logic to move aliens properly

        direction = 1
        alien_speed_x = randint(7, 10) * direction
        alien_speed_y = randint(7, 10) * direction

        if self.x <= 20 or self.x + self.width >= screenWidth:
            direction *= -1
            alien_speed_x = randint(30, 50) * direction
            alien_speed_y = randint(35, 50) * direction
            # Top and Bottom screen boundary
        if self.y <= 20 or self.height >= screenHeight:
            direction *= -1
            alien_speed_x = randint(15, 30) * direction
            alien_speed_y = randint(15, 30) * direction
        self.x += alien_speed_x
        self.y += alien_speed_y


class projectile(object):
    def __init__(self, x, y, radius, colour, direction):
        self.x = x
        self.y = y
        self.radius = radius
        self.colour = colour
        self.direction = direction
        self.vel = 10 * direction

    def draw(self, window):
        pygame.draw.circle(window, self.colour, (self.x, self.y), self.radius)


def reDrawGameWindow():
    window.blit(space, (0, 0))
    p1.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    if (dead != True):
        bot.draw(window)

    for asdf in aliens:
        asdf.draw(window)

    # bot1.draw2(window)

    pygame.display.update()


def crash():
    print("The x is: " + str(bot.x) +
          " and x + width position of the alien is:" + str(bot.x + bot.width))
    print("the y position of the alien is: " + str(bot.y))

    # global liveCrash
    # print("alien is at " + str(bot.y + bot.height))
    # if (len(bullets) > 0):
    #     print("bullet position is at " + str(bullets[len(bullets)-1].y))
    #     if ((bullets[len(bullets)-1].y == (bot.y + bot.height)) and (bullets[len(bullets)-1].x == (bot.x))):
    #         print("Collision!")


# Initlizing objects
p1 = rocket(x, y, width, height)
bot = alien(alien_x, alien_y, width, height)
bot1 = alien(100, 200, width, height)
# Store all our projectile objects in a list
# Function for endgame()


def endGame():
    global oof
    run = True
    while run:
        window.blit(space, (0, 0))
        print("Ending Screen")
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            # if the user hits the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_p]:
                run = False
        score = 10

        largeFont = pygame.font.SysFont('comicsans', 80)
        lastScore = largeFont.render('Best Score: ', 255, 255, 255)
        currentScore = largeFont.render(
            'Score: ' + str(score), 1, (255, 255, 255))
        window.blit(currentScore, (width/2 - currentScore.get_width()/2, 240))
        pygame.display.update()


# clock.tick(60) ##  Means that for every second at most 40 frames should pass
while run:
    clock.tick(30)

    if oof:
        endGame()
    else:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                facing = -1
                if len(bullets) < 1:
                    bullets.append(projectile(
                        (p1.x + p1.width // 2), p1.y, 3, (150, 150, 150), facing))
                crash()

            if keys[pygame.K_LEFT] and p1.x > 0:
                p1.x -= p1.vel
            if keys[pygame.K_RIGHT] and p1.x < screenWidth - p1.width:
                p1.x += p1.vel
            if keys[pygame.K_UP] and p1.y > 0:
                p1.y -= p1.vel
            if keys[pygame.K_DOWN] and p1.y < screenHeight - p1.height:
                p1.y += p1.vel
            if keys[pygame.K_a]:
                aliens.append(alien(alien_x, alien_y, width, height))
            if keys[pygame.K_q]:
                oof = True

        for bullet in bullets:
            if bullet.y < 800 and bullet.y > 0:
                bullet.y += bullet.vel
            else:
                # this removes the bullet if its off the screen
                bullets.pop(bullets.index(bullet))

        for sneila in aliens:
            sneila.selfMove()

        # if aliens:
        #      for i in range(10):
        #          x , y, width,height = aliens[i]
        #          if x <= 20 or x + width >= screenWidth:
        #              direction *= -1
        #              alien_speed_x = randint(7, 10) * direction
        #              alien_speed_y = randint(7, 10) * direction
        #          # Top and Bottom screen boundary
        #          if y <= 20 or height >= screenHeight:
        #              direction *= -1
        #              alien_speed_x = randint(7, 10) *direction
        #          alien_speed_y = randint(7, 10) *direction

        #          x += alien_speed_x
        #          y += alien_speed_y

            # Responsible for random alien movements:

        if bot.x <= 20 or bot.x + bot.width >= screenWidth:
            direction *= -1
            alien_speed_x = randint(7, 10) * direction
            alien_speed_y = randint(7, 10) * direction
            # Top and Bottom screen boundary
        if bot.y <= 20 or bot.height >= screenHeight:
            direction *= -1
            alien_speed_x = randint(7, 10) * direction
            alien_speed_y = randint(7, 10) * direction
        bot.x += alien_speed_x
        bot.y += alien_speed_y

        if (bullets):
            # print(bullets[len(bullets) -1].x)
            # print(bullets[len(bullets) -1].y)
            last_bullet = bullets[len(bullets) - 1]
            if ((last_bullet.y <= (bot.y + bot.height)) and (last_bullet.y >= (bot.y)) and (((last_bullet.x + last_bullet.radius) >= bot.x) and ((last_bullet.x + last_bullet.radius) <= (bot.x + bot.width)))):
                dead = True
                print(dead)
                print("KILLED")

        reDrawGameWindow()
pygame.quit()
