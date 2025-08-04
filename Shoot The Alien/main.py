import pgzrun
import random
WIDTH=500
HEIGHT=500
TITLE="Shoot The Alien"
alien=Actor("alien")
alien.pos=100, 100


def place_alien():
    alien.x=random.randint(100, 400)
    alien.y=random.randint(100, 400)
def draw():
    screen.fill(color=(10, 0, 150))
    alien.draw()
    
 
 
 
place_alien() 
pgzrun.go()