import pygame

# Initialize Pygame
pygame.init()

# Define colors
BLACK = (13, 9, 10)
WHITE = (234, 242, 239)
GRAY = (145, 47, 86)
LIGHT_GRAY = (200, 200, 200)

# Set window dimensions
WIDTH = 800
HEIGHT = 600

# Create the window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Window")
main_display_width = 800
main_display_height = 600
# Define button dimensions
button_width = 150
button_height = 50
button_corner_radius = 10

# Define button positions
button1_pos = (WIDTH // 2 - button_width // 2, HEIGHT - 100)
button2_pos = (WIDTH // 2 - button_width // 2 - 200, HEIGHT - 100)
button3_pos = (WIDTH // 2 - button_width // 2 + 200, HEIGHT - 100)

# Create clock object to control the frame rate
clock = pygame.time.Clock()

# Button state variables
button1_clicked = False
button2_clicked = False
button3_clicked = False

# Display text variables
display_text = "Hello, lets play!"

secondary_display_width = 400
secondary_display_height = 50
secondary_display_pos = (WIDTH // 2 - secondary_display_width // 2, HEIGHT // 2 + 50)
secondary_display_text= "Rock, Paper, Scissors!"

# Run the game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if pygame.Rect(button1_pos, (button_width, button_height)).collidepoint(mouse_pos):
                button1_clicked = True
                display_text = "I chose Paper, I win!"
                secondary_display_text = " Press a button to try again."
            elif pygame.Rect(button2_pos, (button_width, button_height)).collidepoint(mouse_pos):
                button2_clicked = True
                display_text = "I chose Scissors, I win!"
                secondary_display_text = " Press a button to try again."
            elif pygame.Rect(button3_pos, (button_width, button_height)).collidepoint(mouse_pos):
                button3_clicked = True
                display_text = "I chose Rock, I win!"
                secondary_display_text = " Press a button to try again."
        elif event.type == pygame.MOUSEBUTTONUP:
            button1_clicked = False
            button2_clicked = False
            button3_clicked = False

    # Clear the screen
    window.fill(WHITE)

    # Draw buttons
    button1_color = LIGHT_GRAY if button1_clicked else GRAY
    button2_color = LIGHT_GRAY if button2_clicked else GRAY
    button3_color = LIGHT_GRAY if button3_clicked else GRAY

    pygame.draw.rect(window, button1_color, (button1_pos[0], button1_pos[1], button_width, button_height), border_radius=button_corner_radius)
    pygame.draw.rect(window, button2_color, (button2_pos[0], button2_pos[1], button_width, button_height), border_radius=button_corner_radius)
    pygame.draw.rect(window, button3_color, (button3_pos[0], button3_pos[1], button_width, button_height), border_radius=button_corner_radius)

    # Draw button text
    font = pygame.font.Font(None, 36)
    button1_text = font.render("Rock", True, WHITE)
    button2_text = font.render("Paper", True, WHITE)
    button3_text = font.render("Scissors", True, WHITE)
    window.blit(button1_text, (button1_pos[0] + 20, button1_pos[1] + 10))
    window.blit(button2_text, (button2_pos[0] + 20, button2_pos[1] + 10))
    window.blit(button3_text, (button3_pos[0] + 20, button3_pos[1] + 10))

    # Draw display
    display_text_surface = font.render(display_text, True, BLACK)
    display_rect = display_text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    main_display_rect = pygame.Rect(0, 0, main_display_width, main_display_height)
    pygame.draw.rect(window, BLACK, main_display_rect, 2)
    window.blit(display_text_surface, display_rect)
    
    
    
    secondary_display_rect = pygame.Rect(secondary_display_pos, (secondary_display_width, secondary_display_height))
    pygame.draw.rect(window, GRAY, secondary_display_rect)
    pygame.draw.rect(window, BLACK, secondary_display_rect, 2)
    
    font = pygame.font.Font(None, 36)
    text = font.render(secondary_display_text, True, WHITE)
    text_rect = text.get_rect(center=secondary_display_rect.center)
    window.blit(text, text_rect)

    # Update the display
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()