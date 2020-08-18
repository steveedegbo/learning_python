# for i in 'banana':
#     print (i)

# while True:
#     print('I am running..!')

# word = 'banana'
# index = 0

# while index < 6:
#     index += 1
#     print(index)

# word = 'banana'
# index = 0

# while True:
#     print(word[index])
#     index += 1
    

#     if index == len(word):
#         break

# word = 'emancipation'
# for letter in word:
#     if letter == 'p':
#         print ('Yaay! found letter (p)\n')
#         break
#     else:
#         print('Searching for p', 'found', letter)

# else:
#     print('Sorry, P was not found in', word)


# sentence = "In this example, <iterable> is the list a, and <var> is the variable 1. each line through the loop, i takes on a successive item in a, so print() displays the values 'foo' =, 'be' "

# word_list = sentence.split(" ")
# place_holder = ""

# for word in word_list:

#     if len(word) > len(place_holder):
#             place_holder = word
# print(place_holder)


# index = 0
# while True:
#     if len(word_list[index]) > len(place_holder):
#         place_holder = word_list[index]

#     index +=1

#     if index == len(word_list):
#         break

    
# print(place_holder)

# number = 0
# stop_value = 200
# while True:
#     print(number)
#     number +=1

#     if number == stop_value +1:
#         break

#WITH A STEP VALUE

# step_value = 2
# number = 0
# stop_value = 200

# for i in range(1,201,1):
#     print(i)

#COUNTDOWN TIMER
# import time
# import winsound

# number_of_seconds = int(input('Enter time in seconds : '))
# for i in reversed(range(number_of_seconds)):
#     print(i)
#     time.sleep(1)

# winsound.Beep(100, 1000)

# import time
# import winsound
  
  #ASSIGNMENT COUNTDOWN TIMER HELP
# second = int(input('Please enter number of seconds : '))    
# minute = int(input('Please enter number of minutes : '))    
# hour = int(input('Please enter number of hours : '))    
# while(True):           
#     print('%d : %d : %d '%(hour,minute,second))      
#     time.sleep(1)    
#     second += 1    
#     if(second == 60):    
#         second = 0    
#         minute += 1    
#     if(minute == 60):    
#         minute = 0    
#         hour += 1 
# winsound.Beep(100, 1000)
# winsound.Beep(100, 1000)
# winsound.Beep(100, 1000)
#ASSIGNMENT

#MAKE COUNTDOWN TIMER SHOW IN MINUTES AND SECONDS, THREE BEEPS ALARM LIKE AT THE END 
#PICTURE

# import time
# import winsound

# number_of_minutes = int(input('Please enter time in minutes : '))
# number_of_seconds = int(input('Please enter time in seconds : '))
# while True:
#     if number_of_seconds == 0:
#       number_of_seconds = 60
#       number_of_minutes -= 1
#       if number_of_minutes < 1 :
#           break
#     print('%d : %d'%(number_of_minutes,number_of_seconds))
#     number_of_seconds -= 1
#     time.sleep(1)
# winsound.Beep(1000, 1000)
# winsound.Beep(1000, 1000)
# winsound.Beep(1000, 1000)


#SUM TO 555


# number = 0
# while True:
#     number +=1

#     if number == 555/3:
#         break
# print(number)


#ASSIGNMENT LECTURER SOLUTION

# import time
# import winsound
# number_of_mins = int(input('Please enter time in minutes : '))
# number_of_seconds = int(input('Please enter time in seconds : '))

# total_secs = (number_of_mins + 60) + number_of_seconds

# for i in reversed(range(total_secs)):
#   mins = i//60
#   secs = i%60
#   print(f"{mins} : {secs}")
#   time.sleep(1)
# for i in range(3):
#   time.sleep(0.5)

#   for j in range(4):
#     time.sleep(0.3)
#     winsound.Beep(1000,200)


