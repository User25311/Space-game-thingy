from tokenize import String
from anyio import current_effective_deadline
from matplotlib.backend_bases import MouseButton
import pygame
from random import randint
import time
import sys
from random import choice
from sqlalchemy import false, true
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


alien1_speed_x = 25
alien1_speed_y = 25
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
current_score = 0
bullets = []
aliens = []
dead_alien_index = 0

#Timer
MOREalien=0
seconds=0
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
        self.eatgudfoodandbehealthy = 10
        self.iseeu = True

    def draw(self, window):
        if self.iseeu:
            window.blit(ufo, (self.x, self.y)) 
            pygame.draw.rect(window, (255, 255, 255) ,((self.x + 15), (self.y - 20), 50 ,10))
            pygame.draw.rect(window, (250, 48, 2),((self.x + 15), (self.y - 20), 50 -(5 * (10 -self.eatgudfoodandbehealthy))  ,10))

# SOME WORK NEEDS TO BE DONE HERE>:(
    def selfMove(self):
        # add some custom logic to move aliens properly
        for alien in aliens:
            alien0_speed_x = 2
            alien0_speed_y = 2
            direction = choice([i for i in range(-1,1) if i not in [0]])
           
            alien0_speed_x = randint(7, 10) * direction
            alien0_speed_y = randint(7, 10) * direction

        
            if alien.x <= 20 or alien.x + alien.width >= screenWidth:
                direction *= -1
                alien0_speed_x = randint(7, 10) * direction
                alien0_speed_y = randint(7, 10) * direction
                # Top and Bottom screen boundary
            if alien.y <= 20 or alien.height >= screenHeight:
                direction *= -1
                alien0_speed_x = randint(7, 10) * direction
                alien0_speed_y = randint(7, 10) * direction
            alien.x += alien0_speed_x
            alien.y += alien0_speed_y

        
    

        # if bot.x <= 20 or bot.x + bot.width >= screenWidth:
        #     direction *= -1
        #     alien_speed_x = randint(7, 10) * direction
        #     alien_speed_y = randint(7, 10) * direction
        #     # Top and Bottom screen boundary
        # if bot.y <= 20 or bot.height >= screenHeight:
        #     direction *= -1
        #     alien_speed_x = randint(7, 10) * direction
        #     alien_speed_y = randint(7, 10) * direction
        # bot.x += alien_speed_x
        # bot.y += alien_speed_y


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



def game_Intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)

            if event.type == pygame.QUIT:
                 pygame.quit()
        
        window.fill(255,255,255)
        # Global variables for displaying a main menu 
        smallFont = pygame.font.SysFont('Corbel', 30)
        text = smallFont.render('QUIT: ', 255, 255, 255)
        text1 = smallFont.render('START', 255, 255, 255)
        




def reDrawGameWindow():
    global dead_alien_index
    window.blit(space, (0, 0))
    p1.draw(window)
    for bullet in bullets:
        bullet.draw(window)
    if (dead != True):
        bot.draw(window)
        next_bot.draw(window)
  
    for asdf in aliens:
        asdf.draw(window)


    # bot1.draw2(window)

    pygame.display.update()


# def crash():    
    # print("The x is: " + stzr(bot.x) +
    #       " and x + width position of the alien is:" + str(bot.x + bot.width))
    # print("the y position of the alien is: " + str(bot.y))


# Initlizing objects
p1 = rocket(x, y, width, height)
bot = alien(alien_x, alien_y, width, height)
next_bot = alien(100, 200, width, height)
bot1 = alien(100, 200, width, height)
# Store all our projectile objects in a list
# Function for endgame()


def endGame():
    global oof
    run = True

    global current_score 

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
        score = current_score
        

        largeFont = pygame.font.SysFont('comicsans', 40)
        lastScore = largeFont.render('Best Score: ', 255, 255, 255)
        currentScore = largeFont.render(
            '       Score: ' + str(score), 1, (255, 255, 255))
        window.blit(currentScore, (width/2 - currentScore.get_width()/2, 240))
        pygame.display.update()


