# pylint: skip-file
#this is ui code, so it does not need to be checked by pylint
import pygame
import sys
from word_snack import WordSnack
from reader import Reader


class UI:
    def __init__(self, res=(1280,800)):
        self.res = res
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
                if width/2 <= mouse[0] <= width/2+300 and height/2-300 <= mouse[1] <= height/2:
                    pygame.quit()
                    self.display_word_snack()


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
          if width/2 <= mouse[0] <= width/2+300 and height/2-300 <= mouse[1] <= height/2:
              pygame.draw.rect(screen,color_light,[width/2,height/2-100,300,40])

          else:
              pygame.draw.rect(screen,color_dark,[width/2,height/2-100,300,40])
          screen.blit(word_snack_button , (width/2+50,height/2-100))

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
        words = reader.read_from_file("src/resources/sanat.txt") #TODO : make this not hardcoded
        found_words = None
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
        return_to_menu_button = smallfont.render('return to menu' , True , color)
        text =""
        running = True
        input_active = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if 0 <= mouse[0] <= 300 and 0 <= mouse[1] <= 40:
                        pygame.quit()
                        self.display_menu()
                    input_active = True
                    text = ""
                if event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_RETURN:
                        input_active = False
                        found_words = word_snack.find_words(text)
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
            screen.blit(return_to_menu_button , (0,0))
            input_text = bigfont.render(text, True, (255, 0, 0))
            screen.blit(input_text, (width/2, 10))
            if not input_active:
                input_text = bigfont.render("found words:", True, (255, 0, 0))
                screen.blit(input_text, (width/2, 100))
                i = 140
                for word in found_words:
                    input_text = smallfont.render(word, True, (255, 0, 0))
                    screen.blit(input_text, (width/2, 10+i))
                    i+=40
            pygame.display.flip()
            clock.tick(30)
