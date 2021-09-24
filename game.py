import pgzrun
import random
TITLE = "Zombies vs Tanks"
WIDTH = 800
HEIGHT = 640

UP = 180
DOWN = 0
LEFT = 270
RIGHT = 90
BULLET_SPEED = 10

blue_tank = Actor("tank_blue")
blue_tank.x=WIDTH/2
blue_tank.y=HEIGHT/2

bullet = Actor("bulletblue")
bullet_fired = False


bullet = Actor("bulletblue")
BULLET_SPEED = 10

zombie_list = []
ZOMBIE_SPEED = 1

score = 0
game_over = False

def draw():
    if not game_over:
        screen.blit("tank.png", (0,0))
        blue_tank.draw()
        bullet.draw()
        clock.schedule(shoot_bullet, 5)

        clock.schedule(create_zombies, 5)
        move_zombie()
        screen.draw.text(f"score: {score} ",  (350, 150))
    else:
        screen.fill("blue")
        screen.draw.text(f"GAME OVER, Your score: {score} ",  (350, 150))

def update():
    global bullet_fired
    if keyboard.left:
        blue_tank.x = blue_tank.x - 5
        blue_tank.angle = LEFT
    if keyboard.right:
        blue_tank.x = blue_tank.x + 5
        blue_tank.angle = RIGHT
    if keyboard.up:
        blue_tank.y = blue_tank.y - 5
        blue_tank.angle = UP
    if keyboard.down:
        blue_tank.y = blue_tank.y + 5
        blue_tank.angle = DOWN
    if keyboard.space:
        if not bullet_fired:
            bullet_fired = True
            sounds.laserretro_004.play()
            if blue_tank.angle == LEFT:
                bullet.x = blue_tank.x-30
                bullet.y = blue_tank.y

            elif blue_tank.angle == RIGHT:
                bullet.x = blue_tank.x+30
                bullet.y = blue_tank.y

            elif blue_tank.angle == DOWN:
                bullet.x = blue_tank.x
                bullet.y = blue_tank.y + 30

            elif blue_tank.angle == UP:
                bullet.x = blue_tank.x
                bullet.y = blue_tank.y - 30

def shoot_bullet():
    global bullet_fired
    global blue_tank
    global bullet
    if bullet_fired:
        if blue_tank.angle  == LEFT:
            bullet.x -= BULLET_SPEED
        elif blue_tank.angle  == RIGHT:
            bullet.x += BULLET_SPEED
        elif blue_tank.angle  == DOWN:
            bullet.y += BULLET_SPEED
        elif blue_tank.angle  == UP:
            bullet.y -= BULLET_SPEED

        if bullet.x >= WIDTH or bullet.x <=0 or bullet.y >=HEIGHT or bullet.y <=0:
            bullet_fired = False

def create_zombies():
    if len(zombie_list ) < 10 :
        loc_rand = random.randint(0,3)
        if loc_rand == 0:
            y = random.randint(40, HEIGHT-40)
            z = Actor("zombie_stand.png")
            z.x = 1
            z.y = y
            zombie_list.append(z)
        elif loc_rand == 1:
            y = random.randint(40, HEIGHT-40)
            z = Actor("zombie_stand.png")
            z.x = WIDTH-1
            z.y = y
            zombie_list.append(z)
        elif loc_rand == 2:
            x = random.randint(40, WIDTH-40)
            z = Actor("zombie_stand.png")
            z.y = 1
            z.x = x
            zombie_list.append(z)
        elif loc_rand == 3:
            x = random.randint(40, WIDTH-40)
            z = Actor("zombie_stand.png")
            z.y = HEIGHT - 1
            z.x = x
            zombie_list.append(z)

def move_zombie():
    global score,game_over
    for zomb in zombie_list:
        if zomb.x < blue_tank.x:
            zomb.x += ZOMBIE_SPEED
        elif zomb.x > blue_tank.x:
            zomb.x -= ZOMBIE_SPEED
        elif zomb.y < blue_tank.y:
            zomb.y += ZOMBIE_SPEED
        elif zomb.y > blue_tank.y:
            zomb.y -= ZOMBIE_SPEED
        for zomb in zombie_list:
            zomb.draw()
            if zomb.colliderect(bullet):
                zombie_list.remove(zomb)
                score += 1
            if zomb.colliderect(blue_tank):
                game_over = True


pgzrun.go()
