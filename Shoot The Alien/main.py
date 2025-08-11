import pgzrun
#import pygame
import random
WIDTH=500
HEIGHT=500
message= ""
score=0
TITLE="Shoot The Alien"
#redball=Actor("redballhw")
alien=Actor("alien")
alien.pos=100, 100
#redball.pos=200, 200
#redball._surf = pygame.transform.scale (redball._surf, (100, 100))


def place_alien():
    alien.x=random.randint(100, 400)
    alien.y=random.randint(100, 400)
#def place_redball():
#    redball.x= 20
#    redball.y= 20
def draw():
    screen.fill(color=(10, 0, 150))
    
    alien.draw()
    screen.draw.text(message, center=(300,10))
    screen.draw.text ("score"+str(score), center=(50, 20))
#  redball.draw()

def on_mouse_down(pos):
    global message, score
    if alien.collidepoint(pos):
        message="good shot!"
        score=score+1
        place_alien()
    else:
        message="you missed"
    
 
#place_redball() 
 
place_alien() 
pgzrun.go()