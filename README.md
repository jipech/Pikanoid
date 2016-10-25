# Pikanoid

This is Arkanoid (Breakout) game for the RaspBerry Pi with add-on board Sense Hat.
It is writen in Python with support sensehat library. The [pygame library](http://www.pygame.org/wiki/GettingStarted) is also required.
The complete source code is in the file `arkanoid.py`. You can use both python2 and python3.

## Prerequisities

### Hardware

- Raspberry Pi
- Sense Hat

### Software

- Up-to-date Raspbian

## Download and run

Download this repo and run `arkanoid.py` with Python

```
git clone https://github.com/jipech/Pikanoid
cd Pikanoid
python3 arkanoid.py
```

The controll of the game is by the joystick on the Sense Hat board. If you finish game (good or bad), then you can choose:
- another game - joystick left
- end - joystick right
If you like autostart game after booting your Raspberry Pi, then you add line to your crontab:
```
crontab -e
@reboot python3 /home/pi/Pikanoid/arkanoid.py
```
and exit crontab editor (e.g. F2 for nano). You may have to change `/home/pi/arkanoid.py` to your path to the program.

## Setting game

If you wanna change any beahviour of the game, you can do it in the start_set() procedure. This procedure is calling every time before start the game. You can change this variable:
- surface - main desktop of the game, you can add or remove the line of the brick or prepare your own design of the wall
- win, lost - this desktop is shown, when you win or lost a game
- bx, by - starting position of the ball (x=0 - up, x=7 - down, y=0 - left, y=7 - right)
- px, py - starting position of the paddle
- dir, up - starting direction of the ball (default is up and right) (dir=0 - left, dir= - right, up=1 - up, up=0 - down)
- bricks - number of the bricks
- iter - if ball in iter cycles dont touch a brick, the trace of the ball is changed. This is necessary to complet the game.

## Todo

It is possible to add next features:
- compute the score
- add the next levels with different design of the wall
- add the control by the declination of the sense hat
- change the style or the color of the ball, paddle, wall
