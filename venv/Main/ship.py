import pygame

class Ship():
    def __init__(self,ai_settings,screen):
        """Initialize the ship and set is starting position"""
        self.screen=screen
        self.ai_settings=ai_settings
        self.image=pygame.image.load('C:/Users/saikat/PycharmProjects/AlienInvasion/venv/Images/ship.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #Store Decimal value for the ship center
        self.center=float(self.rect.centerx)

        # Start new ship at the bottom center of the screen
        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        #Movement flag
        self.moving_right=False
        self.moving_left = False
    def update(self):
        """Update the ships position based on the movement flag"""
        if self.moving_right and self.rect.right<self.screen_rect.right:
            self.rect.centerx+=self.ai_settings.ship_speed_factor

        elif self.moving_left and self.rect.left>self.screen_rect.left:
            self.rect.centerx-=self.ai_settings.ship_speed_factor

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        """Venter the ship on screen"""
        self.center=self.screen_rect.centerx


