import pygame
import levels

def check_exit_collision(player, exit_rect, current_level):
    # If the player collides with the exit and is on Level 1
    player_rect = pygame.Rect(player.x, player.y, player.width, player.height)
    
    if player_rect.colliderect(exit_rect):
        next_level = current_level + 1
        if next_level > levels.TOTAL_LEVELS:
            next_level = 1  # Optionally restart from Level 1
            # Or return a "game over" signal if you want
        platform, rectangles = levels.load_level(next_level)
        player.x, player.y = 350, 510  # Reset position
        return next_level, platform, rectangles, False
    
    return current_level, None, None, None