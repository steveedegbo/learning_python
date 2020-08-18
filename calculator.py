# #print(1+2+3)

# WRITING VALUES DIRECTLY INTO VARIABLES
# first_num=1
# second_num=2
# third_num=3

# print(first_num+second_num+third_num)

# COLLECTING VALUES FROM USER INPUT INTO
#  VARIABLES
# first_num = input("Please enter the first number : ")
# second_num = input("Please enter the second number : ")
# third_num = input("Please enter the third number : ")

# first_num, second_num, third_num = int(first_num), int(second_num), int(third_num)
# print(first_num+second_num+third_num)

# SIMPLE INTEREST

# principal = input("Please enter the principal : ")
# rate = input("Please enter the rate : ")
# time = input("Please enter the time : ")

# principal, rate, time = int(principal), float(rate), int(time)

# print((principal * rate * time)/100)




#KMH TO MPH CONVERTER
# mph = 0.6214
# kmh = input("Kilometre per Hour : ")
# kmh = int(kmh)
# print("Mph", "=", mph * kmh)

#PYTHAGORAS CALCULATOR

# from math import sqrt
# formula = input('which side (a, b, c) do you wish to calculate? side> ')

# if formula == 'c':
#     side_a = int(input('Input the length of side a : '))
#     side_b = int(input('Input the length of side b : '))

#     side_c = sqrt((side_a ** 2) + (side_b**2))
#     print(side_c)


text = input("Please enter your numbers sepearted by a comma")
text_list = text.split(",")
print(text_list)


