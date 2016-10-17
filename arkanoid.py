from sense_hat import SenseHat
from time import sleep

import pygame
from pygame.locals import *

pygame.init() #For joystick
pygame.display.set_mode() #It is neccessary
pygame.key.set_repeat(500,500) #Repeat keybord (hold joystick) is enabled

sense = SenseHat()
sense.clear()

#Define colors
r = (255,0,0) #red
g = (0,255,0) #green
b = (0,0,0)   #black
w = (255,255,255) #white

# x = from left upper corner down
# y = from left upper corner right

def start_set(): #Initial settings 
   global surface,win,lost,bx,by,px,py,dir,up,iter,bricks,bricks2
   # Define desktop
   surface = [[r,r,r,r,r,r,r,r],
              [r,r,r,r,r,r,r,r],
              [b,b,b,b,b,b,b,b],
              [b,b,b,b,b,b,b,b],
              [b,b,b,b,b,b,b,b],
              [b,b,b,b,b,b,b,b],
              [b,b,b,b,b,b,b,b],
              [b,b,b,b,b,b,b,b]]

   win =  [[b,b,g,g,g,g,b,b],
           [b,g,b,b,b,b,g,b],
           [g,b,g,b,b,g,b,g],
           [g,b,b,b,b,b,b,g],
           [g,b,g,b,b,g,b,g],
           [g,b,b,g,g,b,b,g],
           [b,g,b,b,b,b,g,b],
           [b,b,g,g,g,g,b,b]]

   lost = [[b,b,r,r,r,r,b,b],
           [b,r,b,b,b,b,r,b],
           [r,b,r,b,b,r,b,r],
           [r,b,b,b,b,b,b,r],
           [r,b,b,r,r,b,b,r],
           [r,b,r,b,b,r,b,r],
           [b,r,b,b,b,b,r,b],
           [b,b,r,r,r,r,b,b]]

   bx=6 #x position of ball
   by=4 #y position of ball
   px=7 #x position of paddle
   py=4 #y position of paddle
   #Starting position of ball
   surface[bx][by]=g
   surface[px][py]=w
   dir=1 #direction of ball
      #1 = right, 0 = left
   up=1  #1 = up, 0 = down
   bricks = 16 #Number of bricks
   bricks2 = 16 #Number of bricks last
   iter = 0 #Iteration without change number of balls

