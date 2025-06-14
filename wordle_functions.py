import random
import string

def generate_word(words):
    return random.choice(words)

def is_valid(guess, word_len):
    for letter in guess:
        if letter not in string.ascii_lowercase:
            print("Write only English lowercase letters.")
            return False
    
    if len(guess) != word_len:
        print("Wrong length. Expected", word_len)
        return False
    return True

def check_guess(guess, secret_word):
    result=[]
    for i in range(len(secret_word)):
        if  guess[i] == secret_word[i]:
            result.append('correct')
        elif guess[i] in secret_word:
            result.append('present')
        else:
            result.append('absent')
    return result

def display_result(guess, result):
    display=[]
    for i in range(len(guess)):
        letter = guess[i]
        res = result[i]
        if res =='correct':
            display.append("[" + letter.upper() + "]")
        elif res =='present':
            display.append("(" + letter + ")")
        else:
            display.append(" " + letter + " ")
    print("Result:", ' '.join(display))