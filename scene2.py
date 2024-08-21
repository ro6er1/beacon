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

        self.player_pos = [750, 500]  # Initially, start off-screen on the right
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
            # Animate the character into the scene by moving them to the left
            if self.player_pos[0] < 50:
                self.player_pos[0] += 10
            else:
                self.animating_in = False  # Stop animating when the character is fully in frame
            return None  # Skip the normal update while animating

        # Regular movement logic
        dx = self.target_pos[0] - self.player_pos[0]
        dist = abs(dx)
        if dist > self.speed:
            self.player_pos[0] += (dx / dist) * self.speed
            moving = True
        else:
            moving = False

        self.walk_animation.update(moving)

        # Check if the player has reached the left edge of the screen
        if self.player_pos[0] <= 50:  # Transition when at 50px or less from the left
            return 'Scene1'

        # Prevent transition on the right edge
        if self.player_pos[0] >= 750:
            self.player_pos[0] = 750  # Stop the player at the right edge

        return None

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.walk_animation.get_current_frame(), self.player_pos)
