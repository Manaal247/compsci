#Author: Manaal Shahid
#Revison date : 5/15/2024
#Program: Wordle
#Description: A program that searches for a wordle date or wordle word in the wordle database
#Programming library:
    #dates (list) = list of the wordle dates
    #words (list) = list of the wordle words
    #order (int) = the month in order of the time it occurs
    #months (list) = list of the months
    #date (string) = string format of the date YYYYMMDD
    #line (string) = line of the file
    #p (string) = the day in string format
    #q (string) = the month in string format
    #r (string) = the year in string format
    #file (object) = the file object to open the file
    #word (string) = the entered word
    #found_date (string) = the found date of the entered word
    #date (string) = the entered string
    #found_word (string) = the found word of the entered date
    #min_date (int) = the minimum of the found wordle
    #max_date (int) = the maximum of the found word in the wordle
    #d_or_w (string) = asking the user if they find a word or a date


dates = []
words = []

def merge(p, q, r):
    order = 0
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    for i in range(len(months)):
        if months[i].lower() == q.lower():
            order = i + 1

    order = f"{order:02d}"
    p = f"{int(p):02d}"
    date = f"{r}{order}{p}"
    return int(date)

def scanfile():
    try:
        file = open('wordle.dat', 'r')
        while True:
            line = file.readline()
            if not line:
                break
            (month, day, year, word) = line.split()
            date = merge(day, month, year)
            dates.append(date)
            words.append(word)
        file.close()
    except FileNotFoundError:
        print("File Error: File Not Found")

def search_by_word(word):
    for i in range(len(words)):
        if words[i].lower() == word.lower():
            found_date = dates[i]
            return word, found_date
    return word, None

def search_by_date(date):
    for i in range(len(dates)):
        if dates[i] == date:
            found_word = words[i]
            return date, found_word
    return date, None

scanfile()
min_date = int(merge("19", "Jun", "2021"))
max_date = int(merge("21", "Apr", "2024"))

print("Welcome to the Wordle Database!")
d_or_w = input("Enter w if you are looking for a word, or d for a word on a certain date: ")

if d_or_w.lower() == 'd':
    try:
        year = input("Enter the year: ")
        month = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        day = input("Enter the day: ")

        date = merge(day, month, year)

        if int(date) < min_date:
            print(f"{date} is too early. No wordles occurred before {min_date}. Enter a later date.")
        elif int(date) > max_date:
            print(f"{date} is too recent. Our records only go as late as {max_date}. Please enter an earlier date.")
        else:
            date, word = search_by_date(date)
            if word:
                print(f"The word entered on {date} was {word}.")
            else:
                print(f"No word found for the date {date}.")
    except ValueError:
        print("Please Enter Valid Input")
elif d_or_w.lower() == 'w':
    word = input("What word are you looking for? ")
    word, date = search_by_word(word)
    if date:
        print(f"The word {word.upper()} was the solution to the puzzle on {date}.")
    else:
        print(f"{word.upper()} was not found in the database.")
else:
    print("Please Enter Valid Input")
