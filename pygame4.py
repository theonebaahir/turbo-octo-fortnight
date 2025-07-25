import pygame
pygame.init()
window = pygame.display.set_mode((400,400))
window.fill((155, 66, 55))
green = (125, 155, 145)
pygame.draw.circle(window, green, (150, 200),50)
pygame.draw.circle(window, green, (115, 125),50,3)
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
