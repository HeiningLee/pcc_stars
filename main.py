import pygame
import sys
import game_functions as gf
from star import Star
from settings import Settings
from pygame.sprite import Sprite
from pygame.sprite import Group




def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    stars = Group()
    gf.create_stars(ai_settings, screen, stars)

    while True:
        gf.check_events()

        gf.update_screen(ai_settings, screen, stars)




run_game()