def move_ball():
   global py, px,bx,by,dir,up,bricks,bricks2,iter
   surface[bx][by]=b
   
   if (up): #Ball goes up
      if (bx > 2): #Ball is not close to brick
         bx=bx-1
         if (dir): # Ball goes to right
            if (by == 7): #Ball is on the right side
               by = 6
               dir=0
            else: #Ball is not on the right side
               by = by+1
         else: #Ball goes left
            if (by == 0): # Ball is on left side
               by=1
               dir=1
            else: # Ball is not on the left side
               by=by-1
      elif (bx == 0): #Ball is in upper line
         bx=1
         up = 0 #Go down
         if (dir): #Ball goes right
            if (by==7): #Ball is on the right side
               by=6
               dir=0 #Go left
            else: # Ball is not on the right side
               if (surface[1][by+1]==r): #There is the brick
                  surface[1][by+1]=b
                  by=by-1
                  dir=0
                  bricks=bricks-1
               else:
                  by=by+1
         else: #Ball goes left
            if (by == 0): # Ball is on the left side
               by=1
               dir=1 # Go right
            else: # Ball is not on the left side
               if (surface[1][by-1]==r): #There is the brick
                  surface[1][by-1]=b
                  by=by+1
                  dir=1
                  bricks=bricks-1
               else:
                  by=by-1
      else: #There could be a brick
         if (dir): # Ball goes right
            if (by == 7): # Ball is on righ side
               if (surface[bx-1][6]==r): #There is the brick
                   surface[bx-1][6]=b
                   dir=0 #Go down and left
                   up=0
                   by=6
                   bx=bx+1
                   bricks=bricks-1
               else: # No brick
                   dir=0 #Go left and up
                   by=6
                   bx=bx-1
            else: # Ball is not on the right side
               if (surface[bx-1][by+1]==r): # There is the brick
                   surface[bx-1][by+1]=b
                   dir=0 # Go down and left
                   up=0 
                   bx=bx+1
                   by=by-1
                   bricks=bricks-1
               else: #There is no brick
                   bx=bx-1
                   by=by+1
         else: # Ball goes left
            if (by == 0): # Ball is on left side
               if (surface[bx-1][1]==r): #There is the brick
                   surface[bx-1][1]=b
                   dir=1 #Go down and right
                   up=0
                   by=1
                   bx=bx+1
                   bricks=bricks-1
               else: # No brick
                   dir=1 #Go right and up
                   by=1
                   bx=bx-1
            else: # Ball is not on the left side
               if (surface[bx-1][by-1]==r): # There is the brick
                   surface[bx-1][by-1]=b 
                   dir=1 # Go down and right
                   up=0 
                   bx=bx+1
                   by=by+1
                   bricks=bricks-1
               else: #There is no brick
                   bx=bx-1
                   by=by-1

 
   else: #Ball goes down
      if (bx==7): #Ball miss paddle, end game
         return True
      elif (bx==6): #Ball is on penult line
         if (dir): # Ball goes to right
            if (by == 7): #Ball is on the right side
               if ((surface[7][7]==w) or (surface[7][6]==w)): #Paddle is down from ball
                  bx=5
                  by=6
                  dir=0
                  up=1
               else:  #Paddle is not under ball, game over
                  bx=7
                  by=6
                  return True
            else: #Ball is not on the right side
               if (surface[7][by+1]==w): #paddle is down and right
                  bx=5
                  by=by-1
                  dir=0
                  up=1
               elif (surface[7][by]==w): #paddle is under ball
                  bx=5
                  by=by+1
                  up=1
               else: # Paddle is not under ball, game over
                  bx=7
                  by=by+1
                  return True
         else: #Ball goes to the left
            if (by == 0): #Ball is on the left side
               if ((surface[7][0]==w) or (surface[7][1]==w)): #Paddle is down from ball
                  bx=5
                  by=1
                  dir=1
                  up=1
               else:  #Paddle is not under ball, game over
                  bx=7
                  by=1
                  return True
            else: #Ball is not on the left side
               if (surface[7][by-1]==w): #paddle is down and left
                  bx=5
                  by=by+1
                  dir=1
                  up=1
               elif (surface[7][by]==w): #paddle is under ball
                  bx=5
                  by=by-1
                  up=1
               else: # Paddle is not under ball, game over
                  bx=7
                  by=by-11
                  return True
         if (bricks2==bricks): #In last  move we miss brick
            if (iter>4):
               if (up): #Ten times we not hit the brick and ball goes up
                  bx = bx-1
            else:
               iter = iter + 1
         else: #In last move we hit brick
            bricks2 = bricks
            iter = 0
         #print (bricks,bricks2,iter)
      else: #Ball is from line 1 to line 5
         bx=bx+1
         if (dir): # Ball goes to right
            if (by == 7): #Ball is on the right side
               by = 6
               dir=0
            else: #Ball is not on the right side
               by = by+1
         else: #Ball goes left
            if (by == 0): # Ball is on left side
               by=1
               dir=1
            else: # Ball is not on the left side
               by=by-1
   surface[bx][by]=g
   return False

def move_paddle():
   global py,px
   for event in pygame.event.get():
      if event.type == KEYDOWN:
         if event.key == K_LEFT:
            if (py>0):
               surface[px][py]=b
               py=py-1
               surface[px][py]=w
         elif event.key == K_RIGHT:
            if (py<7):
               surface[px][py]=b
               py=py+1
               surface[px][py]=w
#         elif event.key == K_RETURN:
#            return True
   return False



while True:
   #Main loop of game
   start_set()
   while True:
      sense.set_pixels(sum(surface,[]))
      sleep(0.5)
      if (move_paddle()):
         break
      if (move_ball()):
         break
      if not(bricks):
         break
   #Result of game
   if bricks:
      sense.set_pixels(sum(lost,[]))
      brick=str(bricks)
      msg="You lost. "+brick+" bricks left"
   else:
      sense.set_pixels(sum(win,[]))
      msg="You won"
   sleep(3)
   sense.show_message(msg, scroll_speed=0.1)
   sleep(1)
   msg="Another game? <- Yes, -> No"
   sense.show_message(msg, scroll_speed=0.1)
   sense.clear()
   k=1
   while (k):
     for event in pygame.event.get():
        if event.type == KEYDOWN:
          if event.key == K_LEFT:
            sleep(0.5)
            konec=0
            k=0
          elif event.key == K_RIGHT:
            konec=1
            k=0
   if (konec):
       break
