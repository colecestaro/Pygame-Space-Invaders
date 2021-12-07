# Lily England jww2fj Cole Cestaro uce8du

# Description:
# We want to replicate Space Invaders. The user-controlled space ship is on
# the bottom of the screen and can move left or right.
# Aliens fly in front of the space ship and try to hit it by flying forward.
# If the space ship kills all the aliens, the user wins.
# If any of the aliens touches the bottom of the screen, the user loses.

# Required Features
# 1. User Input - The user can use the left and right arrow keys to move and the space bar to shoot
# 2. Start Screen - The game loads with the start screen which has game name, student names (and IDs), and basic game
# instructions. The user can press 1(easy), 2(medium), or 3(hard) to start the game on the chosen level.
# 3. Game Over - When an alien touches the bottom of the screen, a game over screen is displayed.
# 4. Small Enough Window - Game window will be 800 x 600
# 5. Graphics and Images - Used images from online and edited them to create local image files.

# Optional Features
# 1. Restart from game over - Returns to start screen
# 2. Enemies - These are the aliens. They will spawn at the top of the screen and move down.
# 3. Timer - Displays in the winner post-game screen
# 4. Multiple levels - Easy, medium, and hard modes. As levels get harder, the speed and number of aliens increases.

import pygame
import gamebox
import time
import random


camera = gamebox.Camera(800, 600)
bullet_list = []
alien_list = []
time_of_last_bullet = 0
bawls = 1
num_aliens = 0
finish = 2
game_on = 0
coming_from_mode = 0
time_since_start = 0
clock = 0
loss_restart = 0

def winner(keys):
    '''
    Displays winner screen with time and resets variables
    :param keys: keyboard buttons
    '''
    global game_on
    global alien_list
    global finish
    global clock
    finish = 2
    alien_list = []
    camera.draw('YOU WIN!', 45, "green", 400, 200)
    camera.draw('Compare times with your friends!', 45, 'red', 400, 320)
    if clock < 300:
        camera.draw("Your Time Was: "+str(clock/3)[0]+'.'+str(clock/3)[1]+' seconds!', 45, 'red', 400, 250)
    if clock >= 300:
        camera.draw("Your Time Was: "+str(clock/3)[0:2]+'.'+str(clock/3)[4]+' seconds!', 45, 'red', 400, 250)
    if coming_from_mode == 1:
        camera.draw('Press 0 for start screen',30,'green',400,400)
        camera.draw('Press 1 to restart Easy Mode',30,'green',400,450)
        camera.draw('Press 2 to advance to Medium Mode',30,'green',400,500)
        if pygame.K_0 in keys:
            clock = 0
            game_on = 0
        if pygame.K_1 in keys:
            clock = 0
            game_on = 1
        if pygame.K_2 in keys:
            clock = 0
            game_on = 2
    if coming_from_mode == 2:
        camera.draw('Press 0 for start screen', 30,'green', 400, 400)
        camera.draw('Press 1 to go back to Easy Mode',30,'green',400,450)
        camera.draw('Press 2 to restart Medium Mode',30,'green',400,500)
        camera.draw('Press 3 to advance to Hard Mode',30,'green',400,550)
        if pygame.K_0 in keys:
            clock = 0
            game_on = 0
        if pygame.K_1 in keys:
            clock = 0
            game_on = 1
        if pygame.K_2 in keys:
            clock = 0
            game_on = 2
        if pygame.K_3 in keys:
            clock = 0
            game_on = 3
    if coming_from_mode == 3:
        camera.draw('Press 0 for start screen', 30,'green', 400, 400)
        camera.draw('Press 1 to go back to Easy Mode',30,'green',400,450)
        camera.draw('Press 2 to go back to Medium Mode',30,'green',400,500)
        camera.draw('Press 3 to restart to Hard Mode',30,'green',400,550)
        if pygame.K_0 in keys:
            clock = 0
            game_on = 0
        if pygame.K_1 in keys:
            clock = 0
            game_on = 1
        if pygame.K_2 in keys:
            clock = 0
            game_on = 2
        if pygame.K_3 in keys:
            clock = 0
            game_on = 3

