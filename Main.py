#Mya Daniels and Brandon Bankston
#12/6/23
#Creating the Game Hangman using Pygame
import sys
import random
import pygame
#Button class import 
from button import Button
#Iniizalize pygame and set screen size
pygame.init() 
SCREEN = pygame.display.set_mode((728, 552)) #image is this size

pygame.display.set_caption("Menu") #main menu

BG = pygame.image.load("black.jpeg")#the black background

#Font of buttons
def get_font(size): # Returns Press-Start-2P in the desired size
  return pygame.font.SysFont("arial", size) 
#Methods for the buttons (play,options,quit)
def play():
 #Game logic from game.py
  def random_word():
      words = ["python", "quiz", "math", "joker", "funny", "softdev", "programming", "fun", "start","run", "eat", "massachusetts", "kentucky", "missouri", "kansas", "blue", "horse", "monkey", "chicken", "apple", "hangman", "button", "code", "letter", "method", "christmas", "santa", "shoe"]
      return random.choice(words)
  #Displays the "_" for the number of letters in the word
  def display_word(word, guessed_letters):
      display = ""
      for letter in word:
          if letter in guessed_letters:
              display += letter + " "
          else:
              display += "_ "
      return display.strip()
#Set screen size/font/color
  def hangman():
      pygame.init()
      screen = pygame.display.set_mode((640, 480))
      font = pygame.font.SysFont("Comic Sans", 25)
      word_to_guess = random_word()
      guessed_letters = []
      incorrect_letters = [] #Empty lists to store
      guesses_left = 6 #There are 6 images so guesses has to be ==
      images = [pygame.image.load(f"hangman{i}.jpeg") for i in range(guesses_left)]#create a list to store images that generates the file names for the images
      while True:
          for event in pygame.event.get():#Sets up the game so that it listens for keyboard presses or mouse clicks and it wont end unless the quit button is pressed or the window is closed 
              if event.type == pygame.QUIT:
                  pygame.quit()#quit game
                  return
              elif event.type == pygame.KEYDOWN:#waits for a key to be pressed trasnforms it into a lowercase letter then checks if its only 1 and if it is it checks the guess
                  guess = chr(event.key).lower()
                  if guess.isalpha() and len(guess) == 1:
                      if guess in guessed_letters:
                          pygame.display.set_caption("You have already attempted that letter. Try again.")
                      elif guess in word_to_guess:
                          pygame.display.set_caption("Great Guess. Keep going.")
                          guessed_letters.append(guess)
                      else:
                          pygame.display.set_caption("Incorrect guess. Try again.")
                          incorrect_letters.append(guess)
                          guesses_left -= 1#Guess is subtracted and pciture is added if guess is wrong
                  else:
                      pygame.display.set_caption("Invalid Input. Please enter one letter at a time.")
          screen.fill((255, 255, 255))
          text = font.render(display_word(word_to_guess, guessed_letters), True, (0, 0, 0))
          screen.blit(text, (150, 250))
          text = font.render(f"Attempts left: {guesses_left}", True, (0, 0, 0))
          screen.blit(text, (150, 350))
          text = font.render("Incorrect letters: " + ", ".join(incorrect_letters), True, (0, 0, 0))#Shows the incorrect guesses
          screen.blit(text, (150, 400))
          if set(word_to_guess) <= set(guessed_letters):
            pygame.display.set_caption(f"Congrats, you've won the game by guessing the word: {word_to_guess}")
            pygame.time.wait(3000)
            pygame.quit()
            return
          if guesses_left < len(images):
            screen.blit(images[guesses_left], (450, 50))
          pygame.display.flip()
          if guesses_left == 0:
              pygame.display.set_caption(f"The correct word was {word_to_guess}. Better luck next time!")
              pygame.time.wait(3000)#Waits 3 seconds before closing the winow 
              pygame.quit()
              return

  hangman()#call the game

  

  
  while True: #original condition for the play screen before we added game logic
      PLAY_MOUSE_POS = pygame.mouse.get_pos() 

      SCREEN.fill("black") 

      PLAY_TEXT = get_font(25).render("This is the PLAY screen.", True, "White") 
      PLAY_RECT = PLAY_TEXT.get_rect(center=(385, 100)) 
      SCREEN.blit(PLAY_TEXT, PLAY_RECT) 

      PLAY_BACK = Button(image=None, pos=(600, 400), 
                       text_input="BACK", font=get_font(35), base_color="White", hovering_color="#b68f40") 

      PLAY_BACK.changeColor(PLAY_MOUSE_POS) 
      PLAY_BACK.update(SCREEN) 

      for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
          pygame.quit() 
          sys.exit() 
        if event.type == pygame.MOUSEBUTTONDOWN:
          if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
            main_menu() 
      pygame.display.update() 
