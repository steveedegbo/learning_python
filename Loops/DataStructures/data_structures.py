# # numbers = [1,0,0,2]
# # print(numbers[::-1])


# q = [1,2,3,4,5,6,7,8,9,10]
# print(q[4:8:])

#LISTS

# student_scores = [
#     ["atha", [
#         ["m", "30"],
#         ["e", "30"]
#     ],
#         [["Football", "30%"],["Movies", "70%"]]
#     ],
#     ["bolu", [
#         ["m", "30"],
#         ["e", "30"]
#     ],
#         [["Swimming", "70%"],["Baseball", "30%"]]
#     ],
#     ["seun", [
#         ["m", "30"],
#         ["e", "30"]
#     ],
#         [["Reading", "40%"],["Running", "60%"]]]
# ]
# for target_student in student_scores:

#     name = target_student[0]
#     print("Name : " , name)

#     math_score = target_student[1][0][1]
#     print("Math Score : ", math_score)

#     english_score = target_student[1][1][1]
#     print("English Score : ", english_score)

#     hobbies = target_student[2]

#     hobby1_is_greater = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1])
#     favourite_hobby = hobbies[0][0] if hobby1_is_greater == True else  hobbies[1][0]
#     print("Favourite hobby is : ", favourite_hobby)

#     print()
#     print("--------------------")
#     print("--------------------")
#     print()


# target_student = student_scores[0]
# name = target_student[0]
# print("Name : " , name)

# math_score = target_student[1][0][1]
# print("Math Score : ", math_score)

# english_score = target_student[1][1][1]
# print("English Score : ", english_score)

# hobbies = target_student[2]

# hobby1_is_greater = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1])
# favourite_hobby = hobbies[0][0] if hobby1_is_greater == True else  hobbies[1][0]
# print("Favourite hobby is : ", favourite_hobby)

# atha_name = student_scores[0][0]
# print(atha_name)
# atha_math_score = student_scores[0][1][0][1]
# print(atha_math_score)
# atha_hobby = student_scores[0][2][1][0] #Atha, hobby, first hobby,value
# print(atha_hobby) 


# student_test = [["Atha",[["m","30"],["e","70"]],[["running","20%"],["gyming", "80%"]]],["Bolu",[["m","45"],["e","60"]],[["Movies", "60%"],["Reading","40"]]]]

# for target_student in student_test:

    
#     name = target_student[0]
#     print("Name is : ", name)

#     math_score = target_student[1][0][1]
#     print("Math Score is : ", math_score)

#     english_score = target_student[1][1][1]
#     print("English Score is : ",english_score)

#     hobbies = target_student[2]

#     hobby1_is_greater = int(hobbies[0][1][:-1]) > int(hobbies[1][1][:-1])
#     favourite_hobby = hobbies[0][0] if hobby1_is_greater == True else hobbies[1][0]
#     print("Favourite hobby is : ", favourite_hobby)

#     print()
#     print("----------------------------")
#     print("----------------------------")
#     print()

 

# bolu_name = student_test[1][0]
# print(bolu_name)
# bolu_english_score = student_test[1][1][1][1]
# print(bolu_english_score)
# bolu_hobby = student_test[1][2][0][0]
# print(bolu_hobby)




#DICTIONARIES

# dict_ = {'Name':'Stephen','Age':27,'Sex':'Male'}
# # print(dict_['Name']:,dict_['Name'])

# print ("dict['Name']: ", dict_['Name'] )
# print ("dict['Age']: ", dict_['Age'])

# dict_['Age'] = 20
# print(dict_)

# dict_['Subjects'] = ['Maths','English','TD']
# print(dict_)

# del dict_['Name']
# print(dict_)


# stephen_set = {'pineapple','grape','apple','grape','pineapple'}
# print(stephen_set)

# stephen_tuple = ('pineapple','grape','apple','grape','pineapple')
# print(stephen_tuple[3])

# def Summation(num1,num2):
#     """This function takes two numbers and returns their sum"""
#     summed = num1 + num2
#     return summed

# print(Summation(5,10))


# def factorial_iter(n):
#     num = 1
#     while n >= 1:
#         num = num*n
#         n = n-1
#     return num

# print(factorial_iter(n))

# n = int(input("Please enter n : "))

# def factorial_iter(n):
# #     num = 1
# #     while n >= 1:
# #         num = num * n
# #         n = n - 1
# #     return num  

        
# # print(factorial_iter(n))



# names = ['John','Paul','Sean']
# index = 0

