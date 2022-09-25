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
TILE_SIZE = 100

zvuksmerty = []

#Действия игрока
moving_left = False
moving_right = False
shoot = False
grenate = False
grenate_throw =False

#загрузка картинки
#ПУЛЯ
Pula_img = pygame.image.load("img/icons/bullet.png")
#Граната
Granete_igm = pygame.image.load("img/icons/grenade.png")

BackRound = (32,74,209) #Заливка фона

RET = (255,0,0) #Цвет красный

Fon1 = pygame.mixer.Sound("sounds/Fon1.mp3")
#Fon1.play()
death1 = pygame.mixer.Sound("sounds/Dead.mp3")

def draw_backroundt():
    screen.fill(BackRound)
    pygame.draw.line(screen,RET,(0,400),(SCREEN_WIDTH,400),5)
    pygame.draw.line(screen, RET, (0, 0), (SCREEN_WIDTH, 1000000), 5)
    pygame.draw.line(screen, RET, (0, 1000000), (SCREEN_WIDTH, 0), 5)

#Класс игрока
class Soldier(pygame.sprite.Sprite):
    def __init__(self,carector_tipe,x,y,scale,speed, ammo, grenades):
        # Загрузка изображения персонажа
        pygame.sprite.Sprite.__init__(self)
        self.jump = False
        self.jump_in_air = True
        self.alive = True
        self.vel_y = 0
        self.carector_tipe = carector_tipe
        self.speed=speed
        self.ammo = ammo
        self.star_ammo = ammo
        self.grenades = grenades
        self.health = 100
        self.max_health = self.health
        self.shoot_cooldown = 0
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index=0
        self.action = 0
        self.updata_time = pygame.time.get_ticks()
        Animetion_Types = ["Idle","Run","Jump","Death"]
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
                if self.action == 3:
                    self.frame_index=len(self.animation_list[self.action]) -1
                else:
                    self.frame_index = 0

    def updata_actiones(self,new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.updata_time = pygame.time.get_ticks()






    def draw(self):
        screen.blit(pygame.transform.flip(self.image,self.flip,False),self.rect)
        #pygame.draw.rect(screen,RET,(self.rect.x,self.rect.y, self.rect.width,self.rect.height),3)

    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo > 0:
            self.shoot_cooldown = 20
            bullet = puli(self.rect.centerx + (self.rect.width * 0.6 * self.direction), self.rect.centery,self.direction)
            Pulia_group.add(bullet)
            self.ammo -=1



    def update(self):
        self.updata_animations()
        self.check_alive()

        #Обновление задержки
        if self.shoot_cooldown >0:
            self.shoot_cooldown -=1


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
        #Проверка столкновения с полом
        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.jump_in_air = False

        #Обновление позиции игрока
        self.rect.x += dx
        self.rect.y += dy

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive =False
            self.speed = 0
            self.shoot = 0
            self.updata_actiones(3)
            death1.play(4)


#Класс пули
class puli(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 5
        self.image = Pula_img
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction

    def update(self):
        #Движение пуль
        self.rect.x += self.speed * self.direction
        #ЕПроверить зашла ли пуля за экран
        if self.rect.x < 0 or self.rect.x > 800:
            self.kill()

        #Проверить столкновение с персонажами
        if pygame.sprite.spritecollide(player, Pulia_group, False):
            if player.alive:
                player.health -= 5
                self.kill()

        for Zlodey in Zlodeyskaya_Grupa:
            if pygame.sprite.spritecollide(Zlodey, Pulia_group, False):
                if Zlodey.alive:
                    Zlodey.health -= 5
                    print(Zlodey.health)
                    self.kill()


class Grenade(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.vel_y = -11
        self.speed = 7
        self.image = Granete_igm
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.direction = direction
    def update(self):
        self.vel_y += Gravitazya

        dx = self.speed * self.direction
        dy = self.vel_y

        if self.rect.bottom + dy > 400:
            dy = 400 - self.rect.bottom
            self.jump_in_air = False
            self.speed = 0
        #Проверка столкновения со стеной
        if self.rect.x + dx <= 0:
            self.direction *= -1
        elif self.rect.x + dx >= 800:
            self.direction *= -1

        if self.rect.y + dy >= 600:
            self.direction *= -1
        elif self.rect.y + dy <= 0:
            self.direction *= -1

        self.rect.x += dx
        self.rect.y += dy

        self.timer -= 1
        if self.timer == 0:
            self.kill()
            explosion = Explosion(self.rect.x,self.rect.y, 5)
            explosion_group.add(explosion)
            #Нанести урон, если кто-либо в области поражения
            if abs(self.rect.centerx - player.rect.centerx) < TILE_SIZE*2 and abs(self.rect.centery - player.rect.centery) < TILE_SIZE*2:
                player.health -= 50
            for Zlodey in Zlodeyskaya_Grupa:
                if abs(self.rect.centerx - Zlodey.rect.centerx) < TILE_SIZE * 2 and abs(self.rect.centery - Zlodey.rect.centery) < TILE_SIZE * 2:
                    Zlodey.health -= 50


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        pygame.sprite.Sprite.__init__(self)
        self.timer = 100
        self.image = Granete_igm
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.images = []
        for num in range(1,6):
            img = pygame.image.load(f'img/explsn/exp{num}.png').convert_alpha()
            ing = pygame.transform.scale(img, (img.get_width()*scale, img.get_height()*scale))
            self.images.append(img)
        self.frame_index = 0
        self.image = self.images[self.frame_index]
        self.rect.center = (x,y)
        self.counter = 0

    def update(self):
        EXPLOSION_SPEED = 4


        self.counter += 1
        if self.counter >= EXPLOSION_SPEED:
            self.counter = 0
            self.frame_index += 1

        if self.frame_index >= len(self.images):
            self.kill()
        else:
            self.image = self.images[self.frame_index]




 #Создание групп спрайтов
Zlodeyskaya_Grupa = pygame.sprite.Group()
Pulia_group = pygame.sprite.Group()
Grenade_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

#Персонаж
player = Soldier("player",200,300,2,3,60,50000)
Zlodey = Soldier("enemy",300,365,2,3,120,3)
Zlodeyskaya_Grupa.add(Zlodey)
Zlodey = Soldier("enemy",700,365,2,3,120,3)
Zlodeyskaya_Grupa.add(Zlodey)
Zlodey = Soldier("enemy",530,365,2,3,120,300)
Zlodeyskaya_Grupa.add(Zlodey)

run = True
#Функции при запуске игры
while run:
    draw_backroundt()
    player.draw()
    for Zlodey in Zlodeyskaya_Grupa:
        Zlodey.draw()
        Zlodey.update()

    #Обновление и отрисовка групп
    Pulia_group.update()
    Grenade_group.update()
    explosion_group.update()
    Pulia_group.draw(screen)
    Grenade_group.draw(screen)
    explosion_group.draw(screen)

    #Обновление действий игрока
    if player.alive: #Если игрок жив
        #Выстрелы
        if shoot:
            player.shoot()
        elif grenate and grenate_throw == False and player.grenades > 0:
            grenate = Grenade(player.rect.centerx + (0.5 * player.rect.size[0] * player.direction),\
                              player.rect.top, player.direction)
            Grenade_group.add(grenate)
            player.grenades -= 1

            grenate_throw = True
        if player.jump_in_air:
            player.updata_actiones(2)
        elif moving_left or moving_right:
            player.updata_actiones(1)
        else:
            player.updata_actiones(0)

    player.move(moving_left, moving_right)
    player.update()
    Zlodey.update()



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
            if event.key == pygame.K_SPACE:
                shoot = True
            if event.key == pygame.K_r:
                player.alive = True
            if event.key == pygame.K_m:
                player.alive = True
            if event.key == pygame.K_2:
                grenate = True
            if event.key == pygame.K_9:
                Pulia_group + 0
            if event.key == pygame.K_w and player.alive:
                player.jump = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_SPACE:
                shoot = False
            #if event.key == pygame.K_w and player.alive:
                #player.jump = False
            if event.key == pygame.K_r:
                player.alive = False
                player.speed = 0
                player.updata_actiones(3)
            if event.key == pygame.K_2:
                grenate = False
                grenate_throw = False
            if event.key == pygame.K_m:
                player.alive = True
                player.health += 100
                player.speed = 3
        # KEYUP - отжатие
        # KEYDOWN - нажатие
    #Обновление экрана
    pygame.display.update()
    clock.tick(FPS)