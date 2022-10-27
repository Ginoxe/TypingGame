import pygame, sys, random, json
pygame.init()

size = width, height = 1500, 800
speed = 2
black = 0, 0, 0
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

pygame.display.set_caption("Typing Test")

LetterList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


class letter():
    def __init__(self):
        width, height = pygame.display.get_surface().get_size()
        self.font = pygame.font.SysFont('arial', 30)
        self.letter = random.choice(LetterList)
        self.text = self.font.render(self.letter, True, black)
        self.textrect = self.text.get_rect()
        self.x = random.randint(5, width - 20) #랜덤한 값
        self.y = 40
    
    def fall(self, speed):
        self.y += speed
        self.textrect.topleft = self.x, self.y
        screen.blit(self.text, self.textrect)

def GameEnd():
    global hiscore, score, isplaying, letters
    letters = [letter() for i in range(10)]
    isplaying = False
    if hiscore < score:
        hiscore = score
        storage = load_storage()
        storage["highscore"] = hiscore
        dump_storage(storage)
    

def GameStart():
    global score, level, lives, isplaying
    score = 0
    level = 1
    lives = 3
    isplaying = True

def load_storage():
    with open('highscore.json') as data:
        return json.load(data)

def dump_storage(storage):
    with open('highscore.json', 'w') as data:
        json.dump(storage, data)
        return None

storage = load_storage()

letters = [letter() for i in range(10)]

rectwidth, rectheight = 300, 100
lives = 3
level = 1
score = 0
hiscore = storage['highscore']
y = 0
isplaying = False

mainfont = pygame.font.SysFont('arial', 45, True)
gamefont = pygame.font.SysFont('arial', 25)
starttext = mainfont.render('START TEST', True, white)
starttextrect = starttext.get_rect()
scoretext = mainfont.render(f'SCORE: {score}', True, black)
scoretextrect = scoretext.get_rect()
hiscoretext = mainfont.render(f'HIGH SCORE: {hiscore}', True, black)
hiscoretextrect = hiscoretext.get_rect()
gamescoretext = gamefont.render(f'SCORE: {score}', True, black)
gamescoretextrect= gamescoretext.get_rect()
livestext = gamefont.render(f'LIVES: {lives}', True, black)
livestextrect = livestext.get_rect()

while 1:
    screen.fill(white)

    width, height = pygame.display.get_surface().get_size()
    speed = level/10
    letterslist = []
    for i in range(level):
        letterslist.append(letters[i].letter)

    if isplaying == False:
        starttextrect.center = width/2, height/2
        pygame.draw.rect(screen, black, [width/2 - rectwidth/2, height/2 - rectheight/2, rectwidth, rectheight])

        scoretext = mainfont.render(f'SCORE: {score}', True, black)
        scoretextrect.center = width/2, height/2 + 100

        hiscoretext = mainfont.render(f'HIGH SCORE: {hiscore}', True, black)
        hiscoretextrect.center = width/2, height/2 + 150

        screen.blit(starttext, starttextrect)
        screen.blit(scoretext, scoretextrect)
        screen.blit(hiscoretext, hiscoretextrect)

    if isplaying == True:
        for i in range(level):
            letters[i].fall(speed)
            if letters[i].y > height:
                letters[i] = letter()
                lives -= 1
                if lives == 0:
                    GameEnd()

        livestextrect.topright = width - 15, 15
        livestext = gamefont.render(f'LIVES: {lives}', True, black)

        gamescoretext = gamefont.render(f'SCORE: {score}', True, black)
        gamescoretextrect.topleft = 15, 15

        screen.blit(livestext, livestextrect)
        screen.blit(gamescoretext, gamescoretextrect)

        if score == 10:
            level = 2
        elif score == 30:
            level = 3
        elif score == 60:
            level = 4
        elif score == 100:
            level = 5
        elif score == 150:
            level = 6

    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        #.f Start Game
        if event.type == pygame.MOUSEBUTTONDOWN and isplaying == False:
            if width/2 - rectwidth/2 <= mouse[0] <= width/2 + rectwidth/2 and height/2 - rectheight/2 <= mouse[1] <= height/2 + rectheight/2:
                GameStart()

        if event.type == pygame.KEYDOWN:
            #Escape -> Go to Start Page
            if event.key == pygame.K_ESCAPE:
                GameEnd()

            #Type to kill letter
            else:
                if isplaying == True:
                    if letterslist.count(chr(event.key)) > 1:
                        highestY = 40
                        for i in range(level):
                            if letters[i].letter == chr(event.key):
                                if highestY < letters[i].y:
                                    highestY = letters[i].y
                    for i in range(level):
                        try:
                            if chr(event.key) not in letterslist:
                                lives -= 1
                                if lives == 0:
                                    GameEnd()
                                break
                            elif chr(event.key) == letters[i].letter:
                                if letterslist.count(chr(event.key)) > 1:
                                    if letters[i].y == highestY:
                                        letters[i] = letter()
                                        score += 1
                                else:
                                    letters[i] = letter()
                                    score += 1
                        except:
                            pass
                

    pygame.display.update()

# import pygame
# print(pygame.font.get_fonts())