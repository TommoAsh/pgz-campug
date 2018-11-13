import time

import datetime

WIDTH = 1024
HEIGHT = 384

alien = Actor('alien')
alien.pos = (50, 320)
alien_movable = True

hit_time = datetime.datetime.now()

rock = Actor('rock', (20, 20))
rock.pos = (950, 320)
rock_speed = 2

def draw():
    screen.clear()
    alien.draw()
    rock.draw()

def set_alien_normal():
    alien.image = 'alien'
    global alien_movable
    alien_movable = True

def alien_hit():
    # survival_time = (datetime.datetime.now() - hit_time).toseconds()
    screen.draw.text("hello world", (100, 100), color="orange", fontsize=32)
    hit_time = datetime.datetime.now()
    alien.image = 'alien_hurt'
    global alien_movable
    alien_movable = False
    global rock_speed
    rock_speed = 2
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def update():
    if alien_movable:
        if keyboard[keys.UP]:
            if alien.y > 200:
                alien.y -= 3
        elif alien.y < 320:
            alien.y += 3
        if keyboard[keys.LEFT] and alien.left > 0:
            alien.x -= 3
        if keyboard[keys.RIGHT] and alien.right < WIDTH:
            alien.x += 3
    global rock_speed
    rock.x -= rock_speed
    if rock.x <= 0:
        rock_speed += 1
        rock.x = 1000
        rock.y = random(60)
    if abs(rock.x - alien.x) < 30 and abs(rock.y - alien.y) < 20:
        alien_hit()