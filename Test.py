import pygame
import sys

def display_game_name(screen, game_name):
    pygame.init()
    font = pygame.font.Font(None, 36)  # You can adjust the font size and style
    text_surface = font.render(game_name, True, (255, 255, 255))  # White color
    text_rect = text_surface.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

# Example usage:
if __name__ == "__main__":
    screen_width, screen_height = 800, 600  # Set your desired screen dimensions
    game_name = "My Awesome Game"  # Change this to your game's name
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption(game_name)
    display_game_name(screen, game_name)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()