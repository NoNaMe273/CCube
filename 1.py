import pygame
import random
import shutil
from time import gmtime, strftime
import sys
import os

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (90,237,255)
blue = (0, 0, 255)

dis_width = 800
dis_height = 600

lang=1
# 1-eng
# 0-ru
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Crazy Cube')

scr=False

clock = pygame.time.Clock()
class Game_Two():
    global lang
    speed = 10
    healts = 6
    snake_block = 10
    pop = 20
    snake_speed = 30

    def Your_score(self, time):
        font_style = pygame.font.Font('Inkfree.otf', 20)
        if lang == 1:
            value = font_style.render("You live: "+str(time)+" sec", True, (47, 54, 64))
        elif lang == 0:
            value = font_style.render("Вы живете: " + str(time) + " сек", True, (47, 54, 64))
        dis.blit(value, [0, 0])
    def message(self, msg, color):
        font_style = pygame.font.Font('Inkfree.otf', 50)
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [150, dis_height / 3])
        if lang == 1:
            mesg = font_style.render("q - quit", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 50])
            mesg = font_style.render("r - restart", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 100])
            mesg = font_style.render("b - back", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 150])
        elif lang == 0:
            mesg = font_style.render("q - выход", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 50])
            mesg = font_style.render("r - начать заново", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 100])
            mesg = font_style.render("b - назад", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 150])
    def gameLoop(self):
        global dis_width
        global dis_height
        score = 1
        snake_speed = 30
        speed = 10
        enemy_speed=2
        g=int(strftime("%H", gmtime()))*60+int(strftime("%M", gmtime()))*60+int(strftime("%S", gmtime()))
        p=0
        h=0
        m=0
        n=0
        c=0
        asd=1
        game_over = False
        game_close = False
        game_win = False
        snake_block = 10

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        player = pygame.image.load('res/player.png')
        food = pygame.image.load('res/food.png')
        enemy = pygame.image.load('res/enemy.png')
        background = pygame.image.load('res/fon_game.png')
        background = pygame.transform.scale(background, (800, 600))

        foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        while foodx > dis_width or foodx < 0:
            foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while foody > dis_height or foody < 0:
            foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fodx > dis_width or fodx < 0:
            fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fody > dis_height or fody < 0:
            fody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fooody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fooodx > dis_width or fooodx < 0:
            fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fooody > dis_height or fooody < 0:
            fooody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fdy = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fdx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fdx > dis_width or fdx < 0:
            fdx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fdy > dis_height or fdy < 0:
            fdy = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)

        while not game_close:

            while game_over == True:
                dis.fill(black)
                if lang == 1:
                    self.message("You die, you lived: "+str(v+n)+" sec", (214, 48, 49))
                elif lang == 0:
                    self.message("Вы умерли, Вы жили: " + str(v+n) + " сек", (214, 48, 49))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            sys.exit()
                        elif event.key == pygame.K_r:
                            self.gameLoop()
                        elif event.key == pygame.K_b:
                            menu.index(menu())
                    elif event.type == pygame.QUIT:
                        sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True

                keys = pygame.key.get_pressed()

                if keys[pygame.K_a]:
                    x1_change = -speed
                    y1_change = 0
                elif keys[pygame.K_d]:
                    x1_change = speed
                    y1_change = 0
                elif keys[pygame.K_w]:
                    x1_change = 0
                    y1_change = -speed
                elif keys[pygame.K_s]:
                    x1_change = 0
                    y1_change = speed

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        x1_change = 0
                        y1_change = 0
                    elif event.key == pygame.K_d:
                        x1_change = 0
                        y1_change = 0
                    elif event.key == pygame.K_w:
                        y1_change = 0
                        x1_change = 0
                    elif event.key == pygame.K_s:
                        y1_change = 0
                        x1_change = 0
            v=(int(strftime("%H", gmtime()))*60+int(strftime("%M", gmtime()))*60+int(strftime("%S", gmtime())))-int(g)

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_over = True
            x1 += int(x1_change)
            y1 += int(y1_change)
            dis.blit(background, (0, 0))
            self.Your_score(v+n)
            enemy = pygame.transform.scale(enemy, (10, 10))
            enemy_rect = enemy.get_rect(bottomright=(fdx + 10, fdy + 10))
            dis.blit(enemy, enemy_rect)

            food = pygame.transform.scale(food, (10, 10))
            food_rect = food.get_rect(bottomright=(foodx + 10, foody + 10))
            dis.blit(food, food_rect)

            food = pygame.transform.scale(food, (10, 10))
            food_rect = food.get_rect(bottomright=(fooodx + 10, fooody + 10))
            dis.blit(food, food_rect)

            food = pygame.transform.scale(food, (10, 10))
            food_rect = food.get_rect(bottomright=(fodx + 10, fody + 10))
            dis.blit(food, food_rect)

            player = pygame.transform.scale(player, (10, 10))
            player_rect = player.get_rect(bottomright=(x1 + 10, y1 + 10))
            dis.blit(player, player_rect)

            pygame.display.update()
            if h!=v//30:
                h=v//30
                if v//30 != 0:
                    if h==1:
                        if fdx-5>0:
                            fdx=(fdx//10)*10
                        elif fdx-5<0:
                            fdx = ((fdx//10)*10)+5
                        if fdy-5>0:
                            fdy=(fdy//10)*10
                        elif fdy-5<0:
                            fdy = ((fdy//10)*10)+5
                        c=1
                        enemy_speed=5
                    h=v//30
                if asd-score==0:
                    game_over = True
                asd=score
            if c==1:
                font_style = pygame.font.Font('Inkfree.otf', 20)
                if lang == 1:
                    value = font_style.render("The enemy's speed has increased", True, (47, 54, 64))
                elif lang == 0:
                    value = font_style.render("скорость врага увеличилась", True, (47, 54, 64))
                dis.blit(value, [500, 0])

            k=int(fdx)-x1
            l=int(fdy)-y1
            q = fodx - x1
            w = fody - y1
            e = foodx - x1
            r = foody - y1
            t = fooodx - x1
            y = fooody - y1

            if int(k) < 0:fdx+=enemy_speed
            elif int(k) > 0:fdx-=enemy_speed
            elif int(k) == 0:fdx += 0
            if int(l) < 0:fdy+=enemy_speed
            elif int(l) > 0:fdy-=enemy_speed
            elif int(l) == 0:fdy+=0

            if x1 == foodx and y1 == foody:
                foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                while foodx > dis_width or foodx < 0:
                    foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while foody > dis_height or foody < 0:
                    foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                score+=1
                n+=1
            elif x1 == fdx and y1 == fdy:
                game_over = True
            elif x1 == fooodx and y1 == fooody:
                fooody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fooodx > dis_width or fooodx < 0:
                    fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fooody > dis_height or fooody < 0:
                    fooody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                score += 1
                n+=1
            elif x1 == fodx and y1 == fody:
                fody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fodx > dis_width or fodx < 0:
                    fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fody > dis_height or fody < 0:
                    fody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                score += 1
                n+=1
            clock.tick(60)
        sys.exit()
class Game_Three():
    speed = 10
    healts = 6
    score=0
    snake_block = 10
    pop = 20
    snake_speed = 30

    def Your_score(self, scores):
        font_style = pygame.font.Font('Inkfree.otf', 20)
        if lang == 1:
            value = font_style.render("You Score: "+str(scores), True, (47, 54, 64))
        elif lang == 0:
            value = font_style.render("Ваш счет: " + str(scores), True, (47, 54, 64))
        dis.blit(value, [0, 0])

    def message(self, msg, color):
        font_style = pygame.font.Font('Inkfree.otf', 50)
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [150, dis_height / 3])
        if lang == 1:
            mesg = font_style.render("q - quit", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 50])
            mesg = font_style.render("r - restart", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 100])
            mesg = font_style.render("b - back", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 150])
        elif lang == 0:
            mesg = font_style.render("q - выход", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 50])
            mesg = font_style.render("r - начать заново", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 100])
            mesg = font_style.render("b - назад", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 150])

    def gameLoop(self, spd):
        global dis_width
        global dis_height
        score = 0
        snake_speed = 30
        speed = 10
        enemy_speed=spd
        game_over = False
        game_close = False
        snake_block = 10
        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        player = pygame.image.load('res/player.png')
        food = pygame.image.load('res/food.png')
        enemy = pygame.image.load('res/enemy.png')
        background = pygame.image.load('res/fon_game.png')
        background = pygame.transform.scale(background, (800, 600))

        foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        while foodx > dis_width or foodx < 0:
            foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while foody > dis_height or foody < 0:
            foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fodx > dis_width or fodx < 0:
            fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fody > dis_height or fody < 0:
            fody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fooody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fooodx > dis_width or fooodx < 0:
            fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fooody > dis_height or fooody < 0:
            fooody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fdy = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fdx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fdx > dis_width or fdx < 0:
            fdx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fdy > dis_height or fdy < 0:
            fdy = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)

        while not game_close:

            while game_over == True:
                dis.fill(black)
                if lang == 1:
                    self.message("You die, score: "+str(score), (214, 48, 49))
                elif lang == 0:
                    self.message("Вы умерли, счет: " + str(score), (214, 48, 49))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            sys.exit()
                        if event.key == pygame.K_r:
                            self.gameLoop()
                        if event.key == pygame.K_b:
                            menu.index(menu())
                    elif event.type == pygame.QUIT:
                        sys.exit()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a:
                        if event.key == pygame.K_w:
                            x1_change = -speed
                            y1_change = -speed
                        elif event.key == pygame.K_s:
                            x1_change = -speed
                            y1_change = speed
                        elif event.key == pygame.K_d:
                            x1_change = 0
                            y1_change = 0
                        x1_change = -speed
                        y1_change = 0
                        print(event.key)
                    elif event.key == pygame.K_d:
                        x1_change = speed
                        y1_change = 0
                        print(event.key)
                    elif event.key == pygame.K_w:
                        y1_change = -speed
                        x1_change = 0
                        print(event.key)
                    elif event.key == pygame.K_s:
                        y1_change = speed
                        x1_change = 0
                        print(event.key)
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        x1_change = 0
                        y1_change = 0
                    elif event.key == pygame.K_d:
                        x1_change = 0
                        y1_change = 0
                    elif event.key == pygame.K_w:
                        y1_change = 0
                        x1_change = 0
                    elif event.key == pygame.K_s:
                        y1_change = 0
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_over = True

            x1 += int(x1_change)
            y1 += int(y1_change)
            dis.blit(background, (0, 0))
            self.Your_score(score)
            enemy = pygame.transform.scale(enemy, (10, 10))
            enemy_rect = enemy.get_rect(bottomright=(fdx + 10, fdy + 10))
            dis.blit(enemy, enemy_rect)
            food = pygame.transform.scale(food, (10, 10))
            food_rect = food.get_rect(bottomright=(fodx + 10, fody + 10))
            dis.blit(food, food_rect)
            food = pygame.transform.scale(food, (10, 10))
            food_rect = food.get_rect(bottomright=(foodx + 10, foody + 10))
            dis.blit(food, food_rect)
            food = pygame.transform.scale(food, (10, 10))
            food_rect = food.get_rect(bottomright=(fooodx + 10, fooody + 10))
            dis.blit(food, food_rect)
            player = pygame.transform.scale(player, (10, 10))
            player_rect = player.get_rect(bottomright=(x1 + 10, y1 + 10))
            dis.blit(player, player_rect)
            pygame.display.update()

            pygame.display.update()

            k=fdx-x1
            l=fdy-y1
            q = fodx - x1
            w = fody - y1
            e = foodx - x1
            r = foody - y1
            t = fooodx - x1
            y = fooody - y1

            if k < 0:fdx+=enemy_speed
            elif k > 0:fdx-=enemy_speed
            if l < 0:fdy+=enemy_speed
            elif l > 0:fdy-=enemy_speed

            if x1 == foodx and y1 == foody:
                foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                while foodx > dis_width or foodx < 0:
                    foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while foody > dis_height or foody < 0:
                    foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                score+=1
            elif x1 == fdx and y1 == fdy:
                game_over = True
            elif x1 == fooodx and y1 == fooody:
                fooody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fooodx > dis_width or fooodx < 0:
                    fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fooody > dis_height or fooody < 0:
                    fooody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                score += 1
            elif x1 == fodx and y1 == fody:
                fody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fodx > dis_width or fodx < 0:
                    fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fody > dis_height or fody < 0:
                    fody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                score += 1
            clock.tick(60)
        sys.exit()
