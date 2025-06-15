import pygame

class Button:
    def __init__(self, pos, text_input, font, base_color, hovering_color):
        self.image = pygame.Surface((200, 50)).convert_alpha()
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect(topleft=pos)
        self.font = font
        self.base_color = base_color
        self.hovering_color = hovering_color
        self.text_input = text_input
        self.active = False

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        text_surface = self.font.render(self.text_input, True, self.base_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)
    
    def check_for_input(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.active = True
            return True
        else:
            self.active = False
            return False

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.image.fill(self.hovering_color)
        else:
            self.image.fill(self.base_color)