# while True:
#     names[index] = "Mr " + names[index]

#     index+=1

#     if index == len(names):
#         break
# print(names)
   

# # names = ['John','Paul','Sean']
# # index = 0

# # for index in range(len(names)):
# #     names[index] = "Mr" + names[index]
# # print(names)


# question_1 = input('Do you want to enter a word (y/n) : ')
# question = input('Please enter a word : ')
# while True:
#     print(question)
#     if question_1 == 'n':
#         break



# list_of_values_entered = []
# while True:

#     value = input("Please enter a value : ")
#     list_of_values_entered.append(value)
#     print("You now have", len(list_of_values_entered),"values in your list")

#     stop_or_continue = input("Press y to continue entering values or n to stop : ")

#     if stop_or_continue == "n":
#         break

# total_characters = 0

# print("Value".center(10), "length".center(10))

# for value in list_of_values_entered:
#     length_of_value = len(value)
#     total_characters += length_of_value
#     print(value.center(10), str(length_of_value).center(10))

# print(f"\nValues in list : {len(list_of_values_entered)}. Total characters : {total_characters}.")

# total_characters = 0

# print("Value".center(10), "length".center(10), "Qty of As".center(10), "Qty of Bs".center(10), "Qty of Cs".center(10))

# for value in list_of_values_entered:
#     length_of_value = len(value)
#     total_characters += length_of_value
#     print(f"{value.center(10)}, {str(length_of_value).center(10)}, As : {value.count('a')}. Bs : {value.count('b')}. Cs : {value.count('c')}")

# print(f"\nValues in list : {len(list_of_values_entered)}. Total characters : {total_characters}.")

# word_list = []
# index = 0

# for char in "alphabet":
#     index+=1
#     word_list.append((index, char, char.upper()))

# print(word_list)


#EXTEND

# nums = [1,2,3,4,5,6,7]

# nums.insert(3,4)
# print(nums)

# number_of_sevens = nums.count(7)

# for i in range(number_of_sevens):
#     nums.remove(7)

# print(nums)



#ASSIGNMENT - Write a script that takes in text with dashes as missing values then takes in a list of values and numbers and fills each dash space with it


#FOR SOLUTION
# text = "This is the best _ of my _ i am so _ to be _ today. Who would have _ that you will not _ me"
# splittxt = text.split(" ")
# values = {1:"day", 2:"life", 3:"happy", 4:"here", 5:"thought", 6:"help"}
# index = 0
# val_index = 1

# for index in range(len(splittxt)):
#     if splittxt[index] == '_':
#         splittxt[index] = values[val_index]
#         val_index+=1
# print(splittxt)


#ASSIGNMENT LECTURER SOLUTION

# sentence = input("Please enter your sentence \nwith dashes denoting blank points :\n ")
# replacements = input("Please enter your replacements in order\n separated by commas :\n ")

# sentence_words = sentence.split(" ")
# print(sentence_words)

# replacement_words = replacements.split(",")
# print(replacement_words)

# replacement_index = 0

# for i in range(len(sentence_words)):

#     if sentence_words[i].find("_") != -1:

#         sentence_words[i] = sentence_words[i].replace("_", replacement_words[replacement_index])
#         replacement_index+=1
# full_sentence = " ".join(sentence_words)
# print(full_sentence)


#BUBBLE SORT IMPLEMENTATION

# def bubbleSort(ar):
#    n = len(ar)
#    # Traverse through all array elements
#    for i in range(n):
#    # Last i elements are already in correct position
#     for j in range(0, n-i-1):
#       # Swap if the element found is greater than the next element
#       if ar[j] > ar[j+1] :
#          ar[j], ar[j+1] = ar[j+1], ar[j]
# # Driver code to test above
# ar = ['t','u','t','o','r','i','a','l']
# bubbleSort(ar)
# print ("Sorted array is:")
# for i in range(len(ar)):
#    print (ar[i])




# prices = [200, 330, 400, 213, 32]
# markup = 1.5
# index = 0
# for i in range(len(prices)):
#     prices[index] = prices[index] * markup
#     index+=1
# print(prices)

#ASSIGNMENT CREATE HANGMAN GAME



#ZIP

# word = list("alphabet")
# numbers = list("12345678")

# zipped_vals = zip(word, numbers)

# print(next(zipped_vals))
# print(list(zipped_vals))


#MAP

# numbers = list("12345678")

# def mini(x):
#     return "A"+str(x)

# mapped_result = map(mini, numbers)
# print(list(mapped_result))


