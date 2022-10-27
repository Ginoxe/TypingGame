import pygame, sys
pygame.init()

size = width, height = 1500, 800
speed = 2
black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption("Show text")



class letter():
    def __init__(self):
        self.font = pygame.font.SysFont('arial', 30)
        self.text = self.font.render(random.choice(LetterList))
        self.textrect = self.text.get_rect()
        self.x = 0 #랜덤한 값
        self.y = 0
    
    def fall(self):
        self.y += speed
        self.textrect.center = self.x, self.y

font1 = pygame.font.SysFont('arial', 30)
text = font.render('L', True, black)
textrect = text.get_rect()
font2 = pygame.font.SysFont('arial', 45, True)
starttext = font.render('Start Test', True, white)
starttextrect = starttext.get_rect()


rectwidth, rectheight = 300, 100

y = 0
isplaying = False
while 1:
    screen.fill(white)

    width, height = pygame.display.get_surface().get_size()

    if isplaying == False:
        starttextrect.center = width/2, height/2
        pygame.draw.rect(screen, black, [width/2 - rectwidth/2, height/2 - rectheight/2, rectwidth, rectheight])
        screen.blit(starttext, starttextrect)

    if isplaying == True:
        y += 0.1
        textrect.center = 1000, y
        screen.blit(text, textrect)

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 - rectwidth/2 <= mouse[0] <= width/2 + rectwidth/2 and height/2 - rectheight/2 <= mouse[1] <= height/2 + rectheight/2:
                isplaying = True
    pygame.display.update()

# import pygame
# print(pygame.font.get_fonts())