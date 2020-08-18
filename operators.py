#LOGICAL OPERATORS
# is_worthy = True
# is_member = False
# is_manager = True

# can_enter_vault = is_member and is_worthy and is_manager
# can_enter_lounge = is_member and is_worthy or is_manager

# # print("Using AND : ", can_enter_vault)
# # print("Using OR : ", can_enter_lounge)

# print("User can enter vault : ", can_enter_vault)
# print("User can enter lounge : ", can_enter_lounge)

#MEMBERSHIP OPERATORS
# name = "abdulsalam"

# word_to_test = "abdul"
# test_word_is_in_name = word_to_test in name
# print(test_word_is_in_name)

# COMPARISON OPERATORS

# numeric = 20
# string = "20"

# print(numeric == string)



# EVEN NUMBER TESTER
# number_to_test = 20

# remainder_after_division_by_two = number_to_test % 2

# is_even = not bool(remainder_after_division_by_two)
# print(number_to_test, "is even : ", is_even)

# EVEN NUMBER TESTER FROM USER
# number_to_test = input("Please enter a number to test : ")

# number_to_test = int(number_to_test)

# remainder_after_division_by_two = number_to_test % 2

# is_even = not bool(remainder_after_division_by_two)
# print(number_to_test, "is even : ", is_even)

# is_odd = bool(remainder_after_division_by_two)
# print(number_to_test, "is odd : ", is_odd)


# SCORE ABOVE 60 IN MATH AND ABOVE 50 IN ENGLISH TO PASS

# math_score = input("Please input math score : ")

# math_score = int(math_score)

# is_pass_math = math_score >= 60

# english_score = input("Please input english score : ")

# english_score = int(english_score)

# is_pass_english = english_score >= 50

# print("Student passed math", "is", is_pass_math)
# print("Student passed english", "is", is_pass_english)

# fully_passed = is_pass_math and is_pass_english
# print("Student fully passed", "is", fully_passed)


# # SCORE COMPUTATION LECTURER SOLUTION

# math_score = 60
# english_score = 70

# math_threshold = 60
# english_threshold = 50

# passed_math = math_score >= math_threshold
# passed_english = english_score >= english_threshold

# print("student passed math : ", passed_math)
# print("student passed english : ", passed_english)

# passed_fully = passed_math and passed_english
# print(("student passed fully : ", passed_fully)


# DRINKING RESTRICTION

# age = 21
# sex = "male"

# # age = str(age)
# can_drink_by_age = age >= 21
# can_drink_by_sex = sex == 'male'

# can_drink = can_drink_by_age and can_drink_by_sex

# print("Eligibility for a drink : ", can_drink)

# DRINKING RESTRICTION INPUT

# age = input("Please enter your age : ")
# sex = input("Please enter your sex : ")
# age = int(age)

# can_drink_by_age = age >= 21
# can_drink_by_sex = sex == 'male'

# can_drink = can_drink_by_sex and can_drink_by_age

# print("Eligibility for a drink : ", can_drink)


# Quadratic Equation
# a = int(input("Please input a : "))
# b = int(input("Please input b : "))
# c = int(input("Please input c : "))
# q = (((b**2) - (4*a*c))**0.5)
# x1 = (-b + q)/(2*a) 
# x2 = (-b - q)/(2*a)

# print(x1,x2)


#MAP FUNCTION

# quantities_sold = [2,3,4,5,6,7]

# unit_price = 300

# amount_sold = map(lambda value: value * unit_price, quantities_sold)

# print(list(amount_sold))

# names = ["adan", "sean", "ade", "kunle"]

# saluted_names = map(lambda name: "Mr, "+ name, names)

# print(list(saluted_names))

# names = ["adan", "sean", "ade", "kunle"]

# gender = ["m", "f", "m", "f"]

# saluted_names = map(lambda person: "Mr, " + person[0] if person[1] == "m" else "Mrs,"+ person[0] , zip(names, gender))

# print(list(saluted_names))

# PROGRAM TO GREET A USER

# name = input("Please enter your name : ").replace("e", "o")
# print("Hello", name)

# data = input("Please enter your name and age seperated by comma : ")
# splitted_name_age = data.split(",")
# name = splitted_name_age[0]
# age = splitted_name_age[1]

# print(splitted_name_age)
# print(name)
# print(age)

# WRITE PROGRAM TO TELL USERS THEY WERE BORN IN A LEAP YEAR, TAKES IN AGE AND TELLS YOU

# age = int(input("Please state your age : "))
# current_year = 2020
# yob = current_year - age
# leap_year = yob % 4
# print("You were born in a leap year is ", not bool (leap_year))


# WRITE A PROGRAM TO TEST IF ONE WORD IS AN ANAGRAM OF ANOTHER WORD

# word_one = input("Please input your first word : ")
# word_two = input("Please input your second word : ")

# anagram = sorted(word_one) == sorted(word_two)
# print("Word one is an anagram of Word two is", anagram)

# ASSIGNMENT - USE ALL STRING METHODS

# name = input("Please enter your name : ").replace("e", "o")
# print("Hello", name)

# data = input("Please enter your name and age seperated by comma : ")
# splitted_name_age = data.split(",")
# name = splitted_name_age[0]
# age = splitted_name_age[1]

# print(splitted_name_age)
# print(name)
# print(age)

#JOIN STRINGS

# names = ("Stephen", "Edegbo", "Ojobojo")
# joined_name = " ".join(names) 

# print(joined_name)


# names = input("Please enter your names separated by a comma : ")
# joined_name = "".join(names)
# print(joined_name)
# print(names)


#SWAPCASE
# name = "emmanuel"
# newname = name.swapcase()
# print(newname)

#STARTSWITH

# text = input("Please define your preferred software stack : ")
# print(text.startswith('Python'))

#LOWER

# statement = input("Please write your statement : ")

# lower_statement = statement.lower()
# print(lower_statement)


#ENDSWITH
# statement = input("Please enter your statement : ")
# print(statement.endswith('awesome'))


#FIND
# motto = input("Please enter your motto : ")
# if (motto.find('vision') !=-1):
#     print("contains substring 'vision'")
# else:
#     print("does not contain substring vision")
   
#COUNT
# baygon = "Is a very powerful insecticide"
# number = baygon.count('insecticide')
# print(number)

