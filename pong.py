import pygame
import sys
import degrees_to_velocuty

pygame.init()  # инициализация модулей пайгейма

# константы
WHITE = (255, 255, 255)  # белый цвет
BLACK = (0, 0, 0)  # черный цвет

# экран
screen_width = 1000  # ширина экрана в пикселях
screen_height = 650  # высота экрана в пикселях
screen = pygame.display.set_mode((screen_width, screen_height))  # экран

# игрок 1
player_width1 = 13  # ширина игрока
player_height1 = 80  # высота игрока
player_x1 = 100  # игрок в центре по ширине
player_y1 = screen_height // 2 - player_height1 // 2
player1 = pygame.Rect((player_x1, player_y1, player_width1, player_height1))

# игрок 2
player_width2 = 13  # ширина игрока
player_height2 = 80  # высота игрока
player_x2 = screen_width - 100 - player_width2
player_y2 = screen_height // 2 - player_height2 // 2
player2 = pygame.Rect((player_x2, player_y2, player_width2, player_height2))

# мяч
ball_width = 10
ball_height = 10
ball_x = screen_width // 2 - ball_width
ball_y = screen_height // 2 - ball_height
ball = pygame.Rect((ball_x, ball_y, ball_height, ball_width))
ball_direction = degrees_to_velocuty.degrees_to_velocity(45, 1)
ball_speed_x = ball_direction[0]
ball_speed_y = ball_direction[1]
game = True
while game:
    """
        Главный цикл игры
        Цикл должен обязательно закончится обновлением дисплея,
        если выйти по break, то игра зависнет!
        Контролируем, идет ли игра, переменной game
    """

    # события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # обработка события выхода
            game = False
        if event.type == pygame.KEYDOWN:  # нажатая клавиша (не зажатая!)
            if event.key == pygame.K_ESCAPE:  # клавиша Esc
                game = False
    keys = pygame.key.get_pressed()  # собираем коды нажатых клавиш в список
    if keys[pygame.K_UP]:  # клавиша стрелка вверх
        if player2.y >= 0:
            player2.y -= 1  # двигаем игрока вверх (в PG Y растет вниз)
    if keys[pygame.K_DOWN]:  # клавиша стрелка вниз
        if player2.y <= (screen_height - player_height2):
            player2.y += 1  # двигаем игрока вниз
    if keys[pygame.K_w]:  # клавиша стрелка вверх
        if player1.y >= 0:
            player1.y -= 1  # двигаем игрока вверх (в PG Y растет вниз)
    if keys[pygame.K_s]:  # клавиша стрелка вниз
        if player1.y <= (screen_height - player_height2):
            player1.y += 1  # двигаем игрока вниз

    # логика
    ball.x += ball_speed_x
    if ball.x < 0:
        ball_speed_x *= -1
    if ball.x > screen_width - ball_width:
        ball_speed_x *= -1
    ball.y += ball_speed_y
    if ball.y < 0:
        ball_speed_y *= -1
    if ball.y > screen_height - ball_height:
        ball_speed_y *= -1

    # отрисовка
    screen.fill(BLACK)  # заливаем экран чёрным
    pygame.draw.rect(screen, WHITE, ball)
    pygame.draw.rect(screen, WHITE, player1)  # рисуем игрока
    pygame.draw.rect(screen, WHITE, player2)
    pygame.display.flip()  # обновляем экран

# после завершения главного цикла
pygame.quit()  # выгрузили модули pygame из пямяти
sys.exit()  # закрыли программу