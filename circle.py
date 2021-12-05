import pygame
import random

random.seed()
screen_width, screen_height = 500, 500

rect_width, rect_height = 1, 1
vel = 2
black = (0, 0, 0)
white = (255, 255, 255)
pygame.init()
win = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.Surface((screen_width, screen_height))

run = True


def Draw(x, y, color):
    # print(color)
    pygame.draw.rect(screen, color, (x, y, rect_width, rect_height))


def DrawCircle(xc, yc, xx, yy):
    Draw(xc + xx, yc + yy, white)
    Draw(xc - xx, yc + yy, white)
    Draw(xc + xx, yc - yy, white)
    Draw(xc - xx, yc - yy, white)
    Draw(xc + yy, yc + xx, white)
    Draw(xc - yy, yc + xx, white)
    Draw(xc + yy, yc - xx, white)
    Draw(xc - yy, yc - xx, white)


def CircleBresenham(xc, yc, r):
    xx = 0
    yy = r
    d = 3 - 2*r
    DrawCircle(xc, yc, xx, yy)
    while yy >= xx:
        xx += 1
        if d > 0:
            yy -= 1
            d = d + 4 * (xx - yy) + 10
        else:
            d = d + 4 * xx + 6;
        DrawCircle(xc, yc, xx, yy)


def is_inside_circle(xx, yy, xc, yc, r):
    return (xx - xc)**2 + (yc - yy)**2 < r**2


def FillZone(xx, yy, color):
    c = screen.get_at((xx, yy))
    if ((c != white) and (c != color)):
        Draw(xx, yy, color)
        FillZone(xx, yy + 1, color)
        FillZone(xx, yy - 1, color)
        FillZone(xx + 1, yy, color)
        FillZone(xx - 1, yy, color)
        # FillZone(xx - 1, yy, color)
        # FillZone(xx, yy+1, color)

r1 = random.randint(100, 150)
r1 = 20
r2 = r1


x1, y1 = random.randint(r1, 500 - 2 * r1), random.randint(r1, 500 - 2 * r1)
length_between_center = random.randint(int(2 * r1 / 3), r1)
x2 = x1 + bool(random.getrandbits(1)) * length_between_center
y2 = y1 + bool(random.getrandbits(1)) * length_between_center

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(black)
    # print(x1, y1, r1)
    CircleBresenham(x1, y1, r1)
    CircleBresenham(x2, y2, r2)

    FillZone(int((max(x1, x2) + min(x1, x2))/2), int((max(y1, y2) + min(y1, y2))/2), pygame.Color(0, 255, 0))
    FillZone(x1 - r1 + 1 if x1 <= x2 else x1 + r1 - 1, y1, pygame.Color(255, 0, 0))
    FillZone(x2 + r2 - 1 if x1 <= x2 else x2 - r2 + 1, y2,  pygame.Color(0, 0,255))
    # FillZone(x2 + r2 - 1 if x1 < x2 else x2 - r2 + 1, y1, pygame.Color(254, 123, 116))
    # FillZone(x2, y2, pygame.Color(0, 0, 255))
    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
    pygame.display.update()
pygame.quit()