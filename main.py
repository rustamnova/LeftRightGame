import pygame

pygame.init()

# Определяем размеры экрана
screen_width = 640
screen_height = 480

# Создаем окно
screen = pygame.display.set_mode((screen_width, screen_height))

# Определяем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определяем размер и позицию игрового объекта
block_width = 75
block_height = 15
block = pygame.Rect(0, 0, block_width, block_height)
block.centerx = screen.get_rect().centerx
block.bottom = screen.get_rect().bottom - 10

# Устанавливаем начальную скорость перемещения блока
block_speed = 0.5

# Создаем поверхность для эффекта следа
trail_surface = pygame.Surface((block_width, block_height))
trail_surface.set_alpha(128)
trail_surface.fill(BLACK)

# Определяем основной цикл игры
running = True
while running:
    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Получаем состояние клавиш
    keys = pygame.key.get_pressed()

    # Обновляем позицию блока в зависимости от нажатых клавиш
    if keys[pygame.K_LEFT]:
        block.left -= block_speed
    if keys[pygame.K_RIGHT]:
        block.right += block_speed
    if keys[pygame.K_UP]:
        block.top -= block_speed
    if keys[pygame.K_DOWN]:
        block.bottom += block_speed

    # Очищаем экран и отрисовываем игровые объекты
    screen.fill(BLACK)
    screen.blit(trail_surface, block)
    pygame.draw.rect(screen, WHITE, block)

    # Обновляем поверхность для эффекта следа
    trail_surface.fill(BLACK)
    trail_surface.blit(screen, (-block.left, -block.top), block)

    # Обновляем экран
    pygame.display.flip()

# Завершаем работу Pygame
pygame.quit()
