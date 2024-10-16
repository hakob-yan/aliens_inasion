import pygame
class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.transform.scale(pygame.image.load('./images/ship.png'), (64, 64))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.settings=ai_game.settings
        self.x=float(self.rect.x)
        self.y=float(self.rect.y)
        self.moving_right = False
        self.moving_top = False
        self.moving_bottom = False
        self.moving_left = False



    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_top and self.rect.top >0:
                self.y -= self.settings.ship_speed
        if self.moving_bottom  and self.rect.bottom < self.screen_rect.bottom:
                self.y += self.settings.ship_speed
        self.rect.x=self.x
        self.rect.y=self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)