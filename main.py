import pygame
from scene1 import Scene1
from scene2 import Scene2

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("My Adventure Game")
    clock = pygame.time.Clock()

    # Start with Scene1
    scenes = {
        'Scene1': Scene1(screen),
        'Scene2': Scene2(screen)
    }
    current_scene = scenes['Scene1']

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            current_scene.handle_event(event)

        next_scene_name = current_scene.update()
        if next_scene_name:
            if next_scene_name == 'Scene2':
                current_scene = scenes['Scene2']
                current_scene.player_pos[0] = 60  # Start just offscreen to the left
                current_scene.animating_in = True  # Trigger the animation into the frame
            elif next_scene_name == 'Scene1':
                current_scene = scenes['Scene1']
                current_scene.player_pos[0] = 740  # Start just offscreen to the right
                current_scene.animating_in = False  # Trigger the animation into the frame

            current_scene.target_pos[0] = current_scene.player_pos[0]

        screen.fill((0, 0, 0))  # Clear the screen before drawing the new scene
        current_scene.draw()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
