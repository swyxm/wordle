#Developed by Swayam Parekh, April 13th 2022

import pygame
import random

#initializing the pygame playing window 
pygame.init()
width1 = 400
height1 = 560
SIZE = (width1,height1)

#Initializing the pygame menu window
width2 = 800
height2 = 240
screen = pygame.display.set_mode(SIZE)
SIZE2 = (width2,height2)
introscreen = pygame.display.set_mode(SIZE2) 

#Setting up the main UI fonts only
letterFont = pygame.font.SysFont("Helvetica", 42)
bodyFont = pygame.font.SysFont("Helvetica", 20) #Instructions

#Setting up the colours
GRAY = (69, 69, 75)
BLACK = (24, 24, 24)
GREEN = (83, 141, 78)
YELLOW = (181, 159, 59)
WHITE = (255, 255, 255)

#Initializing key boolean values
running = False
solved = False
intro = True

#Setting up the wordbank
wordList = ["OCEAN", "WIDTH", "JUMPS", "STONE", "ARIAS", "ANVIL", "NAILS", "JOKEY", "QUAKE", "FROZE", "ROCKS", "ROCKY", "QUICK", "JERKY", "HYDRO", "SHADE", "LOOKS", "JUICY", "CRAZY", "HAZED", "TASED", "TASER", "AMBER", "QUIRK", "QUARK", "STAMP'", "FUSED", "DINGY", "STICK", "GLUED", "PASTE", ]
secretWord = random.choice(wordList)
guessList = []

#Setting up key counters
letterCounter = 0
attemptCounter = 0
gameplayBgState = 0
letterX = 55
letterY = 93

myClock = pygame.time.Clock()

def guessChecker(ypos, guessList, secretWord): 
    correct = 0
    for allLetters in range(5):
        #if statement checks not only for the correct letter but also the correct position, draws green sqaure
        if guessList[allLetters] == secretWord[allLetters]:
            pygame.draw.rect(screen, GREEN, ((36 + allLetters*67), (78 + ypos*67), 63, 63)) 
            correct += 1
        #elif statement checks only for the correct letter. none of the words in the bank have repeat letters so >=1 is there   
        elif secretWord.find(guessList[allLetters]) >= 1: 
            pygame.draw.rect(screen, YELLOW, ((36 + allLetters*67), (78 + ypos*67), 63, 63)) 
        #in the case of everything being incorrect   
        else: 
            pygame.draw.rect(screen, GRAY, ((36 + allLetters*67), (78 + ypos*67), 63, 63)) 
            
    #returns True boolean for the main game loop
    if correct == 5:
        return(True)

#displays guesses
def textDisplay(guessList, attemptCounter): 
    letterX = 55
    letterY = 93 + attemptCounter*67
    
    for allLetters in range(5):
        text = letterFont.render(guessList[allLetters], 1, WHITE)
        screen.blit(text, (letterX, letterY, 10, 10))    
        letterX += 67

#formats text 
def textOutput(bodyFont, screen, WHITE, text, ypos): 
    letterDisplay = bodyFont.render(text, 1, WHITE)
    screen.blit(letterDisplay, (200, 78 + ypos*42, 10, 10))       
    pygame.display.flip()
    myClock.tick(60)      

#Draws on top of a 6th word.        
def wordDeleter(guessList, attemptCounter): 
    letter_a = ()
    letter_a = len(guessList)
    pygame.draw.rect(screen, BLACK, ((43+(letter_a*67), (85+(attemptCounter*67)), 50, 50)))

#draws intro screen background when called
def introBg(BLACK, WHITE, GRAY, introscreen): 
    introscreen = pygame.display.set_mode(SIZE2)     
    pygame.draw.rect(introscreen, BLACK, (0, 0, 800, 240)) 
    wordleFont = pygame.font.SysFont("Helvetica", 45) 
    text_WORDLE = wordleFont.render("WORDLE", 1, WHITE)
    screen.blit(text_WORDLE, (305, 12, 10, 10))
    pygame.draw.line(introscreen, GRAY, (0, 51), (800, 51), 1)  
    
#draws game screen background when called   
def gameplayBg(screen, BLACK, width1, height1, GRAY, WHITE):
    pygame.draw.rect(screen, BLACK, (0, 0, width1, height1)) 
    
    #for loop draws wordle grids
    for vertical in range (78, 450, 67):
        
        for horizontal in range (36, 310, 67):
            pygame.draw.rect(screen, GRAY, (horizontal, vertical, 63, 63), 2)
            
    wordleFont = pygame.font.SysFont("Helvetica", 45)
    titleText = wordleFont.render("WORDLE", 1, WHITE)
    screen.blit(titleText, (105, 12, 100, 100))
    pygame.draw.line(screen, GRAY, (0, 51), (400, 51), 1)

