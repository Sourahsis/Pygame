import pygame
import random
import os
pygame.init()
# Colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
blue = (0, 0, 255)
# Creating window
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Game Title
pygame.display.set_caption("Bank Robbery")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)
def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])
def welcome():
    exit_game = False
    pygame.mixer.music.load('Fluffing-a-Duck.mp3')
    pygame.mixer.music.play()
    while not exit_game:
        gameWindow.fill((255,255,255))
        welscreen1=pygame.image.load("welcome.png")
        welscreen=pygame.transform.scale(welscreen1, (screen_width*0.80, screen_height*0.80))
        gameWindow.blit(welscreen, (50, 50))
        wel1 = pygame.image.load("wel2.png")
        wel2 = pygame.transform.scale(wel1, (screen_width * 0.50, screen_height * 0.20))
        gameWindow.blit(wel2, (200,450))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load('Monkeys-Spinning-Monkeys.mp3')
                    pygame.mixer.music.play()
                    gameloop()
        pygame.display.update()
        clock.tick(60)

# Game Loop
def gameloop():
    # Game specific variables
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    police_x1 = 50
    police_y1 = 400
    police_x2 = 10
    police_y2 = 450
    police_x3 = 720
    police_y3 = 10
    police_x4 = 40
    police_y4 = 30
    police_x5 = 400
    police_y5 = 50
    police_x6 = 90
    police_y6 = 90
    velpolice_1 = 0
    velpolice_2 = 0
    with open("hiscore.txt", "r") as f:
        hiscore = f.read()
    food_x = random.randint(20, screen_width / 2)
    food_y = random.randint(20, screen_height / 2)
    score = 0
    init_velocity = 5
    init_velocity2 = 8
    snake_size = 30
    fps = 60
    policeImage1= pygame.image.load("security-guard.png")
    policeImage=pygame.transform.scale(policeImage1, (50, 50))
    ThiefImage1= pygame.image.load("thief (1).png")
    ThiefImage=pygame.transform.scale(ThiefImage1, (50, 50))
    caughtimg= pygame.image.load("custody.png")
    moneyimage1=pygame.image.load("money-bag.png")
    moneyimage=pygame.transform.scale(moneyimage1, (50, 50))
    bgimg1 = pygame.image.load("screen.png")
    bgimg = pygame.transform.scale(bgimg1, (screen_width, screen_height))
    overscreen1 = pygame.image.load("custody 1.png")
    overscreen = pygame.transform.scale(overscreen1, (screen_width, screen_height))

    while not exit_game:
        if game_over:
            if (not os.path.exists("hiscore.txt")):
                with open("hiscore.txt", "w") as f:
                    f.write("0")
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))

            gameWindow.fill(white)
            gameWindow.blit(overscreen, (0, 0))
            text_screen("Game Over! Press Enter To Continue", white, 100, 250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                        velpolice_1 = + init_velocity2
                        velpolice_2 = - init_velocity2

                    if event.key == pygame.K_LEFT:
                        velocity_x = - init_velocity
                        velpolice_1 = + init_velocity2
                        velpolice_2 = - init_velocity2
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - init_velocity
                        velocity_x = 0
                        velpolice_1 = + init_velocity2
                        velpolice_2 = - init_velocity2

                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0
                        velpolice_1 = + init_velocity2
                        velpolice_2 = - init_velocity2

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            police_x1=police_x1 + velpolice_1
            police_x2=police_x2 + velpolice_2
            police_y3=police_y3 + velpolice_1
            police_y4=police_y4 + velpolice_2
            police_y5=police_y5 + velpolice_2
            police_x6=police_x6 + velpolice_2

            if snake_x>900:
                snake_x-=900
            if snake_x<0:
                snake_x+=900
            if snake_y>600:
                snake_y-=600
            if snake_y<0:
                snake_y+=600

            if police_x1>900:
                police_x1-=900
            if police_x1<0:
                police_x1+=900


            if police_x2 > 900:
                police_x2 -= 900
            if police_x2 < 0:
                police_x2 += 900

            if police_y3>600:
                police_y3-=600
            if police_y3<0:
                police_y3+=600

            if police_y4>600:
                police_y4-=600
            if police_y4<0:
                police_y4+=600

            if police_x6 > 900:
                police_x6 -= 900
            if police_x6 < 0:
                police_x6 += 900

            if police_y5>600:
                police_y5-=600
            if police_y5<0:
                police_y5+=600



            if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                score +=10
                print("Score: ", score)

                food_x = random.randint(20, screen_width / 2)
                food_y = random.randint(20, screen_height / 2)
            if abs(snake_x - police_x1) < 20 and abs(snake_y - police_y1) < 20:
                pygame.mixer.music.load('negative_beeps-6008.mp3')
                pygame.mixer.music.play()
                game_over=True

            if abs(snake_x - police_x2) < 10 and abs(snake_y - police_y2) < 10:
                pygame.mixer.music.load('negative_beeps-6008.mp3')
                pygame.mixer.music.play()
                game_over=True

            if abs(snake_x - police_x3) < 10 and abs(snake_y - police_y3) < 10:
                pygame.mixer.music.load('negative_beeps-6008.mp3')
                pygame.mixer.music.play()
                game_over=True

            if abs(snake_x - police_x4) < 10 and abs(snake_y - police_y4) < 10:
                pygame.mixer.music.load('negative_beeps-6008.mp3')
                pygame.mixer.music.play()
                game_over = True

            if abs(snake_x - police_x5) < 10 and abs(snake_y - police_y5) < 10:
                pygame.mixer.music.load('negative_beeps-6008.mp3')
                pygame.mixer.music.play()
                game_over = True

            if abs(snake_x - police_x6) < 10 and abs(snake_y - police_y6) < 10:
                pygame.mixer.music.load('negative_beeps-6008.mp3')
                pygame.mixer.music.play()
                game_over=True
            if score>int(hiscore):
                hiscore=score

            gameWindow.blit(bgimg, (0, 0))
            text_screen("Score: " + str(score) + "  High score: "+str(hiscore), white, 5, 5)

            gameWindow.blit(policeImage, (police_x1, police_y1))
            gameWindow.blit(policeImage, (police_x2, police_y2))
            gameWindow.blit(policeImage, (police_x3, police_y3))
            gameWindow.blit(policeImage, (police_x4, police_y4))
            gameWindow.blit(policeImage, (police_x5, police_y5))
            gameWindow.blit(policeImage, (police_x6, police_y6))
            gameWindow.blit(ThiefImage, (snake_x, snake_y))
            gameWindow.blit(moneyimage, (food_x, food_y))

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()



