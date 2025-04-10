#Intro: This program is based on a game show that prompts a user to guess with limited tries
#Name: Manaal Shahid
#Stundent ID: 1060580
#Course Code: ICS3U
#Programming Library
#secret_number = the random number
#max_attempts = the max number of tries
#attempts = the number of guesses user has done
#guess = the guess the user is currently on

#Import Random Module
import random 

#Pick a random number
secret_number = random.randint(1,100)

#Maximum number of attempt
max_attempts = 6 
attempts = 0

#Print Statements to inform user what to do in the game
print ("Hello! Welcome to the guessing game!")
print ("I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.")

#Loop until player guesses correct ir runs out of tries
while attempts < max_attempts:
  guess = int(input("Enter your guess: "))
  attempts += 1
  
  if guess == secret_number:
   print(f"You guessed correct! The number was {secret_number}. You got it in {attempts} tries.")
  elif guess < secret_number:
    print("Higher!")
  else:
    print("Lower!")
    
#If the loop finishes and the correct guess is not given;
if guess != secret_number:
  print("Out of tries! The number was {secret_number}.")
