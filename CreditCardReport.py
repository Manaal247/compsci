#CreditCardReport.py
#Author: Manaal Shahid
#Date: 06/02/2025
#Course: ICS3U - Computer Science
#Programming Library: 
#read_data(filename) - Reads credit card data from file and stores in seperate arrays
#sort_data(...) - Sorts the data by expiry date in order of past to future
#write_expired_cards(...) - Writes expired or soon to be expired cards to an output file
#(main) - Calls function to create final expired cards report

def read_data(filename):
  #Reads data from file and returns lists of data
  #Create lists for each piece of data
  given_names = []
  surnames = []
  cc_types = []
  cc_number = []
  exp_months = []
  exp_years = []
  expiry_date = []
  
  #Open the file for reading
  with open(filename, 'r') as f:
    for line in f:
      #Remove any whitespace or newline characters
      line = line.strip()
      if not line:
        continue #Skip lines that do not have exactly 6 fields
      
      #Store data in the correct lists
      given_names.append(fields[0])
      surnames.append(fields[1])
      cc_types.append(fields[2])
      cc_numbers.append(fields[3])
      exp_months.append(fields[4])
      exp_years.append(fields[5])
      
      #Create an integer representing the expiry date for comparison
      expiry_date = int(fields[5]) * 100 + int(fields[4])
      expiry_dates.append(expiry_date)
      
  return given_names, surnames, cc_types, cc_numbers, exp_months, exp_years, expiry_dates

def sort_data(given_names, surnames, cc_types, cc_numbers, exp_months, exp_years, expiry_dates):
  #Sorts data by the expiry date using a simple exchange sort
  n = len(expiry_dates)
  for i in range(n - 1):
    for j in range(i + 1, n):
      if expiry_dates[j] < expiry_dates[i]:
        #Switches all corrosponding fields to keep the data aligned
        given_names[i], given_names[j] = given_names[j], given_names[i]
        surnames[i], surnames[j] = surnames[j], surnames[i]
        cc_types[i], cc_types[j] = cc_types[j], cc_types[i]
        cc_numbers[i], cc_numbers[j] = cc_numbers[j], cc_numbers[i]
        exp_months[i], exp_months[j] = exp_months[j], exp_months[i]
        exp_years[i], exp_year[j] = exp_years[j], exp_years[i]
        expiry_dates[i], expiry_dates[j] = expiry_dates[j], expiry_dates[i]
  
