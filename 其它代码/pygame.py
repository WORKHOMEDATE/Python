import pygame


pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT), DOUBLEBUF | OPENGL)
pygame.display.set_caption("Simple Minecraft-like Game")

# Set up perspective
gluPerspective(45, (WIDTH / HEIGHT), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# Main game loop
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Movement controls
    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        glTranslatef(0.1, 0, 0)
    if keys[K_RIGHT]:
        glTranslatef(-0.1, 0, 0)
    if keys[K_UP]:
        glTranslatef(0, -0.1, 0)
    if keys[K_DOWN]:
        glTranslatef(0, 0.1, 0)

    # Drawing a cube
    glBegin(GL_QUADS)
    glColor3fv(RED)
    glVertex3fv((1, -1, -1))
    glVertex3fv((1, 1, -1))
    glVertex3fv((-1, 1, -1))
    glVertex3fv((-1, -1, -1))

    glVertex3fv((1, -1, 1))
    glVertex3fv((1, 1, 1))
    glVertex3fv((-1, 1, 1))
    glVertex3fv((-1, -1, 1))

    glVertex3fv((1, -1, -1))
    glVertex3fv((1, 1, -1))
    glVertex3fv((1, 1, 1))
    glVertex3fv((1, -1, 1))

    glVertex3fv((-1, -1, -1))
    glVertex3fv((-1, 1, -1))
    glVertex3fv((-1, 1, 1))
    glVertex3fv((-1, -1, 1))

    glVertex3fv((1, 1, -1))
    glVertex3fv((1, 1, 1))
    glVertex3fv((-1, 1, 1))
    glVertex3fv((-1, 1, -1))

    glVertex3fv((1, -1, -1))
    glVertex3fv((1, -1, 1))
    glVertex3fv((-1, -1, 1))
    glVertex3fv((-1, -1, -1))
    glEnd()

    pygame.display.flip()
    clock.tick(FPS)