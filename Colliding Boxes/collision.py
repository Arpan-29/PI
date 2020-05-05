import pygame 

pygame.init()
screenWidth = 600
screenHeight = 600
win = pygame.display.set_mode((screenWidth, screenHeight))

font = pygame.font.SysFont("Times New Roman", 72)

WHITE = (255,255,255)
ORANGE = (255, 100, 0)

class Box() :
    def __init__(self, x, y, w, m, vel) :
        self.x = x
        self.y = y - w
        self.w = w
        self.m = m
        self.vel = vel
        self.color = ORANGE

    def update(self) :
        self.x += self.vel

    def collide(self, other) :
        return self.x + self.w > other.x 

    def bounce(self, other) :
        m1 = self.m
        m2 = other.m
        u1 = self.vel
        u2 = other.vel

        v1 = ((m1 - m2) / (m1 + m2)) * u1 + (2 * m2 / (m1 + m2)) * u2
        return v1 

    def collide_wall(self) :
        return self.x < 0 

    def show(self) :
        pygame.draw.rect(win, self.color, (self.x, self.y, self.w, self.w))
        pygame.draw.rect(win, WHITE, (self.x, self.y, self.w, self.w), 2)

digits = 6
    
collisions = 0
timesteps = 1000
speed = 1

box1 = Box(100, screenHeight - 200, 50, 1, 0)
box2 = Box(200, screenHeight - 200, 100, (100)**(digits - 1), -speed/timesteps)

run = True
play = False
while run :

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed() 
    if keys[pygame.K_SPACE] :
        play = True

    if play :
        win.fill(0)
        pygame.draw.line(win, WHITE, (0, screenHeight - 200), (screenWidth, screenHeight - 200))
        
        for i in range(timesteps) :
            box1.update()
            box2.update()

            if box1.collide(box2) :
                collisions += 1
                
                v1 = box1.bounce(box2)
                v2 = box2.bounce(box1)
                box1.vel = v1
                box2.vel = v2

            if box1.collide_wall() :
                collisions += 1
                box1.vel *= -1

            if box1.x > 50 and box1.vel >= 0 and box2.vel > box1.vel and box2.x > screenWidth:
                run = False

            box1.show()
            box2.show()

        text = font.render(str(collisions), True, WHITE)
        win.blit(text, (50, screenHeight - 150))

        pygame.display.update()

pygame.quit()