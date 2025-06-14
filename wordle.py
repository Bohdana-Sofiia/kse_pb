from wordle_functions import generate_word, check_guess, display_result, is_valid

words = ['apple','bread','candy','dream','eagle','flame','grape','house','input','joker']
while True:
    secret_word = generate_word(words)
    word_len = len(secret_word)
    tries = 6

    print("Welcome to Wordle!")
    print("Guess the",word_len,"-letter word. You have", tries, "tries.")

    for attempt in range(1, tries + 1):
        guess = input(f"Attempt {attempt}/6 – Enter guess: ").lower()

        if not is_valid(guess, word_len):
            continue

        if guess == secret_word:
            print("You win!!!")
            break

        result = check_guess(guess, secret_word)
        display_result(guess, result)
    else:
        print("You lose! The word was:", secret_word)

    again = input("Do you want to play again?: ").strip().lower()
    if again != 'yes':
        print("Thanks for playing!")
        break
    #hello