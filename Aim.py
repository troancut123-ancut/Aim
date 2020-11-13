import pgzrun
import pygame
from random import randint

apple = Actor("apple")
WIDHT = 1600

HEIGHT = 900

RED = 255,0,0
pos1x =100
pos1y =100



def draw():
    screen.clear()
    screen.surface = pygame.display.set_mode((WIDHT, HEIGHT))
    screen.fill((255,224,157))
    apple.draw()       
def place_apple():
    apple.x = randint(100,1500)
    apple.y = randint(100,800)
place_apple()

def on_mouse_down(pos):
    
    if apple.collidepoint(pos):
        
        place_apple()
    else:
        print("NOOB")
pgzrun.go()