def postGame(solved, BLACK, WHITE, GRAY, introscreen, bodyFont, wordList, secretWord): 
    replay = True
    introBg(BLACK, WHITE, GRAY, introscreen)

    while solved:
        textOutput(bodyFont, introscreen, WHITE, "Solved!", 0) 
        textOutput(bodyFont, introscreen, WHITE, "Would you like to play again?", 1)
        textOutput(bodyFont, introscreen, WHITE, "(Press the 'Y' key for Yes or 'N' key for No)", 2) 
                
        for evnt in pygame.event.get():
            
            if evnt.type == pygame.KEYDOWN:
                #Changes screens to the intro
                pygame.draw.rect(introscreen, BLACK, (0, 53, 800, 240))                  
                if (evnt.unicode).upper() == 'Y': #New round
                    replay = True
                    solved = False 
                    
                #Game over
                elif (evnt.unicode).upper() == 'N': 
                    textOutput(bodyFont, introscreen, WHITE, "Thanks for playing!!!", 1) 
                    myClock.tick(3)
                    replay = False
                    solved = False
                    
                #Error handling    
                else:
                    pygame.draw.rect(introscreen, BLACK, (0, 53, 800, 240)) 
                    textOutput(bodyFont, introscreen, WHITE, "Please only type the Y or N key.", 3)  
                        
    #returns boolean back into program              
    return(replay)

def GameOver(BLACK, WHITE, GRAY, introscreen, bodyFont): #Game over (pop out window)
    word = ""
    word += secretWord    
    introBg(BLACK, WHITE, GRAY, introscreen)
    textOutput(bodyFont, introscreen, WHITE, "GAME OVER: Oh no, you've used all your guesses :(" , 0)   
    textOutput(bodyFont, introscreen, WHITE, ("The correct answer is:"), .75)
    textOutput(bodyFont, introscreen, WHITE, (word), 1.5)   
    textOutput(bodyFont, introscreen, WHITE, "Thank you for playing!", 2.25)   
    textOutput(bodyFont, introscreen, WHITE, "Better luck next time!", 3)  
    
    pygame.display.flip()
    myClock.tick(3) 
    
    running = False
    return(running)


while intro: #Preface
    introBg(BLACK, WHITE, GRAY, introscreen)
    textOutput(bodyFont, introscreen, WHITE, "Wordle Clone developed by Swayam Parekh" , 1)   
    textOutput(bodyFont, introscreen, WHITE, "Press any key to begin the game.", 2)  
    
    for evnt in pygame.event.get():
        if evnt.type == pygame.QUIT:
            running = False
            intro = False
        
        #starts game when keydown is true   
        if evnt.type == pygame.KEYDOWN:
            intro = False
            running = True
            
    pygame.display.flip()
    myClock.tick(3)

if running: 
    screen = pygame.display.set_mode(SIZE)    
    gameplayBg(screen, BLACK, width1, height1, GRAY, WHITE)

#Main game loop
while running:
    for evnt in pygame.event.get():  
        if evnt.type == pygame.QUIT:
            running = False   
              
        if evnt.type == pygame.KEYDOWN:              
            key = (evnt.unicode).upper()
            pygame.draw.rect(screen, BLACK, (0, 490, width1, 60))
            
            #When enter key is pressed
            if evnt.unicode == "\r":
                
                #Checks if the user has guessListed a word in each row
                if attemptCounter <=5: 
                    
                    #Runs only if all 5 spaces have been filled before pressing the final enter
                    if letterCounter == 5:
                        
                        #Cross references the final word entered with the secret word
                        if guessChecker(attemptCounter, guessList, secretWord):
                            solved = True
                            #GGs screen
                            running = postGame(solved, BLACK, WHITE, GRAY, screen, bodyFont, wordList, secretWord)
                            #ends the game loop if the final word was false
                            
                            if not running:
                                break
                        
                        #If the game is still going, the textdisplay functions displays the user's guessList   
                        textDisplay(guessList, attemptCounter) 
                        #increases counter for each guessList
                        attemptCounter += 1  
                        
                        #Once the enter key is pressed, the pos of the letter changes and shifts down 67.
                        letterX = 55
                        letterY += 67
                        guessList = []
                        letterCounter = 0     
                        
                        if solved: 
                            pygame.draw.rect(screen, BLACK, (0, 53, 400, 220))
                            solved = False
                            screen = pygame.display.set_mode(SIZE)                        
                            gameplayBg(screen, BLACK, width1, height1, GRAY, WHITE)
                            letterY = 93
                            attemptCounter = 0 
                            
                            #avoids repeat words when replaying     
                            wordList.remove(secretWord) 
                            secretWord = random.choice(wordList)                        
                    
                    #error handling 
                    else:
                        lessLetters = bodyFont.render("Not enough letters",1,WHITE)
                        screen.blit(lessLetters, (115,510,100,100))                           
                        
                #ends loop when all attemps have been used and the word is incorrect       
                if attemptCounter == 6: 
                    GameOver(BLACK, WHITE, GRAY, introscreen, bodyFont)
                    break
                
            #blits letters on the grid    
            elif key.isalpha(): 
                if letterCounter <=4 :
                    text = letterFont.render(key, 1, WHITE) 
                    screen.blit(text, (letterX,letterY,100,100))
                    guessList += key 
                    letterX += 67
                    letterCounter += 1              
            
            #when backspace is pressed, the guessList is popped & wordDeleter function is called
            elif evnt.unicode == '\b':
                if letterCounter > 0 and letterCounter <= 5: 
                    letterCounter -= 1 
                    guessList.pop() 
                    wordDeleter(guessList, attemptCounter)
                    letterX -= 67   
                
            else:           
                if letterCounter <=4:
                    keyError = bodyFont.render("This key is not allowed",1, WHITE)
                    screen.blit(keyError, (100,510,100,100))                           

    pygame.display.flip()
    myClock.tick(60)   

pygame.draw.rect(screen, BLACK, (0, 53, width1, height1)) 
pygame.display.flip()
myClock.tick(3)        
 
pygame.quit()
