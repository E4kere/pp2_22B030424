import pygame

pygame.init()
pygame.display.set_caption("My Game")


monitor = pygame.display.set_mode((800, 400))

check = True
s = pygame.Surface((80, 100))
while check:
    
    monitor.fill((255, 192, 203))
    monitor.blit(s, (50, 50))
    pygame.draw.circle(monitor, 'Green', (200, 200), 20)

    pygame.display.update()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            check = False
            pygame.quit()