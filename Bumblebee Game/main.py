import pgzrun
import random
HEIGHT=500
WIDTH=500
game_over=False
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
 if game_over==True:
  screen.fill("yellow")
  screen.draw.text("Time has run out! you got {} flowers in 60 secs".format(score), center=(200, 200), color="red")


def update():
 #global always used after function start (if needed)
 global score

 if keyboard.w:
 # print("up")
  bee.y=bee.y-10
 if keyboard.s:
  
  bee.y=bee.y+10
 if keyboard.a:
  bee.x=bee.x-10
 if keyboard.d:
  bee.x=bee.x+10

 if bee.colliderect(flower): 
  score=score+1
  
  ypos=random.randint(50,400)
  xpos=random.randint(50,400)
  flower.y=ypos
  flower.x=xpos

def timer():
 global game_over
 game_over=True
 

# flower.pos=random.randint((50, 400), (50, 400))


clock.schedule(timer, 60)
pgzrun.go()