def loser(keys):
    '''
    Displays Game Over screen, resets variables, and gives user option to restart or go back to home screen
    :param keys: keyboard buttons
    '''
    global game_on
    global alien_list
    global finish
    global clock
    global loss_restart
    loss_restart = 1
    clock = 0
    finish = 2
    alien_list = []
    camera.clear('black')
    camera.draw('YOU LOSE. GAME OVER', 45, "green", 400, 200)
    if coming_from_mode == 1:
        camera.draw('Press 0 for start screen', 30, 'green', 400, 400)
        camera.draw('Press 1 to restart to Easy Mode',30,'green',400,450)
        if pygame.K_0 in keys:
            clock = 0
            game_on = 0
        if pygame.K_1 in keys:
            clock = 0
            game_on = 1
    if coming_from_mode == 2:
        camera.draw('Press 0 for start screen', 30,'green', 400, 400)
        camera.draw('Press 2 to restart to Medium Mode',30,'green',400,450)
        if pygame.K_0 in keys:
            clock = 0
            game_on = 0
        if pygame.K_2 in keys:
            clock = 0
            game_on = 2
    if coming_from_mode == 3:
        camera.draw('Press 0 for start screen', 30,'green', 400, 400)
        camera.draw('Press 3 to restart to Hard Mode',30,'green',400,450)
        if pygame.K_0 in keys:
            clock = 0
            game_on = 0
        if pygame.K_3 in keys:
            clock = 0
            game_on = 3

def start_screen(keys):
    '''
    Displays the start screen, instructions, and game mode options
    :param keys: Keyboard buttons
    '''
    camera.draw("Space Invaders", 35, "Green", 400, 50)
    camera.draw("Lily England (jww2fj) and Cole Cestaro (uce8du)", 30, "blue", 400, 100)
    camera.draw("Instructions:", 30, "white", 400, 150)
    camera.draw("Use the left and right arrow keys to move.", 30, "white", 400, 200)
    camera.draw("Use the space bar to shoot the aliens.", 30, "white", 400, 250)
    camera.draw("If any of the aliens get past the space ship, the user loses.", 30, "white", 400, 300)
    camera.draw("If the space ship kills all the aliens, the user wins.", 30, "white", 400, 350)
    camera.draw("Press 1 for Easy Mode", 45, "green", 400, 425)
    camera.draw("Press 2 for Medium Mode", 45, "yellow", 400, 475)
    camera.draw("Press 3 for Hard Mode", 45, "red", 400, 525)

x = 400
y = 550
def move_ship(keys):
    '''
    Moves ship when left or right arrow keys are pressed, shoots bullet when space is pressed, and defines ship properties
    :param keys: Keyboard buttons
    '''
    global x
    global y
    ship = gamebox.from_image(x, y, 'spaceship2.png')
    ship.scale_by(.15)
    camera.draw(ship)
    if pygame.K_LEFT in keys and x > 20:
        x -= 10
    if pygame.K_RIGHT in keys and x < 780:
        x += 10
    if pygame.K_SPACE in keys:
        bullet(keys)

def aliens(keys):
    '''
    Randomly spawns alien locations and defines alien properties
    :param keys: Keyboard buttons
    '''
    global bawls
    if bawls == 1:
        for i in range(num_aliens):
            x = random.randrange(50, 750)
            y = random.randrange(0, 10)
            alien = gamebox.from_image(x,y,'alien.webp')
            alien.scale_by(.15)
            alien_list.append(alien)
    bawls = 2

def bullet(keys):
    '''
    Defines bullet properties, restricts bullet shooting to once a half-second
    :param keys: Keyboard buttons
    '''
    global time_of_last_bullet
    current_time = time.time()
    if current_time - time_of_last_bullet > 0.5:

        bullet = gamebox.from_color(x, y, 'red', 8, 8)
        bullet_list.append(bullet)

        time_of_last_bullet = time.time()

def timer(keys):
    '''
    Creates a timer that counts up when the game starts
    :param keys: Keyboard buttons
    '''
    global clock
    clock += 1
    secs = str(int((clock / 30) % 60))
    mins = str(int((clock / 30) / 60))
    frac_sec = str(int((clock % 30)/ 30*10))
    timer = gamebox.from_text(50, 100, mins + ':' + secs + '.' + frac_sec, 30, 'red', bold=False)
    camera.draw(timer)

