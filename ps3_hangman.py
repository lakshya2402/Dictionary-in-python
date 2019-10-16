
import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
   
    #Returns a list of valid words. Words are strings of lowercase letters.
    
    #Depending on the size of the word list, this function may take a while to finish.
   
    print ("\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print ("\t#                  Hangman game 		                     #")
    print ("\t#                       By 		                     #")
    print ("\t#                  Lakshya Yadav 		                     #")
    print ("\txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print("Loading word list from file...")
    # inFile: file
    inFile = open('/root/Desktop/words.txt', 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
   
    #wordlist (list): list of words (strings)

    #Returns a word from wordlist at random
  
    wordlist = loadWords()
    return random.choice(wordlist)

def isWordGuessed(secretWord, lettersGuessed):
    
    #secretWord: string, the word the user is guessing
    #lettersGuessed: list, what letters have been guessed so far
    #returns: boolean, True if all the letters of secretWord are in lettersGuessed; False otherwise
    
    a=[]
    
    c=()
    for i in secretWord:
       if i not in a:
              a+=[i, ]  
    for j in lettersGuessed:
       if j not in c and j in a:
            c+=(j, )
    if len(c)==len(a):
        return True
    else:
        return False    
def getGuessedWord(secretWord, lettersGuessed):
    
       #secretWord: string, the word the user is guessing
       #lettersGuessed: list, what letters have been guessed so far
       #returns: string, comprised of letters and underscores that represents what letters in secretWord have been guessed so far.
    
    a=[]
    result=[]
    for i in secretWord:
        a+=[i, ]    
    for j in range(len(a)):
             
             p=a[j]
             if p in lettersGuessed:
                 
                 result.append(p)
             else:
                 result.append("_")
    str1 = ''.join(result)             

    return str1    
def getAvailableLetters(lettersGuessed):
    
    # lettersGuessed: list, what letters have been guessed so far
    # returns: string, comprised of letters that represents what letters have not yet been guessed.
  
    import string
    a=[]
    result=[]
    for i in string.ascii_lowercase:
        a+=[i, ]
    
    for j in range(len(a)):
             
             p=a[j]
             if p not in lettersGuessed:
                 result.append(p)
    str1 = ''.join(result)             

    return str1
    

def hangman(secretWord):
    
    # The main program for call
    
    print("Welcome to the game, Hangman!")
    print('I am thinking of a word that is ',len(secretWord),' letters long' )    
    lettersGuessed=[]
    number=8
    

    while number>0:
          print('------------')
          print("You have ", number ," guesses left")
          print("Available Letters: ",getAvailableLetters(lettersGuessed))
          Guessed= str(input('Please guess a letter: ')).lower()
          
          
          if Guessed not in lettersGuessed:
              lettersGuessed.append(Guessed)
              if Guessed in secretWord :
                  print("Good guess: ",getGuessedWord(secretWord, lettersGuessed))
                  
              elif Guessed not in secretWord :
                  number-=1  
                  print("Oops! That letter is not in my word: ",getGuessedWord(secretWord, lettersGuessed))
                  
          elif Guessed in lettersGuessed:
                  print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
                                       
          if True== isWordGuessed(secretWord, lettersGuessed):
             print('------------') 
             return print("Congratulations, you won!")
          
    if number==0:

            print('------------')
            
            return print('Sorry, you ran out of guesses. The word was', secretWord)
            
wordlist = loadWords()
secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))
