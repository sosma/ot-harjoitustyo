# pylint: skip-file
#this is ui code, so it does not need to be checked by pylint
import pygame
import sys
import re
from logic.word_snack import WordSnack
from logic.hangman import Hangman
from data_managament.reader import Reader


class UI:
    def __init__(self, res=(1280,800), path="src/resources/sanat.txt"):
        self.res = res
        self.path = path
    def display_menu(self):
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.res)
        width, height = screen.get_width(), screen.get_height()
        """
        colors
        """
        color = (255,0,0)
        color_light = (170,170,170)
        color_dark = (100,100,100)


        helper_image = pygame.image.load("src/resources/apustaja.png")
        helper_rect = helper_image.get_rect()

        smallfont = pygame.font.SysFont('Corbel',35)
        bigfont = pygame.font.SysFont('Corbel',60)
        quit_button = smallfont.render('quit' , True , color)
        word_snack_button = smallfont.render('word snack' , True , color)
        hangman_button = smallfont.render('hangman' , True , color)
        title = bigfont.render('word game helper' , True , color)
        running = True
        while running:
          for event in pygame.event.get():
            if event.type == pygame.QUIT:
              running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                """
                quit button pressed
                """
                if width/2 <= mouse[0] <= width/2+300 and height/2 <= mouse[1] <= height/2+40:
                    pygame.quit()
                    exit()

                """
                word snack button pressed
                """
                if width/2 <= mouse[0] <= width/2+300 and height/2-100 <= mouse[1] <= height/2-60:
                    pygame.quit()
                    self.display_word_snack()
                    return 0

                """
                hangman snack button pressed
                """
                if width/2 <= mouse[0] <= width/2+300 and height/2-200 <= mouse[1] <= height/2-160:
                    pygame.quit()
                    self.display_hangman()
                    return 0
          mouse = pygame.mouse.get_pos()
          screen.fill(0)
          """
          draw quit button
          """
          if width/2 <= mouse[0] <= width/2+300 and height/2 <= mouse[1] <= height/2+40:
              pygame.draw.rect(screen,color_light,[width/2,height/2,300,40])

          else:
              pygame.draw.rect(screen,color_dark,[width/2,height/2,300,40])
          screen.blit(quit_button , (width/2+50,height/2))
          """
          draw word snack button
          """
          if width/2 <= mouse[0] <= width/2+300 and height/2-100 <= mouse[1] <= height/2-60:
              pygame.draw.rect(screen,color_light,[width/2,height/2-100,300,40])

          else:
              pygame.draw.rect(screen,color_dark,[width/2,height/2-100,300,40])
          screen.blit(word_snack_button , (width/2+50,height/2-100))


          """
          draw hangman button
          """
          if width/2 <= mouse[0] <= width/2+300 and height/2-200 <= mouse[1] <= height/2-160:
              pygame.draw.rect(screen,color_light,[width/2,height/2-200,300,40])

          else:
              pygame.draw.rect(screen,color_dark,[width/2,height/2-200,300,40])
          screen.blit(hangman_button , (width/2+50,height/2-200))


          """
          draw helper and title
          """
          screen.blit(title , (width/2,height/2-300))
          screen.blit(helper_image, helper_rect)

          pygame.display.flip()
          clock.tick(30)

    def display_word_snack(self):

        """
        initilize game logic objects
        """
        reader = Reader()
        words = reader.read_from_file(self.path)
        foundWords = None
        word_snack = WordSnack(words)
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.res)
        width, height = screen.get_width(), screen.get_height()

        """
        colors
        """
        color = (255,0,0)
        color_light = (170,170,170)
        color_dark = (100,100,100)


        """
        return button
        """
        smallfont = pygame.font.SysFont('Corbel',35)
        bigfont = pygame.font.SysFont('Corbel',60)
        returnToMenuButton = smallfont.render('return to menu' , True , color)
        text =""
        running = True
        inputActive = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                """
                return to menu button clicked
                """
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 300 and 0 <= mouse[1] <= 40:
                        pygame.quit()
                        self.display_menu()
                        return 0
                    inputActive = True
                    text = ""
                if event.type == pygame.KEYDOWN and inputActive:
                    if event.key == pygame.K_RETURN:
                        inputActive = False
                        foundWords = word_snack.find_words(text)
                    elif event.key == pygame.K_BACKSPACE:
                        text =  text[:-1]
                    else:
                        text += pygame.key.name(event.key)
            mouse = pygame.mouse.get_pos()

            screen.fill(0)
            if 0 <= mouse[0] <= 300 and 0 <= mouse[1] <= 40:
                pygame.draw.rect(screen,color_light,[0,0,300,40])

            else:
                pygame.draw.rect(screen,color_dark,[0,0,300,40])
            screen.blit(returnToMenuButton , (0,0))
            input_text = bigfont.render(text, True, (255, 0, 0))
            screen.blit(input_text, (width/2, 10))
            if not inputActive:
                input_text = bigfont.render("found words:", True, (255, 0, 0))
                screen.blit(input_text, (width/2, 100))
                i = 140
                k=50
                for word in foundWords:
                    if i>=600:
                        i=140
                        k+=100
                    input_text = smallfont.render(word, True, (255, 0, 0))
                    screen.blit(input_text, (width/2+k, 10+i))
                    i+=40
            pygame.display.flip()
            clock.tick(30)
    def display_hangman(self):

        """
        initilize game logic objects
        """
        reader = Reader()
        words = reader.read_from_file(self.path)
        hangman = Hangman(words)
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(self.res)
        width, height = screen.get_width(), screen.get_height()

        """
        colors
        """
        color = (255,0,0)
        color_light = (170,170,170)
        color_dark = (100,100,100)


        """
        return button
        """
        smallfont = pygame.font.SysFont('Corbel',35)
        bigfont = pygame.font.SysFont('Corbel',60)
        returnToMenuButton = smallfont.render('return to menu' , True , color)
        resetButton = smallfont.render('reset' , True , color)
        numberOfLetters = smallfont.render('how many letters?' , True , color)
        gameState = None
        running = True
        lettercount = None
        inputActive = False
        foundLetter = None
        gotInput = True
        text = ""
        while running:
            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


                """
                return to menu button clicked
                """
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 300 and 0 <= mouse[1] <= 40:
                        pygame.quit()
                        self.display_menu()
                        return 0
                """
                rest game when reset button clicked
                """
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width-300 <= mouse[0] <= width and 0 <= mouse[1] <= 40:
                        text = ""
                        lettercount = None
                        gameState = None
                        hangman.reset()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if inputActive:
                            inputActive = False
                        if lettercount == None:
                            lettercount = int(text)
                            gameState = lettercount*"_"

                        """
                        game logic find possible words and decide what is the best next guess
                        """
                        if gotInput == False:
                            hangman.miss(foundLetter)
                        foundWords = hangman.find_words(lettercount, gameState)
                        foundLetter = hangman.guess(foundWords, gameState)
                        inputActive = True
                        gotInput = False

                    elif event.key == pygame.K_BACKSPACE:
                        text =  text[:-1]
                    else:
                        if re.match("[0-9]", pygame.key.name(event.key)):
                            text += pygame.key.name(event.key)
                """
                check if any of the letter boxes where clicked
                """
                i = 100
                if gameState != None and inputActive:
                    for j in range(len(gameState)):
                        if event.type == pygame.MOUSEBUTTONDOWN and i <= mouse[0] <= i+40 and height/2 <= mouse[1] <= height/2+40 and gameState[j] == "_":
                            gameStateTmp = list(gameState)
                            gameStateTmp[j] = foundLetter
                            gameState = ''.join(gameStateTmp)
                            gotInput = True
                        i+=60


            screen.fill(0)

            """
            draw menu button
            """
            if 0 <= mouse[0] <= 300 and 0 <= mouse[1] <= 40:
                pygame.draw.rect(screen,color_light,[0,0,300,40])

            else:
                pygame.draw.rect(screen,color_dark,[0,0,300,40])
            screen.blit(returnToMenuButton , (0,0))

            """
            draw reset button
            """
            if width-300 <= mouse[0] <= width and 0 <= mouse[1] <= 40:
                pygame.draw.rect(screen,color_light,[width-300,0,300,40])

            else:
                pygame.draw.rect(screen,color_dark,[width-300,0,300,40])
            screen.blit(resetButton , (width-300,0))

            """
            draw how many letters if lettercount not given
            """
            screen.blit(numberOfLetters , (width/2-150,0))

            """
            draw amount of letters
            """
            input_text = smallfont.render(text, True, (255, 0, 0))
            screen.blit(input_text, (width/2-150, 30))

            """
            draw missed letters
            """
            input_text = smallfont.render("missed letters: " + hangman.missed, True, (255, 0, 0))
            screen.blit(input_text, (100, height/2-150))

            """
            draw letters
            """
            if gameState != None:
                """
                draw letter guessed by game
                """
                input_text = smallfont.render("found letter: " +foundLetter, True, (255, 0, 0))
                screen.blit(input_text, (width/2-150, 50))


                """
                draw letters
                """
                i = 100
                for letter in gameState:
                    if i <= mouse[0] <= i+40 and height/2 <= mouse[1] <= height/2+40 and letter == "_":
                        pygame.draw.rect(screen,color_light,[i,height/2,40,40])

                    else:
                        pygame.draw.rect(screen,color_dark,[i,height/2,40,40])
                    input_text = bigfont.render(letter, True, (255, 0, 0))
                    screen.blit(input_text, (i, height/2))
                    i+=60


            pygame.display.flip()
            clock.tick(30)
