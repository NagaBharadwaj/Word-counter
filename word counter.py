def word_counter(text):
    words = text.split()
    num_words = len(words)
    return num_words
user_text = input("Please enter the text:")
word_count = word_counter(user_text)
print(f"The number of words in the given text is: {word_count}")

