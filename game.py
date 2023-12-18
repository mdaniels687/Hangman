import random
import pygame
#Game logic for the game hangman
def random_word():
  words = ["python", "quiz", "math", "joker", "funny", "softdev", "programming", "fun", "start","run", "eat", "massachusetts", "kentucky", "missouri", "kansas", "blue", "horse", "zebra", "lebron", "apple", "hangman", "button", "code", "letter", "method", "christmas", "santa", "shoe"]
  return random.choice(words)
#Displays the "_" for the number of letters in the word
def display_word(word, guessed_letters):
  display = ""
  #Create a function to take two arguments in
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
  font = pygame.font.SysFont("Comic Sans", 25)#set font and size
  word_to_guess = random_word()
  guessed_letters = []#empty list to store guessed letters
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
      screen.fill((182, 143, 64))#Screen.blit draws images onto game
      text = font.render(display_word(word_to_guess, guessed_letters), True, (0, 0, 0))
      screen.blit(text, (150, 250))
      text = font.render(f"Attempts left: {guesses_left}", True, (0, 0, 0))
      screen.blit(text, (150, 350))
      text = font.render("Incorrect letters: " + ", ".join(incorrect_letters), True, (0, 0, 0))#Shows the incorrect guesses
      screen.blit(text, (150, 400))
      if guesses_left < len(images):
        screen.blit(images[guesses_left], (150, 50))
      pygame.display.flip()
      if guesses_left == 0:
          pygame.display.set_caption(f"The correct word was {word_to_guess}. Better luck next time!")
          pygame.time.wait(3000)#Waits 3 seconds before closing the winow 
          pygame.quit()
          return

hangman()#call the game
