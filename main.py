import pygame
from settings import *
import math
from Level import Level
import msvcrt

#pygame tööle
pygame.init()

#font tööle
pygame.font.init()

#fondi väärtused
myfont = pygame.font.SysFont('Comic Sans MS', 30)



#kui settingutest on fullscreen 1 siis avab akna FULLSCREEN mode peal
if FULLSCREEN == 1:
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    disp_h = 1080
    disp_w = 1920
else:
    screen = pygame.display.set_mode((disp_w, disp_h))

#akna nimi
pygame.display.set_caption("MUTENESS")
#karakteri pilt
playerImage = pygame.image.load("ball.png")
#muudame karakteri suurust
playerImage = pygame.transform.scale(playerImage, (playerSize, playerSize))

#karakter startpositsioonis
screen.blit(playerImage, startPos)

#suunaväärtused
moveRight = 0
moveLeft = 0
moveUp = 0
moveDown = 0

PI = math.pi

#võtame mapi
level = Level("Level1.png")
pilt = level.open_pic() #default size (1440, 1080)

#leveli argumendid
mode = pilt.mode
size = pilt.size
data = pilt.tobytes()

#leveli koordinaadid
x = size[0] + BORDER
y = size[1]

#level image väärtusena, et blittida ekraanile
background1 = pygame.image.fromstring(data, size, mode)



#võtame mapi
level = Level("Level1.png")
pilt = level.open_pic() #default size (1440, 1080)

#leveli argumendid
mode = pilt.mode
size = pilt.size
data = pilt.tobytes()

#level image väärtusena, et blittida ekraanile
background2 = pygame.image.fromstring(data, size, mode)


#võtame mapi
level = Level("Level1.png")
pilt = level.open_pic() #default size (1440, 1080)

#leveli argumendid
mode = pilt.mode
size = pilt.size
data = pilt.tobytes()

#level image väärtusena, et blittida ekraanile
background3 = pygame.image.fromstring(data, size, mode)


backgrounds = []
for _ in levelid:
    # võtame mapi
    level = Level("Level1.png")
    pilt = level.open_pic()  # default size (1440, 1080)

    # leveli argumendid
    mode = pilt.mode
    size = pilt.size
    data = pilt.tobytes()

    # level image väärtusena, et blittida ekraanile
    background = pygame.image.fromstring(data, size, mode)
    backgrounds.append(background)

#Aja muutujad
clock = pygame.time.Clock()
font = pygame.font.Font(None, 54)
font_color = pygame.Color('red')

ajad = []
for i in range(len(backgrounds)):
    vahe = []
    for j in range(5):
        vahe.append(999999)
    ajad.append(vahe)

passed_time = 0
timer_started = False

#kiirenduste suunad
acceleratingRight = 0
acceleratingLeft = 0
acceleratingDown = 0
acceleratingUp = 0

bg_index = 0
current_bg = backgrounds[bg_index]



game_over = False

