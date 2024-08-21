import pygame
from scene import Scene
from animation import Animation

class Scene2(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.background = pygame.image.load('assets/images/background_scene2.jpeg')

        # Initialize the walking animation
        self.walk_animation = Animation(
            [
                'assets/images/walk1.png',
                'assets/images/walk2.png',
                'assets/images/walk3.png',
                'assets/images/walk4.png'
            ],
            frame_delay=5  # Adjust the delay to control animation speed
        )

        self.player_pos = [50, 500]  # Start at the far left side of the screen
        self.target_pos = self.player_pos[:]
        self.speed = 5
        self.walk_y = 500  # Fixed y position for walking

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.target_pos = [event.pos[0], self.walk_y]

    def update(self):
        dx = self.target_pos[0] - self.player_pos[0]
        dist = abs(dx)
        if dist > self.speed:
            self.player_pos[0] += (dx / dist) * self.speed
            moving = True
        else:
            moving = False

        self.walk_animation.update(moving)

        # Check if the player has reached the left edge of the screen
        if self.player_pos[0] <= 50:  # Assuming 0 is the left edge
            return 'Scene1'

        # Prevent transition on the right edge
        if self.player_pos[0] >= 750:
            self.player_pos[0] = 750  # Stop the player at the right edge

        return None

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.walk_animation.get_current_frame(), self.player_pos)
