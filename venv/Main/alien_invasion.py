import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats



def run_game():
    # Initialize game and create a screen object.
    pygame.init()q

    # Initialize screen settings
    ai_settings= Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    #Create an instance to store game_stat
    stats=GameStats(ai_settings)

    # Make the ship
    ship=Ship(ai_settings,screen)
    # Make group to store bullets in
    bullets=Group()
    # Make an alien
    aliens=Group()
    gf.create_fleet(ai_settings,screen,ship,aliens)


    # Start the main loop for the game
    while True:
        # Check for events
        gf.check_events(ai_settings,screen,ship,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        gf.update_screen(ai_settings,screen,ship,bullets,aliens)

run_game()