#Options (Rules Screen)
def options(): 
  while True: 
    OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
    SCREEN.fill((182, 143, 64))#Color of scrren
    OPTIONS_TEXT = get_font(45).render("Hangman Game Rules", True, (255,255,255))#Displays the rules
    OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(SCREEN.get_width() / 2, SCREEN.get_height() / 4))#Not centered but a title
    SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)
    RULES_TEXT1 = get_font(25).render("1. A random word will be selected", True, (255, 255, 255))
    RULES_RECT1 = RULES_TEXT1.get_rect(center=(350,200))
    SCREEN.blit(RULES_TEXT1, RULES_RECT1)
    RULES_TEXT2 = get_font(25).render("2. Guess one letter at a time.", True, (255, 255, 255))
    RULES_RECT2 = RULES_TEXT2.get_rect(center=(350,275))
    SCREEN.blit(RULES_TEXT2, RULES_RECT2)
    RULES_TEXT3 = get_font(25).render("3. Attempt to guess word before guesses run out", True, (255, 255, 255))
    RULES_RECT3 = RULES_TEXT3.get_rect(center=(370,350))
    SCREEN.blit(RULES_TEXT3, RULES_RECT3)
    OPTIONS_BACK = Button(image=None, pos=(600, 400),
                          text_input="BACK", font=get_font(35), base_color="Black", hovering_color="#b68f40")
    OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
    OPTIONS_BACK.update(SCREEN)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                main_menu()
    pygame.display.update()
#Main menu
def main_menu(): #Displays "menu"
  while True:
    SCREEN.blit(BG, (0, 0)) 

    MENU_MOUSE_POS = pygame.mouse.get_pos() #checks if mouse is clicking

    MENU_TEXT = get_font(80).render("Hangman", True, "#b68f40")     
    MENU_RECT = MENU_TEXT.get_rect(center=(375, 75)) 

    PLAY_BUTTON = Button(image=pygame.image.load("button.png"), pos=(375, 245), 
                         text_input="PLAY", font=get_font(25), base_color="#b68f40", hovering_color="White") 

    OPTIONS_BUTTON = Button(image=pygame.image.load("button.png"), pos=(600, 350), 
                            text_input="RULES", font=get_font(25), base_color="#b68f40", hovering_color="White") 

    QUIT_BUTTON = Button(image=pygame.image.load("button.png"), pos=(150, 350), 
                         text_input="QUIT", font=get_font(25), base_color="#b68f40", hovering_color="White") 

    SCREEN.blit(MENU_TEXT, MENU_RECT) 

    for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
      button.changeColor(MENU_MOUSE_POS) #if mouse is hovering
      button.update(SCREEN) #if clicked screen will switch 

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit() 
        sys.exit() 
      if event.type == pygame.MOUSEBUTTONDOWN:
        if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS): 
          play() 
        if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS): 
          options() 
        if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS): 
          pygame.quit() 
          sys.exit() 
    pygame.display.update() 

main_menu() 
