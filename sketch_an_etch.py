import pygame

pygame.init()

# Constants
SCREENWIDTH, SCREENHEIGHT = 800,600
WHITE = (255,255,255)
GHOSTWHITE = (248, 248, 255)
BLACK = (0, 0, 0)
TIMBERWOLF = (219, 215, 210)    
FE_RED = (206, 32, 41)
GOLDEN_POPPY = (252, 194, 0)
VEL = 2     # how quickly the stylus moves
FPS = 60


def draw_board(screen):
    # Background // the outside edges
    pygame.font.init()
    screen.fill(FE_RED)

    # Title
    font = pygame.font.SysFont('kunstlerscript', 55)
    text = font.render('Sketch - An - Etch', True, GOLDEN_POPPY)
    textRect = text.get_rect()
    textRect.center = (SCREENWIDTH // 2, 30)
    screen.blit(text, textRect)

    # Directions for movement and clearing
    #font1 = pygame.font.SysFont()

    # Actual drawing area
    pygame.draw.rect(screen, TIMBERWOLF, (75, 60, 650, 440), border_radius=10)
    pygame.draw.rect(screen, BLACK, (75, 60, 650, 440), border_radius=10, width = 2)

    # Left dial
    pygame.draw.circle(screen, WHITE, (50,550), 40)
    pygame.draw.circle(screen, GHOSTWHITE, (50,550), 40, width = 10)
    font1 = pygame.font.SysFont('vladimirscript', 20)
    text1 = font1.render('A or D', True, GOLDEN_POPPY)
    textRect1 = text1.get_rect()
    textRect1.center = (50,550)
    screen.blit(text1, textRect1)

    # Right dial
    pygame.draw.circle(screen, WHITE, (750,550), 40)
    pygame.draw.circle(screen, GHOSTWHITE , (750,550), 40, width = 10)
    font2 = pygame.font.SysFont('vladimirscript', 20)
    text2 = font2.render('W or S', True, GOLDEN_POPPY)
    textRect2 = text2.get_rect()
    textRect2.center = (750,550)
    screen.blit(text2, textRect2)

    # Shake Directions
    font3 = pygame.font.SysFont('vladimirscript', 25)
    text3 = font3.render('Spacebar to shake', True, GOLDEN_POPPY)
    textRect3 = text3.get_rect()
    textRect3.center = (SCREENWIDTH // 2, 550)
    screen.blit(text3, textRect3)

    # Speed Up Directions
    font4 = pygame.font.SysFont('vladimirscript', 25)
    text4 = font4.render('arrow keys to speed up', True, GOLDEN_POPPY)
    textRect4 = text4.get_rect()
    textRect4.center = (SCREENWIDTH // 2, 570)
    screen.blit(text4, textRect4)    

def move_stylus(keys_pressed, stylus, screen):
    # Simulate the idea of turning the knob faster
    if keys_pressed[pygame.K_LEFT] or keys_pressed[pygame.K_RIGHT]:
        VEL_X = VEL + 1
    else:
        VEL_X = VEL
    if keys_pressed[pygame.K_UP] or keys_pressed[pygame.K_DOWN]:
        VEL_Y = VEL + 1
    else:
        VEL_Y = VEL
    
    # Moving the stylus
    if keys_pressed[pygame.K_a] and stylus.x - VEL_X > 76: # moving left
        stylus.x -= VEL_X
        pygame.draw.line(screen, BLACK, [stylus.x + VEL_X, stylus.y], [stylus.x, stylus.y], 2)
    if keys_pressed[pygame.K_d] and stylus.x + VEL_X + stylus.width < 724:    #right
        stylus.x += VEL_X
        pygame.draw.line(screen, BLACK, [stylus.x - VEL_X, stylus.y], [stylus.x, stylus.y], 2)
    if keys_pressed[pygame.K_w] and stylus.y - VEL_Y > 60:     #up
        stylus.y -= VEL_Y
        pygame.draw.line(screen, BLACK, [stylus.x, stylus.y + VEL_Y], [stylus.x, stylus.y], 2) 
    if keys_pressed[pygame.K_s] and stylus.y + VEL_Y + stylus.height < 499:  #down
        stylus.y += VEL_Y
        pygame.draw.line(screen, BLACK, [stylus.x, stylus.y - VEL_Y], [stylus.x, stylus.y], 2)
    

def shake_board(screen, keys_pressed):
    if keys_pressed[pygame.K_SPACE]:
        draw_board(screen)


def main():
    SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
    pygame.display.set_caption("Sketch-An-Etch")

    stylus = pygame.Rect(400, 300, 2, 2)

    game_on = True
    clock = pygame.time.Clock()

    draw_board(SCREEN)

    while game_on: 
        clock.tick(FPS)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_on = False

        keys_pressed = pygame.key.get_pressed()

        pygame.draw.rect(SCREEN, BLACK, stylus)     # draws the stylus

        move_stylus(keys_pressed, stylus, SCREEN)

        shake_board(SCREEN, keys_pressed)

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()