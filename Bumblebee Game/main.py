import pgzrun
import random
HEIGHT=500
WIDTH=500
bee=Actor("bee")
bee.pos=100, 100
flower=Actor("flower")
flower.pos=150, 150
score=0


def draw():
 screen.blit("backround", (0,0))
 bee.draw()
 flower.draw()
 screen.draw.text("your score is "+ str(score), center=(50, 200))

def update():

 if keyboard.up:
 # print("up")
  bee.y=bee.y-5
 if keyboard.down:
  
  bee.y=bee.y+5
 if keyboard.left:
  bee.x=bee.x-5
 if keyboard.right:
  bee.x=bee.x+5

if bee.colliderect(flower): 
 score=score+1
 ypos=random.randint(50,400)
 xpos=random.randint(50,400)
 flower.y=ypos
 flower.x=xpos


# flower.pos=random.randint((50, 400), (50, 400))



pgzrun.go()