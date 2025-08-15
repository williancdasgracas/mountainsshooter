import pygame

print('stup start')
pygame.init()

window = pygame.display.set_mode(size=(600, 480))
print('stup end')
print('lopp start')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()