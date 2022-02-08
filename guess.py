import random
import sys
import time


def exit_game():
    print("\nThank you! see you next time.\n")
    sys.exit()

print("\nYou need a password before if you want to play the game. ")
print("your password is in 8 digit.\n")
time.sleep(1)

try1 = 0 

while True:
    s  = input("Please enter the password:  ")
    if  s == 'shivhare':
        print("\n Welcome! sir.")
        break
    elif s == 'exit':
        exit_game()
    else: 
        try1 +=1

        if try1  :
            print("\nSorry! the password you entered is wrong. try again.\n")
            time.sleep(0.5)
            print("You have ", 3-try1, " more chance left you have to try...\n")
            continue
        elif try1  == 3:
            time.sleep(1)
            print("cheaters not allowed\n")
            sys.exit()

time.sleep(1)


name = input("Please enter your name:  ")

while name == '':
    name = input("Please enter your name:  ")

time.sleep(0.5)

if  name == 'exit':
    exit_game()

print(f"\n ********** {name},  let's  play the game. all the very best for the game. **********\n ")


def instructions():
    print("\n**********instructions************")
    time.sleep(1)

    print("\n*\t this is a hangman a fun game.")
    time.sleep(1)

    print('''*\t an innocent person has been caught and you 
         know that. you want to free him off.''')
    time.sleep(1)

    print("*\t your statement is recorded to used for evidence to proove.\n")
    time.sleep(1)

    while True:
        start1 = input(" Press enter to continue\n")
        if start1 == 'exit':
          exit_game()

        elif start1 not in'':
         print('Invalid input')
         continue

        else:
         break

    print("#\t at start you will be given the number of letters in your word.")
    time.sleep(1)

    print("#\t you have to guess the word letter by letter.")
    time.sleep(1)

    print("#\t a correct letter would be inserted in your word.")
    time.sleep(1)

    print("#\t a wrong letter would be increases your guesses. ")
    time.sleep(1)

    print("#\t once the guess counter becomes zero. you loose the game.")
    time.sleep(1)

    print("#\t try to find a word minimum guess counter.\n")
    time.sleep(1)


    while True:
        start2 = input('''**** if you are ready.\npress enter to continue''')

        if start2 =='exit':
            exit_game()

        elif start2 not in '':
          print('invalid input \n ')
          continue

        if start2 in '':
         break

time.sleep(1)

while True: 
    know_the_game = input("do you  know how to play? -  ").lower()

    if know_the_game == 'exit':
        exit_game()

    elif know_the_game not in ('yes', 'y', 'no', 'n'):
        print('invalid input')
        continue

    if know_the_game in ( 'no','n'):
        instructions()
    break

time.sleep(0.5)


print('''\n Great! let's start \n ''')

time.sleep(1)

print("********** a code copy by ankur shivhare **********")
time.sleep(0.5)

print("          -------------------------------      \n")
print()
time.sleep(1)

ascii_letters = 'abcdefghijklmnopqrstuvwxyz'

players = ['rohan','dhoni', 'kohli', 'sharma', 'rahul', 'shami', 'ishant',
        'sunil', 'kapil', 'sachin', 'dravid', 'lee', 'plesis', 'nehra', 'kumble', 
        'jadeja', 'rishabh']

games = ['cricket', 'bedminton','chess', 'ludo', 'football', 'swimming',
          'karate', 'shooting', 'merathon', 'jevelin', 'kabaddi', 'hockey']

words = players + games

while True:
    word = random.choice(words)

    print("\t you have 3 clue for guessing the word.\n")
    print(f"1.  your word has {len(word)} character.")
    time.sleep(1)
    

    if word in players:
        print("2.  your word is  a player.")

    elif word in games:
        print('2.  your word is in games.')
        time.sleep(3)

    turns = 11 - len(word)
    if len(word) >= 8:
        turns = 4

    print(f"3.  you have a only ({turns}) turns to choose your words.\n")
    time.sleep(1.2)

    turns -= 1

    while True:
        start = input("\n press enter to start guessing...")

        if start == 'exit':
         exit_game()

        elif start not in '':
            print('\ninvalid input')
            continue

        else:
            break
     
    guesses = ''
    while turns > 0:
        failed = 0

        guess = input("\n guess a character: ").lower()
        if guess == 'exit':
          exit_game()

        if guess in '':
          print("\n please enter a valid character.\n")
          continue

        else:
           guess = guess

        if guess in guesses:
            
            print(f"\n you have already guessed this character.please try with other character {turns-1}\n")
           
            continue

        guesses += guess

        for char in word:
            if char in guesses:
               print(char,"", end="")

            else:
               print("-", end="")
            failed += 1
        if failed == 0 and len(word) == guesses:
            print("congratulation! you won.")
        elif len(char) == guesses:
            print("y")
            
            time.sleep(1)
            
            
            print(f"\n the word was {word} \n")
            time.sleep(0.5)

            print("\n an innocent has been saved.\n")
            break

        if guess in word:
            print(f"Excellent! {guess} is in the word.")

        if guess not in word:
            if guess not in ascii_letters:
                print("\n Please enter a valid character\n")

            else:
                print(f"\n wrong! It seems  that {guess} is not in the word \n")
                turns -=1

            if turns != 0:
                print(f"\n You have {turns}  more to guess the word\n")

            elif turns == 0:
                print(f"\nYou have no more {turns} to guess  the word.\n")
                time.sleep(0.5)

                print("you loose! you had not guessed the right word.\nDon't mind! Better luck next time.")
                time.sleep(1)

                print("\n")

            
                with open('another.txt', 'w') as f:
                     a = f.write('name- ')
                     a = f.write(name)
                     a = f.write('\npassword attempt- ')
                     a = f.write(str(try1+1))
                     a = f.write('\nturns left- ')
                     a = f.write (str(turns))
                     a = f.write('\nFailed- ')
                     a = f.write(str(failed))
                     a = f.write('\nword- ')
                     a = f.write(word)
                     time.sleep(2)
                   

    while True:
        play_again = input("\tDo you want to play again ? \t").lower()

        if play_again in ('y', 'n','yes','no'):
            break
        print("\n invalid input")

        if play_again in ('y', 'yes'):
           
            time.sleep(1)
            continue

        else:
            time.sleep(0.2)
            print()
            break

    
    
    time.sleep(5)
