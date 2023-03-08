import pygame
pygame.init()


sc=pygame.display.set_mode((600,400))
pygame.display.set_caption("Моя первая игра на pygame")
pygame.display.set_icon(pygame.image.load('play.bmp'))

pygame.draw.rect(sc,(255,255,255),(10,10,50,100))
pygame.display.update()

clock = pygame.time.Clock()
FPS=60

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    clock.tick(FPS)