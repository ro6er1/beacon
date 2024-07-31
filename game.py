class Game:
    def __init__(self, screen):
        self.screen = screen
        self.load_assets()
        self.player_pos = [400, 300]
        self.target_pos = self.player_pos[:]
        self.speed = 5
        self.dialogue = Dialogue(screen)

    def load_assets(self):
        self.background = pygame.image.load('assets/images/background.png')
        self.player_image = pygame.image.load('assets/images/player.png')

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.target_pos = list(event.pos)
            self.dialogue.show("You clicked at " + str(event.pos))

    def update(self):
        dx = self.target_pos[0] - self.player_pos[0]
        dy = self.target_pos[1] - self.player_pos[1]
        dist = math.hypot(dx, dy)
        if dist > self.speed:
            self.player_pos[0] += dx / dist * self.speed
            self.player_pos[1] += dy / dist * self.speed

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.player_image, self.player_pos)
        self.dialogue.draw()
