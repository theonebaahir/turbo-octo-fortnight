import pygame
pygame.init()

SCREENWIDTH, SCREENHEIGHT = 500, 500
displaysurface = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))


pygame.display.set_caption('adding image and background image')

backgroundimage = pygame.transform.scale(pygame.image.load('background.png').convert(),(SCREENWIDTH, SCREENHEIGHT ))
penguin_image = pygame.transform.scale(pygame.image.load('hello penguin.png').convert_alpha(), (200))
penguin_rect = penguin_image.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 30))
text = pygame.font.Font(None, 36).render('hello world', True, pygame.color('black'))
text_rect = text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 110))

def game_loop():
    clock = pygame.time.clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        displaysurface.blit(backgroundimage, (0,0))
        displaysurface.blit(backgroundimage, penguin_rect)
        displaysurface.blit(text, text_rect, )
        
        pygame.display.flip()
        clock.tick(30)
    pygame.quit()
    
if __name__ == '__main__':
    game_loop
        