#põhitsükkel
running = True
while running:

    if game_over:
        for event in pygame.event.get():
            if event.key == pygame.K_SPACE:
                game_over = False
            if event.type == pygame.QUIT:
                running = False

    else:
        #taustavärv
        screen.fill(bgColor)

        #lisame leveli
        screen.blit(current_bg, (int(BORDER / 2), 0))
        screen.blit(font.render("Väljumiseks vajuta ESC", True, font_color),
                    (10, disp_h-100))
        screen.blit(font.render(levelid[bg_index], True, font_color),
                    (10, disp_h - 200))

        #event handler
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            #kui nupuvajutus siis vastav muutus
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_z:
                    moveRight = 1
                if event.key == pygame.K_x:
                    moveLeft = -1
                if event.key == pygame.K_c:
                    moveDown = 1
                if event.key == pygame.K_v:
                    moveUp = -1
                if event.key == pygame.K_ESCAPE:
                    running = False
            #kui nupp lastakse lahti siis vastavad muutused
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_z:
                    moveRight = 0
                if event.key == pygame.K_x:
                    moveLeft = 0
                if event.key == pygame.K_c:
                    moveDown = 0
                if event.key == pygame.K_v:
                    moveUp = 0

        #kontrollib kas karakteri suund on diagonaal
        checkDiagonal = max(1, abs(moveRight + moveLeft) + abs(moveDown + moveUp))

        #kiirendushandler
        if moveRight == 1:
            acceleratingRight = min(maxSpeed, acceleratingRight + acceleration)
        else:
            acceleratingRight = max(0, acceleratingRight - acceleration)

        if moveLeft == -1:
            acceleratingLeft = max(-maxSpeed, acceleratingLeft - acceleration)
        else:
            acceleratingLeft = min(0, acceleratingLeft + acceleration)

        if moveDown == 1:
            acceleratingDown = min(maxSpeed, acceleratingDown + acceleration)
        else:
            acceleratingDown = max(0, acceleratingDown - acceleration)

        if moveUp == -1:
            acceleratingUp = max(-maxSpeed, acceleratingUp - acceleration)
        else:
            acceleratingUp = min(0, acceleratingUp + acceleration)

        #karakteri positsioon X ja Y, kiiruse jaoks
        positionX += (acceleratingRight + acceleratingLeft) / math.sqrt(checkDiagonal) * SPEED
        positionY += (acceleratingDown + acceleratingUp) / math.sqrt(checkDiagonal) * SPEED

        #näitame karaktrit aknas
        screen.blit(playerImage, ((int(positionX), int(positionY))))
        #näitame piksi värvi karakteri  asukohas, tema vasak ülemine nurk
        #screen.blit(myfont.render(str(level.get_pixel_value(pilt, (positionX-BORDER/2, positionY))), False, (0, 0, 0)), (10, 10))

        #palli jaoks piiride loomine
        for i in range(1,playerSize+1):
            x = int(playerSize/2*math.sin(math.degrees(360/i))+positionX+playerSize/2)
            y = int(playerSize/2*math.cos(math.degrees(360/i))+positionY+playerSize/2)

            #kontrollimine, kas karkateri piir asub musta piksli peal
            if level.get_pixel_value(pilt, (x-BORDER/2,y)) == (0, 0, 0):
                if restart == True:
                    positionX, positionY = int(BORDER / 2) + 10, 0 + 10
                else:
                    running = False
            elif level.get_pixel_value(pilt, (x-BORDER/2,y)) == (0, 255, 0):
                timer_started = True
                if timer_started:
                    start_time = pygame.time.get_ticks()

            elif level.get_pixel_value(pilt, (x - BORDER / 2, y)) == (255, 0, 0):
                timer_started = False
                ajad[bg_index].append(passed_time / 1000)
                if restart == True:
                    if bg_index == len(backgrounds)-1:
                        game_over = True
                    else:
                        bg_index += 1
                        current_bg = backgrounds[bg_index]

                    acceleratingRight = 0
                    acceleratingLeft = 0
                    acceleratingDown = 0
                    acceleratingUp = 0
                    positionX, positionY = int(BORDER / 2) + 10, 0 + 10
                else:
                    running = False

        if game_over:
            screen.blit(font.render("Mäng läbi!", True, font_color),
                        (size[0]/2, 650))
            screen.blit(font.render("Uuesti mängimiseks vajuta tühikut!", True, font_color),
                        (size[0]/2, 850))
            acceleratingRight = 0
            acceleratingLeft = 0
            acceleratingDown = 0
            acceleratingUp = 0
            moveRight = 0
            moveLeft = 0
            moveUp = 0
            moveDown = 0
            positionX, positionY = int(BORDER / 2) + 10, 0 + 10
            bg_index = 0
        else:
            if timer_started:
                passed_time = pygame.time.get_ticks() - start_time

            #uuendame akent
            #Aja kuvamine
            text = font.render("Current time:", True, font_color)
            text_best = font.render("Best times:", True, font_color)
            text_sec = font.render(str(passed_time / 1000), True, font_color)

            screen.blit(text, (size[0] + int(BORDER / 2), 0))
            screen.blit(text_sec, (size[0] + int(BORDER / 2) + 100, 50))
            screen.blit(text_best, (size[0] + int(BORDER / 2), 100))

            # Parimad ajad
            screen.blit(font.render("1. ", True, font_color), (size[0] + int(BORDER / 2), 150))
            screen.blit(font.render("2. ", True, font_color), (size[0] + int(BORDER / 2), 200))
            screen.blit(font.render("3. ", True, font_color), (size[0] + int(BORDER / 2), 250))
            screen.blit(font.render("4. ", True, font_color), (size[0] + int(BORDER / 2), 300))
            screen.blit(font.render("5. ", True, font_color), (size[0] + int(BORDER / 2), 350))

            screen.blit(font.render(str(sorted(ajad[bg_index])[0]), True, font_color), (size[0] + int(BORDER / 2) + 100, 150))
            screen.blit(font.render(str(sorted(ajad[bg_index])[1]), True, font_color), (size[0] + int(BORDER / 2) + 100, 200))
            screen.blit(font.render(str(sorted(ajad[bg_index])[2]), True, font_color), (size[0] + int(BORDER / 2) + 100, 250))
            screen.blit(font.render(str(sorted(ajad[bg_index])[3]), True, font_color), (size[0] + int(BORDER / 2) + 100, 300))
            screen.blit(font.render(str(sorted(ajad[bg_index])[4]), True, font_color), (size[0] + int(BORDER / 2) + 100, 350))

    pygame.display.update()
    clock.tick(60)