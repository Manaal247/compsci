#Manaal Shahid
#1060580
#ICS3U
#secret_number - the random number
#max_attempts - the max number of tries
#attempts - the number of guesses user has done
#guess - the guess the user is currently on
import random #import random module
secret_number = random.randint(1,100) #Pick a random number
max_attempts = 6 #Maximum number of attempt
print ("Hello! Welcome to the guessing game!")
print ("I am thinking of a number between 1 and 100. It is your turn to guess what it is. You have a maximum of six (6) tries.")
#Loop through multiple attempts
for attempts in range(1, max_attempts + 1):
  guess = int(input(f"Guess #{attempts}: "))
  if guess < secret_number:
    print ("Higher!")
  elif guess > secret_number:
    print("Lower!")
  else:
    print("You guessed correct!") #The user has put in the correct guess
#If user does not guess correctly/runs out of number of tries
if guess != secret_number:
  print(f"Out of tries! The number was, {secret_number}")
