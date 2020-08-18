# x = 1
# y = 5
# # if x<y:
# #     print('Yes')

# if x:
#     print('Yes')

# LOGIN 

# password = '123qwert'
# username = 'owambe21'

# input_username = input('Please enter username : ')
# input_password = input('Please enter password : ')

# if input_username == username:
#     print('Weldone, your username exists')
#     print('Checking password, hold on')
#     print()

# if input_password == password:
#     print('Congrats you are signed in')

# elif input("Recover password ? (y/n): ") == 'y':
#     print('Your password is', password)

# elif input("Recover username ? (y/n): ") == 'y':
#     print('Your username is', username)


# LARGER NUMBER
# a = int(input('Please enter first number : '))
# b = int(input('Please enter second number : '))

# if a>b:
#     print('A is the larger number')
# else:
#     print('B is the larger number')

# CLASS WORK PASS OR FAIL
# score = int(input("Please enter your score : "))
# grade = 'Passed' if score >= 50 else 'Failed'

# print(grade)
# salutation
# gender = 'male'
# offering = 'gift'
# # txt = 'Hello there Mr/Mrs Adelabi, thank you for the gift/food you gave, it was so nice or sweet, I enjoy/ enjoyed eating/using it '

# txt = f"Hello there {'Mr' if gender == 'male' else 'Mrs'} Adelabi, thank you for the {offering} you gave it was so {'nice' if offering == 'gift' else 'sweet'}. I {'enjoy' if offering == 'gift' else 'enjoyed'} {'using' if offering == 'gift' else 'eating'} it."

# print(txt)


# CLASSWORK
# text = "Hello (Mr) (Adams), we realized that you recently signed up for our weight loss program, we see that you are (130kgs) and (5ft) tall which gives you a BMI of (23) and by standards is (good) hence we recommend the (sustainance) package for you today, Buy now at (200)naira "

# gender = 'female'
# full_name = 'Adunni Olori'
# weight = 85
# height = 1.6
# BMI = (weight)/(height**2)
# text = f"Hello {'Mr' if gender == 'male' else 'Mrs'} {full_name}, we realized that you recently signed up for our weight loss program, we see that you are {weight} kgs and {height} ft tall which gives you a BMI of {BMI} and by standards is {'good' if BMI <= 25 else 'bad'} hence we recommend the {'sustainance package' if BMI <=25 else 'weight loss package'} for you today, Buy now at {'200 Naira' if BMI<=25 else '1000 Naira'} only."
# print(text)

# ASSIGNMENT

# if character variable taxCode is ’T’, increase price by adding the taxRate per-
# centage of price to it.

# price = int(input('Please enter price : '))
# taxcode = input('Please enter your taxcode : ')
# if taxcode == 'a':
#     print('Your total price is', price*1.1)
# elif taxcode == 'b':
#     print('Your total price is', price*1.15)
# elif taxcode == 'c':
#     print('Your total price is', price*1.2)

# # If integer variable opCode has the value 1, read in double values for X and Y and
# # calculate and print their sum.

# x = 100
# y = 20
# opcode = 1
# if opcode == 1:
#     print(x+y)

# # If integer variable currentNumber is odd, change its value so that it is now 3
# # times currentNumber plus 1, otherwise change its value so that it is now half of
# # currentNumber (rounded down when currentNumber is odd).

# currentnumber = int(input('Please enter number : '))
# odd_no_check = currentnumber%2
# if bool(odd_no_check):
#     print((currentnumber*3) + 1)
# else:
#     print(currentnumber*0.5)

# # Assign true to the boolean variable leapYear if the integer variable year is a
# # leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must
# # also be a multiple of 400.)

# yob = int(input('Please enter your year of birth : '))
# leap_year = yob%4

# if not bool (leap_year):
#     yob = 'true'
#     print(yob)
# else:
#     yob = 'false'
#     print(yob)



# # Assign a value to double variable cost depending on the value of integer variable
# # distance as follows:
# # Distance Cost
# # 0 through 100 5.00
# # More than 100 but not more than 500 8.00
# # More than 500 but less than 1,000 10.00
# # 1,000 or more 12.00

# distance = int(input('Please input the distance : '))
# if distance <= 100:
#     print('Cost is 5.00')
# elif distance <= 500 > 100 :
#     print('Cost is 8.00')
# elif distance < 1000 > 500 :
#     print('Cost is 10.00')
# elif distance > 1000:
#     print('Cost is 12.00')

#CHECK UP
name = input("Please enter your name : ")
q1 = input("Feeling good? >y/n : ")
if q1 == 'y':
    print("Bye")
else:
    q2 = input("Do you have a headache? >y/n : ")
    if q2 == 'n':
        print('Drink water and mind your business')
    else:
        q3 = input('Stressed lately? >y/n : ')
        if q3 == 'y':
            print('Have some rest')
        else:
            q4 = input('Do you have fever? >y/n : ')
            if q4 == 'y':
                print('Call NCDC')
            else:
                print('Sorry cant help now')



# LOGIN 

# password = '123qwert'
# username = 'owambe21'

# input_username = input('Please enter username : ')
# input_password = input('Please enter password : ')

# if input_username == username:
#     print('Weldone, your username exists')
#     print('Checking password, hold on')
#     print()

# if input_password == password:
#     print('Congrats you are signed in')

# elif input("Recover password ? (y/n): ") == 'y':
#     print('Your password is', password)

# elif input("Recover username ? (y/n): ") == 'y':
#     print('Your username is', username)



#CHECKUP 2
name = input("Please enter your name : ")

if input("Feeling good? (y/n) : ") == 'y':
    print("Bye")
elif input("Do you have a headache? (y/n) : ") == 'n':
    print('Drink water and mind your business')
elif input('Stressed lately? (y/n) : ') == 'y':
    print('Have some rest')
elif input('Do you have fever? (y/n) : ') == 'y':        
    print('Call NCDC')
else:
    print('Sorry cant help now')