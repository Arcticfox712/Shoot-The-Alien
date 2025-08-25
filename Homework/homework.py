import pgzrun
import random
HEIGHT=500
WIDTH=500
bee=Actor("redball")
bee.pos=0, 0
score=0

def draw():
    bee.draw()

def update():

 if keyboard.up:
  bee.y=bee.y-5

 if keyboard.down:
  bee.y=bee.y+5
  print("works")
 if keyboard.left:
  bee.x=bee.x-5

 if keyboard.right:
  bee.x=bee.x+5

pgzrun.go()