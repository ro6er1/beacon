import pygame

class Animation:
    def __init__(self, image_paths, frame_delay):
        self.frames = [pygame.image.load(image_path) for image_path in image_paths]
        self.current_frame = 0
        self.frame_count = 0
        self.frame_delay = frame_delay

    def update(self, moving):
        if moving:
            self.frame_count += 1
            if self.frame_count >= self.frame_delay:
                self.current_frame = (self.current_frame + 1) % len(self.frames)
                self.frame_count = 0
        else:
            self.current_frame = 0  # Reset to the first frame when not moving

    def get_current_frame(self):
        return self.frames[self.current_frame]
