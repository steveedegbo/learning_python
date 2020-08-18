# ##DECLARE FILENAME AND OPEN FILE FOR READING
# file_name = "functions/words.txt"
# file = open(file_name, "r")

# ## READ FILE
# data = file.read().split(',')


# ##IMPORT THE RANDOM MODULE FOR RANDOM VALUE SELECTIONS
# import random

# ## SELECT A RANDOM CHOICE FROM THE LIST OF WORDS READ FROM THE FILE
# selected_word = random.choice(data)

# guessed_character = []

# print("I have selected a word")

# ##CREATE A PLACE HOLDER TO HOLD SUCCESSFULLY GUESSED CHARACTERS
# guessed_chars_list = []

# ##DECLARE THE MAXIMUM NUMBER OF TURNS POSSIBLE
# turns = 5

# ##WHILE LOOP IS DECLARED WITH TURNS TO LIMIT NUMBER OF TURNS A USER HAS
# while turns:
    
# ## COLLECT GUESSED WORD FROM USER
#     guessed_char = input("Please guess a char : ")

# ##CHECK IF CHARACTER GUESSED BY USER IS IN WORD THAT HAS BEEN SELECTED BY THE COMPUTER

#     if guessed_char in selected_word:

#         ##IF CHAR IS GUESSED RIGHT, THEN ADD THE CHAR TO THE LIST OF SUCCESSFULLY GUESSED CHARS
#         guessed_chars_list.append(guessed_char)
#     else:
#         ## IF CHAR IS GUESSED WRONG, THEN REDUCE NUMBER OF TURNS
#         turns -= 1

#     for character in selected_word:

#         ## PRINT CHARACTER IF IT HAS BEEN GUESSED CORRECTLY

#         if character in guessed_chars_list:
#             print(character, end ="")

#         else:
#             ##PRINT DASH IF IT WAS GUESSED WRONG
#             print("_", end = "")

#     print()
#     ## PRINT NUMBER OF TURNS LEFT
#     print(f"You have {turns} tries left.!!!")

#     ## CHECK IF ALL CHARS OF THE SELECTED WORD HAVE BEEN GUESSED CORRECTLY AND IF SO END THE PROGRAM

#     if set(guessed_chars_list) == set(selected_word):
#         print('Congrats!!!')
#         break

    
import random

selected_word = ""
guessed_chars_list = []
def get_random_text():

    file_name = "functions/words.txt"
    file = open(file_name, "r")
    data = file.read().split(',')
    selected_word = random.choice(data) 

    return selected_word

def check_guess(guessed_char):
    global selected_word
    global guessed_chars_list

    if guessed_char in selected_word:
        guessed_chars_list.append(guessed_char)
        return True
    else:
        return False

def display():
    global selected_word
    global guessed_chars_list
    for character in selected_word:

        if character in guessed_chars_list:
            print(character, end ="")

        else:
            print("_", end = "")

    print()

def check_if_guess_complete():
    global guessed_chars_list
    global selected_word

    if set(guessed_chars_list) == set(selected_word):
        print('Congrats!!!')
        return True
    else:
        return False

