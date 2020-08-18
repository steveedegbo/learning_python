# # # # # #TAKES NAME & GENDER INPUT AND GREETS ACCORDINGLY 
# # # # # def greet(name, gender, age):

# # # # #     if gender == "male" and age >= 18:

# # # # #         print(f'Hello Mr {name}..!')
    
# # # # #     elif gender == "male" and age < 18:

# # # # #         print(f'Hello Mst {name}..!')

# # # # #     elif gender == "female" and age >= 18:
        
# # # # #         print(f'Hello Mrs {name}..!')
    
# # # # #     else:

# # # # #         print(f'Hello Ms {name}..!')
# # # # # # greet("Ade", "female")

# # # # # people = [("bolu", "male", 23), ("ade", "female", 15), ("sholu", "female", 45), ("manny", "male", 33)]

# # # # # for name,gender,age in people:
# # # # #     greet(name,gender,age) 

# # # # # for name,gender in people:
# # # # #     greet(name,gender)


# # # # #DEFINING YOUR OWN PYTHOIN FUNCTION REAL PYTHON READ UP
# # # # #HANGMAN WITH FUNCTIONS IN IT




# # # # name = input("Please enter your name : ")
# # # # print(f"Hi {name}, welcome to Hangman")

# # # # turns = 5

# # # # word = "stephen"

# # # # word_guess = ""

# # # # while turns > 0:

# # # #     failed = 0

# # # #     for char in word:

# # # #         if char in word_guess:

# # # #             print(char)

# # # #         else:
            
# # # #             print("_")

# # # #             failed += 1

# # # #     if failed == 0:

# # # #         print("You guessed right!")

# # # #         break

    
# # # #     guess = input("Please enter your guess : ")

# # # #     word_guess += guess

# # # #     if guess not in word:

# # # #         turns -= 1

# # # #         print("You have", turns, "more guesses")

# # # #         if turns == 0:

# # # #             print("You lost")





# # # # def say_hello(name):

# # # #     """THIS FUNCTION IS NICE and this is a docstring"""
# # # #     print(f"Hello {name}")

# # # # say_hello('bola')



# # # # def sqrt(number1,number2,power):

# # # #     answer = (number1 ** 2 + number2 ** 2) ** (1/power)

# # # #     print(answer)

# # # # sqrt(3,4,2)




# # # def sqrt(number):

# # #     answer = number ** (1/2)

# # #     return answer


# # # def square(number):

# # #     answer2 = number ** 2

# # #     return answer2


# # # sdf = sqrt(square(5) + square(7))

# # # print(sdf)


# # import datetime

# # # time_now = datetime.datetime.now()

# # # # print(time_now)
# # # # print(time_now.weekday()) #GIVES WEEKDAY IN NUMERALS

# # # print(time_now.strfttime("%a:%H:%M")) #GIVES A FORMATTED STRING REPRESENTATION OF TIME


# # # time_stamp = (time_now.strfttime("%a %H:%M"))

# # def get_timestamp():

# #     time_now = datetime.datetime.now()

# #     time_stamp = time_now.strftime("%b %d %Y %a %H %M.")

# #     print(time_stamp)

# #     return time_stamp

# # def number_words(text):

# #     count = len(text)

# #     print(count)

# #     return count

# # def store_memory(memory, time_stamp, count):

# #     file = open(f"functions/{time_stamp},{count}.txt", "w")

# #     file.write(memory)

# #     file.close()

# #     return True


# # text = input("Please enter text : ")

# # time_stamp = get_timestamp()

# # count = number_words(text)

# # store_memory(text, time_stamp, count)

# # #OPEN NEW FILE AND WRITE TO IT
# # # file = open("functions/note.txt", "w")

# # # text = input("Please enter text : ")

# # # file.write(text)


# # * is a tuple unpacker * variable positional argument
# ## ** is a dictionary unpacker *variable keyworrd argument

# # def sum_nums(*args):

# #     print(args)

# # sum_nums(2,32,3,4,7,8,9,0,4,5)


# def sum_nums(**kwargs):
#     print(kwargs)

# sum_nums(x=2,y=3,z=4,q=6,h=23)


#LAMBDA FUNCTION
# numbers = list("12345678")


# mini2 = lambda x: "A" + str(x)

# mapped_result2 = map(mini2, numbers)
# print(list(mapped_result2))


#RECURSION

# def factorial(n):
#     if n <= 1:
#         return n
#     else:
#         val = n + factorial(n-1)
#         print(val)
#         return val

# factorial(3)


# def count_down(num):
#     if num == 0:
#         return num
#     print(num)

#     return count_down(num-1)

# count_down(10)



# previous_number = 0
# numbers = 20,60,90,103,109,120

# for i in numbers:
#     print(i - previous_number)
#     previous_number = i

#with recursion
# previous_number = 0

# numbers = [20,60,90,103,109,120]

# def moving_difference(vals):

#     if len(vals) == 1:
#         return 0
#     else:
#         previous = vals.pop(0)
#         print(vals[0] - previous)
#         return moving_difference(vals)

# moving_difference(numbers)