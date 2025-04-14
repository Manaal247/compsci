#Name: Manaal Shahid
#Revision date: 4/14/2025
#Program: Palindrome Assignment
#Description: A program to check if a word is a palindrome or not
#Programming Library:
  #S (String) = String to be checked if it is a palindrome
  #i (int) = index of the current character being checked
  #mid (int) = the index of the middle element in the string
  #ask (String) = user-input string to be checked
  #is_palin (boolean) = whether or not the string is a palindrome
  #do (String) = asks the user if they would like to enter another string to be checked

# Lines of code for the program to determine if a word is a palindrome or not 
def is_palindrome(S, i=0):  # Function to check if a string is a palindrome
    mid = len(S) // 2  # Calculate the middle index of the string
    if i >= mid:  # Base case: if index reaches or passes the middle, it's a palindrome
        return True
    if S[i] != S[-(i+1)]:  # If characters at index and the mirror don't match, it's not a palindrome
        return False
    return is_palindrome(S, i+1)  # Repetitive call to check the next pair of characters

print('Palindrome program!')

# Line of code that prompts user to enter their word their chosen amount of times and determine if it is a palindrome or not
do_another = True  # Variable to control the main loop
while do_another:  # Main loop to keep asking for words until user decides to stop
    ask = input("Please enter a word, and I will decide if it is a palindrome: ")
    is_palin = is_palindrome(ask)  # Check if the input word is a palindrome

    if is_palin:  # If the word is a palindrome
        print(f"{ask} is a palindrome!")
    else:  # If the word is not a palindrome
        print(f"{ask} is not a palindrome.")

    while True:  # Loop to ensure valid input ('y' or 'n') from the user
        do = input("Do another (y/n): ").lower()
        if do == 'y':  # If user inputs 'y', break the loop and continue with the main loop
            break
        elif do == 'n':  # If user inputs 'n', set do_another to False and break the loop to end program
            do_another = False
            break
        else:  # If input is invalid, prompt again
            print("Please enter 'y' or 'n'.")

print("Goodbye!")  # Program completion message
