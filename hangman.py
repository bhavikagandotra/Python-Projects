from random import choice
words=['respectful','artifacts','entrepreneur','counselor']
correct=[]
wrong=[]
tries=6
right_ans=0
game_fin=False

def select_word(list_of_word):
    choosen_word=choice(list_of_word)
    different_letters=len(set(choosen_word))
    return choosen_word,different_letters

def ask_letter():

    choosen_letter=''
    valid=False
    alphabet='abcdefghijklmnopqrstuvwxyz'
    while not valid:
        chosen_letter=input("Please enter a letter ")
        if chosen_letter in alphabet and len(chosen_letter)==1:
            valid=True
        else:
             print("You haven't chosen correct letter")
    return chosen_letter

def show(chosen_word):
    hidden_list=[]
    for l in chosen_word:
        if l in correct:
            hidden_list.append(l)
        else:
            hidden_list.append('-')
    print(' '.join(hidden_list))

def check_letter(chosen_letter,hidden_word,tries,matches):
    end=False
    if chosen_letter in hidden_word:
        