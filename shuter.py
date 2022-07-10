import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = (SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Война в Сталинграде")

class Soldier(pygame.sprite.Sprite):
    def __init__(self,x,y,scale):
        pygame.sprite.Sprite.__init__(self)
        img = pygame.image.load("img/player/Idle/0.png")
        self.image = pygame.transform.scale(img,(img.get_width() * scale, img.get_height() * scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def draw(self):
        screen.blit(self.image,self.rect)


player = Soldier(200,300,2)
player2 = Soldier(300,300,2)


run = True
while run:
    player.draw()
    player2.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
