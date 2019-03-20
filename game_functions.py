import sys
import pygame
from star import Star
from settings import Settings
from pygame.sprite import Sprite


def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sys.exit()


def update_screen(ai_settings, screen, stars):
    screen.fill(ai_settings.bg_color)
    stars.draw(screen)
    pygame.display.flip()


def create_stars(ai_settings, screen, stars):
    star = Star(ai_settings, screen)
    nstar_x = get_number_x(ai_settings, star)
    nstar_y = get_number_y(ai_settings, star)
    for i in range(nstar_y):
        for j in range(nstar_x):
            star1 = Star(ai_settings, screen)
            star1.rect.x = star1.rect.width + j * 2 * star1.rect.width
            star1.rect.y = star1.rect.height + i * 2 * star1.rect.height
            stars.add(star1)


def get_number_x(ai_settings, star):
    screen_x = ai_settings.screen_width
    star_x = star.rect.width
    usage_x = screen_x - 2 * star_x
    nstar_x = int(usage_x/(star_x*2))
    # print(nstar_x)
    return nstar_x


def get_number_y(ai_settings, star):
    screen_y = ai_settings.screen_height
    star_y = star.rect.height
    usage_y = screen_y - 2 * star_y
    nstar_y = int(usage_y/(star_y*2))
    # print(nstar_y)
    return nstar_y


