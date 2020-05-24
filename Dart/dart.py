import pygame
import random

pygame.init()
font = pygame.font.SysFont("Times New Roman", 50)

screenHeight = 600
screenWidth = 600
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('Approximation of PI')

win.fill(0)
pygame.draw.circle(win, (255,255,255), (screenWidth // 2, screenHeight // 2), screenHeight // 2)
pygame.draw.circle(win, (0,0,0), (screenWidth // 2, screenHeight // 2), screenHeight // 2 - 2)

inside = 0
total = 0

pts = []

avgValue = -1
count = 0
run = True
play = False
while run :

    pygame.time.delay(1)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False   

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] :
        play = True

    if play :
        win.fill(0)

        for _ in range(10000) :
            x = random.randint(0, screenWidth - 1)
            y = random.randint(0, screenHeight - 1)
            pts.append((x,y))

        for pt in pts :
            disFromCenter = ((pt[0] - screenWidth/2)**2 + (pt[1] - screenHeight/2)**2)
            if disFromCenter <= (screenHeight/2)**2 :
                pygame.draw.circle(win, (0,150,0), (pt[0], pt[1]), 2)
                inside += 1
            else :
                pygame.draw.circle(win, (0,0,150), (pt[0], pt[1]), 2)
            total += 1
        
        valueOfPI = 4 * inside / total

        if avgValue == -1 :
            avgValue = valueOfPI
        else :
            avgValue += valueOfPI
        count += 1
        text = font.render(str(avgValue/count), True, (255, 255, 255))
        win.blit(text, (100, screenHeight // 2 - 25))
        if (len(pts) > 100000) :
            pts = pts[ : 100000]

    pygame.display.update()

pygame.quit()   