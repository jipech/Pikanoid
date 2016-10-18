# Pikanoid

This is Arkanoid (Breakout) game for the RaspBerry Pi with add-on board Sense Hat.
It is writen in Python with support sensehat library. The [pygame library](http://www.pygame.org/wiki/GettingStarted) is also required.
The complete source code is in the file arkanoid.py. You can use both python2 and python3.

## Prerequisities

### Hardware

- Raspberry Pi
- Sense Hat

### Software

- The updated Raspbian
- [Sense Hat software](https://www.raspberrypi.org/learning/getting-started-with-the-sense-hat/requirements/software/)
- Installed the pygame library:

  ```
  apt-get install python-pygame
  apt-get install python3-pygame
  ```
## Installation
You need only the file arkanoid.py. Place it as you wish.

## Running
You can run the program by typing:
```
sudo python arkanoid.py
```
or
```
sudo python3 arkanoid.py
```
The controll of the game is by the joystick on the Sense Hat board. If you finish game (good or bad), then you can choose:
- another game - joystick left
- end - joystick right
If you like autostart game after booting your Raspberry Pi, then you add line to your crontab:
```
crontab -e
@reboot /usr/bin/python /home/pi/arkanoid.py
```
and exit crontab editor (e.g. F2 for nano). You have to change ```/home/pi/arkanoid.py``` to your path to the program.

## Setting game

If you wanna change any beahviour of the game, you can do it in the start_set() procedure. This procedure is calling every time before start the game. You can change this variable:
- surface - main desktop of the game, you can add or remove the line of the brick or prepare your own design of the wall
- win, lost - this desktop is shown, when you win or lost a game
- bx, by - starting position of the ball (x=0 - up, x=7 - down, y=0 - left, y=7 - right)
- px, py - starting position of the paddle
- dir, up - starting direction of the ball (default is up and right) (dir=0 - left, dir= - right, up=1 - up, up=0 - down)
- bricks - number of the bricks
- iter - if ball in iter cycles dont touch a brick, the trace of the ball is changed. This is necessary to complet the game.
