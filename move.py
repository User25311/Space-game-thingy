import pygame 
from random import randint
pygame.init() ## Used to initalize all the rquired modules of pygame
screenWidth = 800
screenHeight = 800

window = pygame.display.set_mode((screenWidth,screenHeight)) # Used to display a window of the desired size 

pygame.display.set_caption("Space Game") # Sets the window title

x = 400 # starting x coordinate
y =  600# Starting y coordinate
radius = 50
width = 100 #Dimensions of the object (width)
height = 100 #Dimesions of the object (height)


## Starting alien properities
alien_x = 400 # starting x coordinate
alien_y =  100# Starting y coordinate
#Starting speed of alien
alien_speed_x = 50
alien_speed_y = 50
# Creating variable for alien starting direction
direction = 1

clock = pygame.time.Clock() # Used to control the frames per second and thus the game speed 
run = True #Indiciate that pygame is running and 'while' loop is used
ship = pygame.image.load("./assets/rocket.png")
ship = pygame.transform.scale(ship, (width,height))
ufo = pygame.image.load("./assets/ufo.png")
ufo = pygame.transform.scale(ufo, (width,height))
ufo2 = pygame.image.load("./assets/ufo#2.png")
ufo2 = pygame.transform.scale(ufo2, (width,height))
space = pygame.image.load("./assets/Space.jpeg")
space = pygame.transform.scale(space, (screenWidth,screenHeight))

music = pygame.mixer.music.load('./assets/universe-space-sounds-3595.mp3')
pygame.mixer.music.play(-1)

class rocket(object):
    def __init__(self, x ,y, width, height):
        self.x = x 
        self.y = y
        self.width = width
        self.height = height

        ## Predefined properties
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


   


    #  1. Create a function that draws the aliens in a random position
    #  2. Create a function responsible for moving the alien in random directions

class projectile(object):
    def __init__(self, x, y, radius, colour, direction):
        self.x = x 
        self.y = y
        self.radius = radius
        self.colour = colour
        self.direction = direction
        self.vel = 20 * direction

    def draw(self, window):
        pygame.draw.circle(window, self.colour, (self.x,self.y), self.radius)


## Homework Create a alien class


 
def reDrawGameWindow():
    window.blit(space, (0,0))
    p1.draw(window)
    bot.draw(window)
    # bot1.draw2(window)
    for bullet in bullets:
        bullet.draw(window)
           
    pygame.display.update()
    






p1 = rocket(x, y, width, height)
bot = alien(alien_x, alien_y, width, height)
# bot1 = alien(100, 200, width, height)
## Store all our projectile objects in a list
bullets = [] 
clock.tick(60)
while run:

   

   


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
        for bullet in bullets:
            if bullet.y < 800 and bullet.y > 0:
                bullet.y += bullet.vel
            else:
                bullets.pop(bullets.index(bullet)) # this removes the bullet if its off the screen
         
        # Responsible for random alien movements:
        if bot.x <= 20 or bot.x + bot.width >= screenWidth:
            direction *= -1
            alien_speed_x = randint(10, 30) * direction
            alien_speed_y = randint(10, 30) * direction

        # Top and Bottom screen boundary 
        if bot.y <= 20 or bot.height >= screenHeight:
            direction *= -1
            alien_speed_x = randint(15, 40) *direction
            alien_speed_y = randint(15, 40) *direction

        
        
        bot.x += alien_speed_x
        bot.y += alien_speed_y



            
        keys = pygame.key.get_pressed()
        # 1. Add Up, remember to stop moving up once we have reached the top
        # 2. Add Down, remember to astop moving down once we have reached the bottom
        if keys[pygame.K_LEFT] and p1.x > 0:
            p1.x -= p1.vel
        if keys[pygame.K_RIGHT] and p1.x < screenWidth - p1.width:
            p1.x += p1.vel
        if keys[pygame.K_UP] and p1.y > 0:
            p1.y -= p1.vel
        if keys[pygame.K_DOWN] and p1.y < screenHeight - p1.height:
            p1.y += p1.vel
        if keys[pygame.K_SPACE]:
            facing = -1
            if len(bullets) < 5: ## This will make sure we cannot exceed 15 bullets on the screen
                bullets.append(projectile((p1.x + p1.width // 2) , p1.y, 6, (150,150,150), facing))

        
        reDrawGameWindow()

pygame.quit()

