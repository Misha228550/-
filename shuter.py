import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = (SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Война в Сталинграде")

#Частота кадров
clock = pygame.time.Clock()
FPS = 120

#Действия игрока
moving_left = False
moving_right = False

BackRound = (32,74,209)

def draw_backroundt():
    screen.fill(BackRound)

class Soldier(pygame.sprite.Sprite):
    def __init__(self,carector_tipe,x,y,scale,speed):
        # Загрузка изображения персонажа
        pygame.sprite.Sprite.__init__(self)
        self.carector_tipe = carector_tipe
        self.speed=speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index=0
        self.action = 0
        self.updata_time = pygame.time.get_ticks()
        tenp_list = []
        for i in range(5):
            img = pygame.image.load(f"img/{self.carector_tipe}/Idle/{i}.png").convert_alpha()
            img = pygame.transform.scale(img,(img.get_width() * scale, img.get_height() * scale))
            tenp_list.append(img)
        self.animation_list.append(tenp_list)
        tenp_list = []
        for i in range(6):
            img = pygame.image.load(f"img/{self.carector_tipe}/Run/{i}.png").convert_alpha()
            img = pygame.transform.scale(img,(img.get_width() * scale, img.get_height() * scale))
            tenp_list.append(img)
        self.animation_list.append(tenp_list)
        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)

    def updata_animations(self):
        #оБНОВЛЕНИЕ АНИМАЦИЙ
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks() - self.updata_time > animation_cooldown:
            self.frame_index += 1
            self.updata_time = pygame.time.get_ticks()

            if self.frame_index >= len(self.animation_list[self.action]):
                self.frame_index = 0

    def updata_actiones(self,new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.updata_time = pygame.time.get_ticks()






    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)


    def move(self,moving_left,moving_right):
        #Обнулить переменные перемещения
        dx=0
        dy=0

        if moving_left:
            dx = - self.speed
            self.direction = -1
            self.flip = True
        if moving_right:
            dx = self.speed
            self.direction = 1
            self.flip = False

        #Обновление позиции игрока
        self.rect.x += dx
        self.rect.y += dy

#Персонаж
player = Soldier("player",200,300,2,3)
Zlodey = Soldier("enemy",300,300,2,3)


run = True
while run:
    draw_backroundt()
    player.draw()
    Zlodey.draw()

    if moving_left or moving_right:
        player.updata_actiones(1)
    else:
        player.updata_actiones(0)

    player.move(moving_left, moving_right)
    player.updata_animations()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        #Проверка нажатия клавиш
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        # Проверка нажатия клавиш
        # KEYUP - отжатие
        # KEYDOWN - нажатие
    pygame.display.update()
    clock.tick(FPS)