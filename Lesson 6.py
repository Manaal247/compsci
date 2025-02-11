import math
birthyear = int(input("Please put your year of birth"))
age = int(input("Please put your age"))
step2 = (birthyear*2) + 5
step3 = ((step2*50)+age)
result = (step3 - 250) / 100
print ("The answer to this question is", result)
