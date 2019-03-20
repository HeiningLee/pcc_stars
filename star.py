import pygame
from pygame.sprite import Sprite


class Star(Sprite):
    def __init__(self, ai_settings, screen):
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load("images/star.bmp")
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height


    def blitme(self):
        self.screen.blit(self.image, self.rect)
