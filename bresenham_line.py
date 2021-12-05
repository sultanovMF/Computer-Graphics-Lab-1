import pygame
screen_width, screen_height = 500, 500

rect_width, rect_height = 1, 1
vel = 2
black = (0, 0, 0)
white = (255, 255, 255)
pygame.init()
win = pygame.display.set_mode((screen_width, screen_height))
screen = pygame.Surface((screen_width, screen_height))

run = True

x1, y1, x2, y2 = 0,0,400, 200

def Draw(x, y):
    pygame.draw.rect(screen, white, (x, y, rect_width, rect_height))


d = 100
while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(black)
    dx = x2 - x1
    dy = y2 - y1
    D = 2 * dy - dx
    y = y1

    for x in range(x1, x2):
        Draw(x, y)
        if D > 0:
            y += 1
            D = D - 2*dx
        else:
            D = D + 2 * dy
    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
    pygame.display.update()
pygame.quit()