import sys
import pygame
from settings import Settings
def run_game():
    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((
        ai_settings.screen_width,ai_settings.screen_height))#屏幕大小
    pygame.display.set_caption("it is game test")
    bg_color=(ai_settings.bg_color)
    while True:
        for event in pygame.event.get():
            if (event.type==pygame.QUIT):
                pygame.quit()
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()
run_game()