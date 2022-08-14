import pygame
import os
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = (SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Война в Сталинграде")

#Частота кадров
clock = pygame.time.Clock()
FPS = 60

Gravitazya = 0.75 #Гравитация

#Действия игрока
moving_left = False
moving_right = False

BackRound = (32,74,209) #Заливка фона
RET = (255,0,0) #Цвет красный

def draw_backroundt():
    screen.fill(BackRound)
    pygame.draw.line(screen,RET,(0,400),(SCREEN_WIDTH,400),5)
    pygame.draw.line(screen, RET, (0, 0), (SCREEN_WIDTH, 1000000), 5)
    pygame.draw.line(screen, RET, (0, 1000000), (SCREEN_WIDTH, 0), 5)

#Класс игрока
class Soldier(pygame.sprite.Sprite):
    def __init__(self,carector_tipe,x,y,scale,speed):
        # Загрузка изображения персонажа
        pygame.sprite.Sprite.__init__(self)
        self.jump = False
        self.jump_in_air = True
        self.alive = True
        self.vel_y = 0
        self.carector_tipe = carector_tipe
        self.speed=speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index=0
        self.action = 0
        self.updata_time = pygame.time.get_ticks()
        Animetion_Types = ["Idle","Run","Jump"]
        for animation in Animetion_Types:
            tenp_list = []
            num_off_frames = len(os.listdir(f"img/{self.carector_tipe}/{animation}"))
            for i in range(num_off_frames):
                img = pygame.image.load(f"img/{self.carector_tipe}/{animation}/{i}.png").convert_alpha()
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
        #pygame.draw.rect(screen,RET,(self.rect.x,self.rect.y, self.rect.width,self.rect.height),3)

    #Движение
    def move(self,moving_left,moving_right):
        #Переменные перемещения
        dx=0
        dy=0

        if moving_left:
            dx = - self.speed
            self.direction = -1
            self.flip = True
            if player.rect.left <= 0:
                dx = 0
        if moving_right:
            dx = self.speed
            self.direction = 1
            self.flip = False
            if player.rect.right >= 800:
                dx = 0
        if self.jump == True and self.jump_in_air == False:
            self.vel_y = -11
            self.jump = False
            self.jump_in_air = True

        self.vel_y += Gravitazya
        dy += self.vel_y

        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.jump_in_air = False







        #Обновление позиции игрока
        self.rect.x += dx
        self.rect.y += dy

#Персонаж
player = Soldier("player",200,300,2,3)
Zlodey = Soldier("enemy",300,300,2,3)


run = True
#Функции при запуске игры
while run:
    draw_backroundt()
    player.draw()
    Zlodey.draw()

    #Обновление действий игрока
    if player.alive: #Если игрок жив
        if player.jump_in_air:
            player.updata_actiones(2)
        elif moving_left or moving_right:
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
            if event.key == pygame.K_w and player.alive:
                player.jump = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            #if event.key == pygame.K_w and player.alive:
                #player.jump = False
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
        # KEYUP - отжатие
        # KEYDOWN - нажатие
    #Обновление экрана
    pygame.display.update()
    clock.tick(FPS)