import pygame
from scene import Scene
from animation import Animation

class Scene1(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.screen = screen
        self.background = pygame.image.load('assets/images/background.png')

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

        self.player_pos = [50, 500]  # Start near the left side of the screen
        self.target_pos = self.player_pos[:]
        self.speed = 5
        self.walk_y = 500  # Fixed y position for walking

        # Post-transition animation state
        self.animating_in = False

    def handle_event(self, event):
        if not self.animating_in and event.type == pygame.MOUSEBUTTONDOWN:
            self.target_pos = [event.pos[0], self.walk_y]

    def update(self):
        if self.animating_in:
            # Animate the character into the scene by moving them to the right
            if self.player_pos[0] > 50:
                self.player_pos[0] -= 10
                if self.player_pos[0] <= 50:
                    self.animating_in = False  # Stop animating when the character is fully in frame
            return None

        dx = self.target_pos[0] - self.player_pos[0]
        dist = abs(dx)
        if dist > self.speed:
            self.player_pos[0] += (dx / dist) * self.speed
            moving = True
        else:
            moving = False

        self.walk_animation.update(moving)

        # Check if the player has reached the right edge of the screen
        if self.player_pos[0] >= 750:  # Assuming the screen width is 800
            return 'Scene2'
        return None

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.walk_animation.get_current_frame(), self.player_pos)
