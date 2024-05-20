import pygame
import time
'''Display text at a specified position on the screen'''
def showText(screen, font, text, color, position):
	text_render = font.render(text, True, color)
	rect = text_render.get_rect()
	rect.left, rect.top = position
	screen.blit(text_render, rect)
	return rect.right


'''Button'''
def Button(screen, position, text, font, buttoncolor=(120, 120, 120), linecolor=(20, 20, 20), textcolor=(255, 255, 255), bwidth=200, bheight=50):
	left, top = position
	pygame.draw.line(screen, linecolor, (left, top), (left+bwidth, top), 5)
	pygame.draw.line(screen, linecolor, (left, top-2), (left, top+bheight), 5)
	pygame.draw.line(screen, linecolor, (left, top+bheight), (left+bwidth, top+bheight), 5)
	pygame.draw.line(screen, linecolor, (left+bwidth, top+bheight), (left+bwidth, top), 5)
	pygame.draw.rect(screen, buttoncolor, (left, top, bwidth, bheight))
	text_render = font.render(text, 1, textcolor)
	rect = text_render.get_rect()
	rect.centerx, rect.centery = left + bwidth / 2, top + bheight / 2
	return screen.blit(text_render, rect)
def HalfButton(screen, position, text, font, buttoncolor=(120, 120, 120), linecolor=(20, 20, 20), textcolor=(255, 255, 255), bwidth=100, bheight=50):
    left, top = position
    pygame.draw.line(screen, linecolor, (left, top), (left+bwidth, top), 5)
    pygame.draw.line(screen, linecolor, (left, top-2), (left, top+bheight), 5)
    pygame.draw.line(screen, linecolor, (left, top+bheight), (left+bwidth, top+bheight), 5)
    pygame.draw.line(screen, linecolor, (left+bwidth, top+bheight), (left+bwidth, top), 5)
    pygame.draw.rect(screen, buttoncolor, (left, top, bwidth, bheight))
    text_render = font.render(text, 1, textcolor)
    rect = text_render.get_rect()
    rect.centerx, rect.centery = left + bwidth / 2, top + bheight / 2
    return screen.blit(text_render, rect)
class TextBox:
    def __init__(self, screen, position, size, color=(255, 255, 255), text_color=(0, 0, 0)):
        self.screen = screen
        self.position = position
        self.size = size
        self.rect = pygame.Rect(position, size)
        self.color = color
        self.text_color = text_color
        self.text = ''
        self.font = pygame.font.SysFont('Consolas', 20)
        self.focus = False
        self.cursor_visible = True  # New attribute to control the visibility of the cursor
        self.last_switch = time.time()
        self.hidden_text = False
    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        text_surface = self.font.render(self.text, True, self.text_color)
        self.screen.blit(text_surface, (self.rect.x+5, self.rect.y+14))
        if self.focus and self.cursor_visible:
            pygame.draw.line(self.screen, self.text_color, (self.rect.x + 10 + text_surface.get_width(), self.rect.y + 10), (self.rect.x + 10 + text_surface.get_width(), self.rect.y + self.size[1] - 10))
    def update(self, event):
        if self.focus:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                elif event.key == pygame.K_CAPSLOCK: 
                    self.hidden_text = not self.hidden_text
                    
                elif event.unicode.isprintable() and not event.unicode.isspace(): 
                    if len(self.text) < 17:  # Limit to 17 characters
                        self.text += event.unicode
            if time.time() - self.last_switch > 0.3:
                self.cursor_visible = not self.cursor_visible
                self.last_switch = time.time()
            if self.hidden_text:
                self.text = '*' * len(self.text)
    def check_focus(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.focus = True
            else:
                self.focus = False