def easy(keys):
    '''
    Easy mode game play - draws background, calls above functions, spawns aliens and defines their speed
    :param keys: Keyboard buttons
    '''
    global num_aliens
    global bawls
    global finish
    global game_on
    global coming_from_mode
    global loss_restart

    coming_from_mode = 1
    background = gamebox.from_image(400,300,'yeaaaaa.png')
    camera.draw(background)
    timer(keys)
    num_aliens = 3
    move_ship(keys)
    aliens(keys)

    for each in bullet_list:
        each.speedy -= 1
        each.move_speed()
        camera.draw(each)
    for each in alien_list:
        each.speedy = 2
        each.move_speed()
        camera.draw(each)
        if each.y >= 600:
            game_on = 11
    if finish == 1 and alien_list == []:
        game_on = 10
        finish = 2
    if finish == 2 and alien_list == []:
        aliens(keys)
        finish = 1
        bawls = 1
        for each in alien_list:
            each.speedy = 2
            each.move_speed()
            camera.draw(each)
            if each.y >= 600:
                game_on = 11
    if loss_restart == 1:
        finish = 2
        loss_restart = 0


def medium(keys):
    '''
    Medium mode game play - draws background, calls above functions, spawns aliens and defines their speed
    :param keys: Keyboard buttons
    '''
    global num_aliens
    global bawls
    global finish
    global game_on
    global coming_from_mode
    global loss_restart

    coming_from_mode = 2
    background = gamebox.from_image(400, 300, 'yeaaaaa.png')
    camera.draw(background)
    num_aliens = 5
    aliens(keys)
    move_ship(keys)
    timer(keys)


    for each in bullet_list:
        each.speedy -= 1
        each.move_speed()
        camera.draw(each)
    for each in alien_list:
        each.speedy = 2.25
        each.move_speed()
        camera.draw(each)
        if each.y >= 600:
            game_on = 11
    if finish == 1 and alien_list == []:
        game_on = 10
        finish = 2
    if finish == 2 and alien_list == []:
        aliens(keys)
        finish = 1
        bawls = 1
        for each in alien_list:
            each.speedy = 2.25
            each.move_speed()
            camera.draw(each)
            if each.y >= 600:
                game_on = 11
    if loss_restart == 1:
        finish = 2
        loss_restart = 0


def hard(keys):
    '''
    Hard mode game play - draws background, calls above functions, spawns aliens and defines their speed
    :param keys: Keyboard buttons
    '''
    global num_aliens
    global bawls
    global finish
    global game_on
    global coming_from_mode
    global loss_restart

    coming_from_mode = 3

    background = gamebox.from_image(400, 300, 'yeaaaaa.png')
    camera.draw(background)
    num_aliens = 8
    move_ship(keys)
    aliens(keys)
    timer(keys)


    for each in bullet_list:
        each.speedy -= 1
        each.move_speed()
        camera.draw(each)
    for each in alien_list:
        each.speedy = 2.5
        each.move_speed()
        camera.draw(each)
        if each.y >= 600:
            game_on = 11
    if finish == 1 and alien_list == []:
        game_on = 10
        finish = 2
    if finish == 2 and alien_list == []:
        aliens(keys)
        finish = 1
        bawls = 1
        for each in alien_list:
            each.speedy = 2.5
            each.move_speed()
            camera.draw(each)
            if each.y >= 600:
                game_on = 11
    if loss_restart == 1:
        finish = 2
        loss_restart = 0


def tick(keys):
    '''
    Runs 30 times a second, outlines game progression, and collision events
    :param keys: Keyboard buttons
    '''
    global game_on
    global finish
    camera.clear('black')
    if game_on == 0:
        start_screen(keys)
        if pygame.K_1 in keys:
            game_on = 1
        if pygame.K_2 in keys:
            game_on = 2
        if pygame.K_3 in keys:
            game_on = 3
    if game_on == 1:
        easy(keys)
    if game_on == 2:
        medium(keys)
    if game_on == 3:
        hard(keys)
    if game_on == 10:
        finish = 2
        winner(keys)
    if game_on == 11:
        finish = 2
        loser(keys)
    for each1 in alien_list:
        for bullet in bullet_list:
            if bullet.touches(each1):
                alien_list.remove(each1)
                bullet_list.remove(bullet)
    camera.display()

gamebox.timer_loop(30, tick)