# clock.tick(60) ##  Means that for every second at most 40 frames should pass
track = 0
while run:
    

    track += 1
    clock.tick(30)

    if oof:
        endGame()
    else:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False

            



            keys = pygame.key.get_pressed()
            
            # if event.type == pygame.KEYDOWN:
            #      if event.key == pygame.K_a:
            #         aliens.append(alien(alien_x, alien_y, width, height))
            #         print(len(aliens))


            if keys[pygame.K_SPACE]:
                facing = -1
                if len(bullets) < 1:
                    bullets.append(projectile(
                        (p1.x + p1.width // 2), p1.y, 3, (150, 150, 150), facing))
                # crash()

            if keys[pygame.K_LEFT] and p1.x > 0:
                p1.x -= p1.vel
            if keys[pygame.K_RIGHT] and p1.x < screenWidth - p1.width:
                p1.x += p1.vel
            if keys[pygame.K_UP] and p1.y > 0:
                p1.y -= p1.vel
            if keys[pygame.K_DOWN] and p1.y < screenHeight - p1.height:
                p1.y += p1.vel
           
            if keys[pygame.K_q]:
                oof = True
       
       # This code generates a new alien every 30 milliseconds * 50 
        # if track % randint(50,100) ==0:
        #     aliens.append(alien(alien_x, alien_y, width, height))     
        #     print("new alien")
    

        for bullet in bullets:
            if bullet.y < 800 and bullet.y > 0:
                bullet.y += bullet.vel
            else:
                # this removes the bullet if its off the screen
                bullets.pop(bullets.index(bullet))

        for x, sneila in enumerate(aliens):
            sneila.selfMove()
            if bullets:
                last_bullet = bullets[len(bullets) - 1]
                if ((last_bullet.y <= (sneila.y + sneila.height)) and (last_bullet.y >= (sneila.y)) and (((last_bullet.x + last_bullet.radius) >= sneila.x) and ((last_bullet.x + last_bullet.radius) <= (sneila.x + sneila.width)))):                 
                    print("mini Alien Dead")
                    dead_alien_index = x 
                    aliens.pop(dead_alien_index)
                    current_score += 5
                    print(dead_alien_index)
   
     

        if bot.x <= 50 or (bot.x + bot.width) >= screenWidth:
            direction *= -1
            alien_speed_x = randint(7, 10) * direction
            alien_speed_y = randint(7, 10) * direction
            # Top and Bottom screen boundary
        if bot.y <= 50 or bot.height >= screenHeight - 100:
            direction *= -1
            alien_speed_x = randint(7, 10) * direction
            alien_speed_y = randint(7, 10) * direction
        

        if next_bot.x <= 50 or next_bot.x + next_bot.width >= screenWidth:
            direction *= -1
            alien1_speed_x = randint(1, 5) * direction
            alien1_speed_y = randint(1, 10) * direction
            # Top and next_bottom screen boundary
        if next_bot.y <= 50 or next_bot.height >= screenHeight - 100:
            direction *= -1
            alien1_speed_x = randint(1, 5) * direction
            alien1_speed_y = randint(1, 5) * direction
 
        bot.x += alien_speed_x
        bot.y += alien_speed_y
        next_bot.x += alien1_speed_x
        next_bot.y += alien1_speed_y
    
        if (bullets):
            last_bullet = bullets[len(bullets) - 1]
            if ((last_bullet.y <= (bot.y + bot.height)) and (last_bullet.y >= (bot.y)) and (((last_bullet.x + last_bullet.radius) >= bot.x) and ((last_bullet.x + last_bullet.radius) <= (bot.x + bot.width)))):
            
                bot.eatgudfoodandbehealthy -= 2
                bullets.pop(bullets.index(last_bullet))
                print(bot.eatgudfoodandbehealthy)
                if bot.eatgudfoodandbehealthy == 0:
                    dead = True                       
                    print(dead)
                    current_score += 5
                    print("KILLED")
        


        time_start = time.time()
        seconds = 0
        MOREalien = 0


            

        reDrawGameWindow()
pygame.quit()
