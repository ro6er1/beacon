import pygame
import math

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.load_assets()
        self.player_pos = [400, 500]  # Start at x=400, y=500 (near the bottom)
        self.target_pos = self.player_pos[:]
        self.speed = 5
        self.walk_y = 500  # Fixed y position for walking

    def load_assets(self):
        self.background = pygame.image.load('assets/images/background.png')
        self.player_image = pygame.image.load('assets/images/player.png')

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Only update the target x position; y is fixed
            self.target_pos = [event.pos[0], self.walk_y]

    def update(self):
        dx = self.target_pos[0] - self.player_pos[0]
        dist = abs(dx)
        if dist > self.speed:
            self.player_pos[0] += (dx / dist) * self.speed
        self.player_pos[1] = self.walk_y  # Ensure the y position remains fixed

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player_image, self.player_pos)
