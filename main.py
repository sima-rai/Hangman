import random
import time


#Welcoming user
print("Welcome to Hangman game by Seema\n")

name=input("Please enter your name")
print("Hello" + name + "Good luck!!!")


time.sleep(2)
print("The game is about to begin\n")
time.sleep(3)



def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game

    words_to_guess = ["apple", "hurray", "thursday", "sanitizer", "milk", "chocolate", "school", "paper"]


    word=random.choice(words_to_guess)
    length=len(word)
    count=0
    display="_" * length
    already_guessed=[] #this would contain the string indices of correctly guessed word
    play_game=""



#A loop to rexecute the game when the first one ends:

def play_loop():
    global play_game
    play_game=input("Do you want to replay the game?  y=yes, n=no \n")
    while play_game not in ["y", "n", "Y", "N"]:
        play_game=input("Do you want to replay the game?  y=yes, n=no \n")
    if play_game=="y or Y":
        main()
    elif play_game=="n or N":
        print("Thanks for playing. Good day!!")
        exit()




# Initializing all the conditions required for the game:
def hangman():
    global count
    global display
    global word
    global already_guessed
    global play_game
    limit = 5
    guess=input("Guess the word: " + display + "Enter your guess: \n")
    guess=guess.strip() #?? I think yo just extra space haru hatauna lai strip gareko ho
    if len(guess.strip())==0 or len(guess.strip())>=2 or guess<="9":
        print("Invalid input. Try another \n")
        hangman()

    elif guess in word:#???????????????????????
        already_guessed.extend([guess])
        index=word.find(guess)
        word=word[:index]+ "_" + word[index+1:]
        display= display[:index] + guess + display[index+1:]
        print(display+ "\n")

    elif guess in already_guessed:
        print("Try another letter\n")

    else:
        count +=1

        if count==1:
            time.sleep(1)
            print("  ____\n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  "_|_\n")
            print("Wrong guess " + str(limit-count) + " guesses remaining\n" )

        elif count==2:
            time.sleep(1)
            print("  ____\n"
                  " |    |\n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  "_|_\n")
            print("Wrong guess " + str(limit-count) + " guesses remaining\n")


        elif count==3:
            time.sleep(1)
            print("  ____\n"
                  " |    |\n"
                  " |    |\n"
                  " |    \n"
                  " |    \n"
                  " |    \n"
                  "_|_\n")
            print("Wrong guess " + str(limit-count) + " guesses remaining\n")



        elif count==4:
            time.sleep(1)
            print("  ____\n"
                  " |    |\n"
                  " |    |\n"
                  " |    o\n"
                  " |    \n"
                  " |    \n"
                  "_|_\n")
            print("Wrong guess " + str(limit-count) + " guesses remaining\n")


        elif count==5:
            time.sleep(1)
            print("  ____\n"
                  " |    |\n"
                  " |    |\n"
                  " |    o\n"
                  " |   /|\  \n"
                  " |   /|\  \n"
                  "_|_\n")
            print("Wrong guess. You are hanged \n")
            print(" The correct word is: ",already_guessed,word)
            play_loop()

    if word=='_' * length: #????
        print("Congrats you have guessed the word correctly")
        play_loop()

    elif count != limit:
        hangman()


main()


hangman()