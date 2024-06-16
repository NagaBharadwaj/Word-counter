# Word Counter

## Overview
The Word Counter is a simple Python program that counts the number of words in a given text. It takes user input from the console and outputs the word count. This program is a great example for beginners to understand basic string manipulation and user input handling in Python.

## Features
- Counts the number of words in a user-provided text.
- Simple and easy-to-understand code.
- Demonstrates basic use of Python's string methods.

## Getting Started

### Prerequisites
- Python 3.x installed on your machine.

### Installation
1. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/NagaBharadwaj/word-counter.git

### Navigate to the project directory:
cd word-counter

### Usage
1.Run the word_counter.py script:
python word_counter.py

2.When prompted, enter the text for which you want to count the words.
3.The program will output the number of words in the provided text.
### Example
$ python word_counter.py
Please enter the text: This is an example text to demonstrate the word counter.
The number of words in the given text is: 9

### Code Explanation
The core functionality of the Word Counter is implemented in the count_words function. Here’s a breakdown of the code:

def count_words(text):
    # Split the text into words
    words = text.split()
    # Count the number of words
    num_words = len(words)
    return num_words

### Prompt the user to enter some text
user_text = input("Please enter the text: ")

### Count the words in the user input
word_count = count_words(user_text)

### Print the result
print(f"The number of words in the given text is: {word_count}")