class Game_One():
    global lang
    speed = 10
    healts = 6
    snake_block = 10
    pop = 20
    snake_speed = 30

    def message(self, msg, color):
        font_style = pygame.font.Font('Inkfree.otf', 50)
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [150, dis_height / 3])
        if lang == 1:
            mesg = font_style.render("q - quit", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 50])
            mesg = font_style.render("r - restart", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 100])
            mesg = font_style.render("b - back", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 150])
        elif lang == 0:
            mesg = font_style.render("q - выход", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 50])
            mesg = font_style.render("r - начать заново", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 100])
            mesg = font_style.render("b - назад", True, color)
            dis.blit(mesg, [150, (dis_height / 3) + 150])


    def gameLoop(self):
        global dis_width
        global dis_height
        score = 1
        snake_speed = 30
        speed = 10
        pop = 20
        healts = 6
        game_over = False
        game_close = False
        game_win = False
        snake_block = 10

        x1 = dis_width / 2
        y1 = dis_height / 2

        x1_change = 0
        y1_change = 0

        player = pygame.image.load('res/player.png')
        food = pygame.image.load('res/food.png')
        enemy = pygame.image.load('res/enemy.png')
        background = pygame.image.load('res/fon_game.png')
        background = pygame.transform.scale(background, (800, 600))

        foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        while foodx > dis_width or foodx < 0:
            foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while foody > dis_height or foody < 0:
            foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fodx > dis_width or fodx < 0:
            fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fody > dis_height or fody < 0:
            fody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fooody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fooodx > dis_width or fooodx < 0:
            fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fooody > dis_height or fooody < 0:
            fooody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
        fdy = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        fdx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fdx > dis_width or fdx < 0:
            fdx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
        while fdy > dis_height or fdy < 0:
            fdy = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)

        while not game_close:

            while game_over == True:
                dis.fill(black)
                if lang == 1:
                    self.message("You die", (214, 48, 49))
                elif lang == 0:
                    self.message("Вы умерли", (214, 48, 49))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            sys.exit()
                        if event.key == pygame.K_r:
                            self.gameLoop()
                        if event.key == pygame.K_b:
                            menu.index(menu())
                    elif event.type == pygame.QUIT:
                        sys.exit()
            while game_win == True:
                dis.fill(black)
                if lang == 1:
                    self.message("You win", (0, 184, 148))
                if lang == 0:
                    self.message("Вы победили", (0, 184, 148))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            sys.exit()
                        if event.key == pygame.K_c:
                            self.gameLoop()
                        if event.key == pygame.K_b:
                            menu.index(menu())
                    elif event.type == pygame.QUIT:
                        sys.exit()
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and keys[pygame.K_w]:
                x1_change = -speed
                y1_change = -speed
            elif keys[pygame.K_a] and keys[pygame.K_s]:
                x1_change = -speed
                y1_change = speed
            elif keys[pygame.K_a] and keys[pygame.K_d]:
                x1_change = 0
                y1_change = 0
            elif keys[pygame.K_a]:
                x1_change = -speed
                y1_change = 0
            elif keys[pygame.K_d] and keys[pygame.K_w]:
                x1_change = speed
                y1_change = -speed
            elif keys[pygame.K_d] and keys[pygame.K_s]:
                x1_change = speed
                y1_change = speed
            elif keys[pygame.K_d]:
                x1_change = speed
                y1_change = 0
            elif keys[pygame.K_w] and keys[pygame.K_s]:
                x1_change = 0
                y1_change = 0
            elif keys[pygame.K_w]:
                x1_change = 0
                y1_change = -speed
            elif keys[pygame.K_s]:
                x1_change = 0
                y1_change = speed

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_close = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_a:
                        x1_change = 0
                        y1_change = 0
                    elif event.key == pygame.K_d:
                        x1_change = 0
                        y1_change = 0
                    elif event.key == pygame.K_w:
                        y1_change = 0
                        x1_change = 0
                    elif event.key == pygame.K_s:
                        y1_change = 0
                        x1_change = 0

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_over = True

            x1 += int(x1_change)
            y1 += int(y1_change)

            dis.blit(background, (0, 0))
            helt00 = pygame.draw.rect(dis, black, [0, 0, 120, pop])
            if healts >= 6: helt5 = pygame.draw.rect(dis, (231, 76, 60), [100, 0, pop, pop])
            if healts >= 5: helt4 = pygame.draw.rect(dis, (231, 76, 60), [80, 0, pop, pop])
            if healts >= 4: helt3 = pygame.draw.rect(dis, (231, 76, 60), [60, 0, pop, pop])
            if healts >= 3: helt2 = pygame.draw.rect(dis, (231, 76, 60), [40, 0, pop, pop])
            if healts >= 2: helt1 = pygame.draw.rect(dis, (231, 76, 60), [20, 0, pop, pop])
            if healts >= 4:
                food = pygame.transform.scale(food, (10, 10))
                food_rect = food.get_rect(bottomright=(foodx + 10, foody + 10))
                dis.blit(food, food_rect)
            if healts >= 2:
                food = pygame.transform.scale(food, (10, 10))
                food_rect = food.get_rect(bottomright=(fooodx + 10, fooody + 10))
                dis.blit(food, food_rect)
            helt= pygame.draw.rect(dis, (231, 76, 60), [0, 0, pop, pop])

            enemy = pygame.transform.scale(enemy, (10, 10))
            enemy_rect = enemy.get_rect(bottomright=(fdx + 10, fdy + 10))
            dis.blit(enemy, enemy_rect)

            food = pygame.transform.scale(food, (10, 10))
            food_rect = food.get_rect(bottomright=(fodx + 10, fody + 10))
            dis.blit(food, food_rect)

            player = pygame.transform.scale(player, (10, 10))
            player_rect = player.get_rect(bottomright=(x1+10, y1+10))
            dis.blit(player, player_rect)

            pygame.display.update()

            pygame.display.update()

            k=fdx-x1
            l=fdy-y1
            q = fodx - x1
            w = fody - y1
            e = foodx - x1
            r = foody - y1
            t = fooodx - x1
            y = fooody - y1

            if k < 0:fdx+=int(speed//4)
            elif k > 0:fdx-=int(speed//4)
            if l < 0:fdy+=int(speed//4)
            elif l > 0:fdy-=int(speed//4)

            if healts <= 0:
                game_win=True

            if x1 == foodx and y1 == foody and healts >= 4:
                foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                while foodx > dis_width or foodx < 0:
                    foodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while foody > dis_height or foody < 0:
                    foody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                healts-=1
                print(score)
            elif x1 == fdx and y1 == fdy:
                game_over = True
            elif x1 == fooodx and y1 == fooody and healts >= 2:
                fooody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fooodx > dis_width or fooodx < 0:
                    fooodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fooody > dis_height or fooody < 0:
                    fooody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                healts -= 1
                print(score)
            elif x1 == fodx and y1 == fody:
                fody = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fodx > dis_width or fodx < 0:
                    fodx = int(round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0)
                while fody > dis_height or fody < 0:
                    fody = int(round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0)
                healts -= 1
                print(score)
            clock.tick(snake_speed)
        sys.exit()
class menu():
    def complexity(self):
        global lang
        global scr
        run = True
        choice = 1
        background = pygame.image.load('res/fon.png')
        background = pygame.transform.scale(background, (800, 600))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_DOWN:
                        choice += 1
                    elif event.key == pygame.K_UP:
                        choice -= 1
                    elif event.key == pygame.K_RETURN:
                        if choice == 1:
                            Game_Three.gameLoop(Game_Three(), 2)
                        elif choice == 2:
                            Game_Three.gameLoop(Game_Three(), 5)
                        elif choice == 3:
                            self.start()
                elif event.type == pygame.QUIT:
                    sys.exit()
            dis.blit(background, (0, 0))
            if choice == 1:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('easy', True, white)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('normal', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    mes = font_style.render('back', True, black)
                    dis.blit(mes, [50, dis_height-50])
                elif lang == 0:
                    mesg = font_style.render('легко', True, white)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('нормально', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    mes = font_style.render('назад', True, black)
                    dis.blit(mes, [50, dis_height-50])
            elif choice == 2:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('easy', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('normal', True, white)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    mes = font_style.render('back', True, black)
                    dis.blit(mes, [50, dis_height - 50])
                elif lang == 0:
                    mesg = font_style.render('легко', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('нормально', True, white)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    mes = font_style.render('назад', True, black)
                    dis.blit(mes, [50, dis_height - 50])
            elif choice == 3:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('easy', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('normal', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    mes = font_style.render('back', True, white)
                    dis.blit(mes, [50, dis_height - 50])
                elif lang == 0:
                    mesg = font_style.render('легко', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('нормально', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    mes = font_style.render('назад', True, white)
                    dis.blit(mes, [50, dis_height - 50])
            elif choice > 3:
                choice = 3
            elif choice < 1:
                choice = 1
            pygame.display.update()
    def start(self):
        global lang
        global scr
        run = True
        choice = 1
        background = pygame.image.load('res/fon.png')
        background = pygame.transform.scale(background, (800, 600))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_DOWN:
                        choice += 1
                    elif event.key == pygame.K_UP:
                        choice -= 1
                    elif event.key == pygame.K_RETURN:
                        if choice == 1:
                            Game_One.gameLoop(Game_One())
                        elif choice == 2:
                            Game_Two.gameLoop(Game_Two())
                        elif choice == 3:
                            self.complexity()
                        elif choice == 4:
                            self.index()
                elif event.type == pygame.QUIT:
                    sys.exit()
            dis.blit(background, (0, 0))
            if choice == 1:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('kill the cube', True, white)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('play for a while', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('collect the most points', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                    msg = font_style.render('back', True, black)
                    dis.blit(msg, [50, dis_height - 50])
                elif lang == 0:
                    mesg = font_style.render('Убей куб', True, white)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('Играй на время', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    font_style = pygame.font.Font('Inkfree.otf', 45)
                    msg = font_style.render('Собери большее количество очков', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                    msg = font_style.render('Назад', True, black)
                    dis.blit(msg, [50, dis_height - 50])
            elif choice == 2:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('kill the cube', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('play for a while', True, white)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('collect the most points', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                    msg = font_style.render('back', True, black)
                    dis.blit(msg, [50, dis_height - 50])
                elif lang == 0:
                    mesg = font_style.render('Убей куб', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('Играй на время', True, white)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    font_style = pygame.font.Font('Inkfree.otf', 45)
                    msg = font_style.render('Собери большее количество очков', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                    msg = font_style.render('Назад', True, black)
                    dis.blit(msg, [50, dis_height - 50])
            elif choice == 3:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('kill the cube', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('play for a while', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('collect the most points', True, white)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                    msg = font_style.render('back', True, black)
                    dis.blit(msg, [50, dis_height - 50])
                elif lang == 0:
                    mesg = font_style.render('Убей куб', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('Играй на время', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    font_style = pygame.font.Font('Inkfree.otf', 45)
                    msg = font_style.render('Собери большее количество очков', True, white)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                    msg = font_style.render('Назад', True, black)
                    dis.blit(msg, [50, dis_height - 50])
            elif choice == 4:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('kill the cube', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('play for a while', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('collect the most points', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                    msg = font_style.render('back', True, white)
                    dis.blit(msg, [50, dis_height - 50])
                elif lang == 0:
                    mesg = font_style.render('Убей куб', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('Играй на время', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    font_style = pygame.font.Font('Inkfree.otf', 45)
                    msg = font_style.render('Собери большее количество очков', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                    msg = font_style.render('Назад', True, white)
                    dis.blit(msg, [50, dis_height - 50])
            elif choice > 4:
                choice = 4
            elif choice < 1:
                choice = 1
            pygame.display.update()
    def settings(self):
        global lang
        global scr
        choice=1
        i = lang
        run = True
        background = pygame.image.load('res/fon.png')
        background = pygame.transform.scale(background, (800, 600))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_DOWN:
                        choice+=1
                    elif event.key == pygame.K_UP:
                        choice -= 1
                    elif event.key == pygame.K_LEFT:
                        if choice == 1:
                            if i<1:
                                i+=1
                    elif event.key == pygame.K_RIGHT:
                        if choice == 1:
                            if i>0:
                                i-=1
                    elif event.key == pygame.K_RETURN:
                        if choice == 1:
                            pass
                        elif choice == 2:
                            self.index()
                elif event.type == pygame.QUIT:
                    sys.exit()
            dis.blit(background, (0, 0))
            lang = i
            if choice==1:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if i == 0:
                    mesg = font_style.render('язык: Русский', True, white)
                    dis.blit(mesg, [dis_width / 3, (dis_height / 3) - 50])
                    msg = font_style.render('назад', True, black)
                    dis.blit(msg, [dis_width / 3, (dis_height / 1.5) - 50])
                elif i == 1:
                    mesg = font_style.render('language: ENG', True, white)
                    dis.blit(mesg, [dis_width / 3, (dis_height / 3) - 50])
                    msg = font_style.render('back', True, black)
                    dis.blit(msg, [dis_width / 3, (dis_height / 1.5) - 50])
            elif choice==2:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if i == 0:
                    mesg = font_style.render('язык: Русский', True, black)
                    dis.blit(mesg, [dis_width / 3, (dis_height / 3) - 50])
                    msg = font_style.render('назад', True, white)
                    dis.blit(msg, [dis_width / 3, (dis_height / 1.5) - 50])
                elif i == 1:
                    mesg = font_style.render('language: ENG', True, black)
                    dis.blit(mesg, [dis_width / 3, (dis_height / 3) - 50])
                    msg = font_style.render('back', True, white)
                    dis.blit(msg, [dis_width / 3, (dis_height / 1.5) - 50])
            elif choice > 2:
                choice = 2
            elif choice < 1:
                choice=1
            pygame.display.update()
    def index(self):
        global lang
        global scr
        global dis_height
        global dis_width
        run = True
        choice=1
        background = pygame.image.load('res/fon.png')
        background = pygame.transform.scale(background, (800, 600))
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()
                    elif event.key == pygame.K_DOWN:
                        choice+=1
                    elif event.key == pygame.K_UP:
                        choice -= 1
                    elif event.key == pygame.K_RETURN:
                        if choice == 1:
                            self.start()
                        elif choice == 2:
                            self.settings()
                        elif choice == 3:
                            sys.exit()
                elif event.type == pygame.QUIT:
                    sys.exit()
            dis.blit(background, (0, 0))
            if choice==1:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('start', True, white)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('settings', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('quit', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                if lang == 0:
                    mesg = font_style.render('старт', True, white)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('настройки', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('выход', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
            elif choice==2:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('start', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('settings', True, white)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('quit', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                if lang == 0:
                    mesg = font_style.render('старт', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('настройки', True, white)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('выход', True, black)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
            elif choice==3:
                font_style = pygame.font.Font('Inkfree.otf', 50)
                if lang == 1:
                    mesg = font_style.render('start', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('settings', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('quit', True, white)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
                if lang == 0:
                    mesg = font_style.render('старт', True, black)
                    dis.blit(mesg, [50, (dis_height / 3) - 50])
                    mes = font_style.render('настройки', True, black)
                    dis.blit(mes, [50, (dis_height / 2) - 50])
                    msg = font_style.render('выход', True, white)
                    dis.blit(msg, [50, (dis_height / 1.5) - 50])
            elif choice > 3:
                choice = 3
            elif choice < 1:
                choice=1
            pygame.display.update()

menu.index(menu())