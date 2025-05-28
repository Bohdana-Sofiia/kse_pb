def count_words(text):
    words = text.split()
    wordCount = len(words)
    return wordCount

def average_word_length(text):
    total_length = 0
    words = text.split()
    for word in words:
        total_length += len(word)
    average = total_length / len(words)
    return(average)


print(average_word_length("Hello, World bro!"))