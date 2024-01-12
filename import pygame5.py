import pygame
import sys
import random

# 初始化Pygame
pygame.init()

# 設定遊戲視窗大小
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kindness Points Game")

# 設定顏色
white = (255, 255, 255)
red = (255, 0, 0)

# 設定好意點的初始位置和大小
point_size = 30
point_x, point_y = random.randint(0, width - point_size), random.randint(0, height - point_size)

# 設定分數
score = 0

# 設定字體和字體大小
font = pygame.font.Font(None, 36)

# 遊戲主迴圈
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 檢測滑鼠點擊事件
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()

            # 檢查是否點擊到好意點
            if point_x < mouse_x < point_x + point_size and point_y < mouse_y < point_y + point_size:
                # 重新設定好意點位置
                point_x, point_y = random.randint(0, width - point_size), random.randint(0, height - point_size)
                score += 1

    # 繪製背景
    screen.fill(white)

    # 繪製好意點
    pygame.draw.rect(screen, red, (point_x, point_y, point_size, point_size))

    # 繪製分數
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # 更新畫面
    pygame.display.flip()

    # 控制遊戲更新速率
    pygame.time.Clock().tick(60)
