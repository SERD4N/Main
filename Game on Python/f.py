import pygame
 
pygame.init()
#Создание окна
width_window = 850
height_window = 700
screen = pygame.display.set_mode((width_window, height_window))

#Контроль FPS
clock = pygame.time.Clock()
FPS = 50
#Игровые переменные
pygame.mixer.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play()

speed = 10
bg = pygame.image.load('bg.jpg')

x_player = 0
y_player = 570

x_enemy = 0
y_enemy = 0

x_arrow = 1000
y_arrow = 1000

h_player = 130
w_player = 122

h_enemy = 130
w_enemy = 122

h_arrow = 115
w_arrow = 30

running = True
right = True
left = True
shot = False

icon = pygame.image.load('icon.jpg')
pygame.display.set_icon(icon)

player = pygame.image.load('Green_elf_2.png')
enemy = pygame.image.load('enemy.png')
arrow = pygame.image.load('arrow.png')

my_font = pygame.font.SysFont(None, 35)
my_font2 = pygame.font.SysFont(None, 20)
text2 = my_font2.render ('Для управления персонажем используйте клавиши A и D', True, [255, 255, 255])
text3 = my_font2.render ('Для стрельбы используйте левую кнопку мыши', True, [255, 255, 255])
text4 = my_font2.render ('Ваша цель просто попадать по кругу (игра длится бесконечно)', True, [255, 255, 255])

count = 0

pygame.display.set_caption('Ball and Arrow game')
#Игровой цикл


while running: 
    clock.tick(FPS)  
    #Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
               if not x_player <= 0:
                   x_player -= speed
           if event.key == pygame.K_d:
                if not x_player >= width_window - w_player:
                    x_player += speed
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if shot == False:
                    shot = True
                    x_arrow = x_player
                    y_arrow = y_player - 122
                    
        if shot:
            y_arrow -= speed
            if y_arrow < 0:
                shot = False
                x_arrow = 1000
                y_arrow = 1000
        
        if (y_enemy >= y_arrow - h_enemy) and (x_arrow - w_enemy <= x_enemy <= x_arrow + w_arrow):
            count += 1
            shot = False
            x_arrow = 1000
            y_arrow = 1000
        
        
        if right:
            x_enemy += 10
            if x_enemy > 728:
               x_enemy -= 1
               right = False
        else:
            x_enemy -= 5
            if x_enemy < 0:
                x_enemy += 1
                right = True
                
    #Отрисовка событий
    screen.blit(bg, (0,0))
    screen.blit(arrow, (x_arrow, y_arrow))
    screen.blit(enemy, (x_enemy, y_enemy))
    screen.blit(player, (x_player, y_player))
    screen.blit (text2, (400, 210))
    screen.blit (text3, (400, 230))
    screen.blit (text4, (400, 250))
    text1 = my_font.render ('Твой счет: '+str(count), True, [255, 255, 255])
    screen.blit (text1, (0, 150))

    pygame.display.flip()    

pygame.quit()