#ASSIGNMENT 2 EXHAUSTIVE ENUMERATION

# for i in range(100, 999):
#   sum_nums = i * 3
#   last_nums = str(i)[2] * 3

#   if sum_nums == int(last_nums):

#     print(i, sum_nums, last_nums)
#     break





# file_name = 'loops/buhari.txt'
# file = open(file_name, "r", errors='ignore')
# data = file.read()

# lines = data.replace("-", " ").splitlines()
# buhari_place_holder = ""


# for line in lines:
#   words = line.split(" ")
#   for word in words:
#       if len(word) > len(buhari_place_holder):
#         buhari_place_holder = word
# print(buhari_place_holder)

# file_name = 'loops/obama.txt'
# file = open(file_name, "r", errors='ignore')
# data = file.read()

# lines = data.replace("-", " ").splitlines()
# obama_place_holder = ""

# for line in lines:
#   words = line.split(" ")
#   for word in words:
#       if len(word) > len(obama_place_holder):
#         obama_place_holder = word
  
# print(obama_place_holder)

# longestword_owner = "Buhari" if len(buhari_place_holder) > len(obama_place_holder) else "Obama"
# print(longestword_owner)

#STANDARD DEVIATION TO EXCEL
# file_name = "loops/num_file.csv"
# file = open(file_name, "w")

# numbers = [50, 10, 100, 99, 80, 80, 30]

# file.write(f"Scores, Passed\n")
# for number in numbers:
#   file.write(f"{number}, {number >50}\n")

#write statistics to excel file
# file_name = "loops/num_file.csv"
# file = open(file_name, "w")

# numbers = [50, 10, 100, 99, 80, 80, 30]
# numbers_deviation = []
# numbers_deviation_squared = []
# n = len(numbers)
# mean = sum(numbers)/n

# for number in numbers:

#   numbers_deviation.append(number - mean)
#   numbers_deviation_squared.append((number - mean)**2)

# file.write(f"Scores,X - XBar,X - XBar2\n")

# for number in numbers:
#   file.write(f"{number},{number-mean},{(number-mean)**2}\n")
# file.write(f" X - XBar\n")
# for number in numbers_deviation:
#   file.write(f"{number}\n")
# file.write(f"(X - XBar)Squared\n")
# for number in numbers_deviation_squared:
#   file.write(f"{number}\n")


#ASSIGNMENT
#https://w3resource.com/python-exercises/python-conditional-statements-and-loop-exercises.php, first 10

# for i in range(1500, 2701):
#   number_divisible_by_7 = i%7
#   number_multiple_of_5 = i%5
#   if not bool(number_divisible_by_7) and not bool(number_multiple_of_5):
#     print(i)



#  Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# Sample Output :
# fizzbuzz
# 1
# 2
# fizz
# 4
# buzz


# start = 1
# stop = 51
# while True:
#   start+=1
#   if not bool (start % 3):
#     print("Fizz")
#   elif not bool (start % 5):
#     print("Buzz")
#   elif not bool(start%3) and not bool(start%5):
#     print("FizzBuzz") 
#   else:
#     print(start)
#   if start == stop:
#     break

#TEMPERATURE CALCULATOR

# temperature = input("Do you want to calulate celcius or fahrenheit? (c/f) : ")

# if temperature == 'c':
#   celc_temp_input = float(input('Please enter the temperature : '))
#   fahr_temp_output = (celc_temp_input * (9/5)) + 32
#   print('Your fahrenheit temperature is', fahr_temp_output)
# elif temperature == 'f':
#   fahr_temp_input = float(input('Please enter the temperature : '))
#   celc_temp_output = (fahr_temp_input - 32) * (5/9)
#   print('Your celcius temperature is', celc_temp_output)


#FIBONACCI

# quantity = 15

# x = 1
# y = 1
# print(x)
# print(y)

# for i in range(quantity):
#   print(x + y)
  
#   x, y = y, x+y

