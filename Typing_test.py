

# from time import time
# print('Press Enter to star or to break a new line')
# print('Press Enter twice to finish typing')
# input('......................................')
# start = time()
# text = []
# while True:
#     line  = input()
#     if not line:
#         break
#     text.append(line)


# end = time()
# # print('The text user typed in: ')
# # for line in text:
# #     for line in  text:
# #         print(line)

# print('.......................................')
# elapsed_time = (end - start)/60
# chars_count = sum(len(item) for item in text)
# words_count = chars_count/5
# wpm = round(words_count/elapsed_time)
# print(f'your average Words Per Minute(WPM) is: {wpm}')


# from time import time

# # Function to count errors in typed text
# def calculate_errors(original_text, user_input):
#     errors = 0
#     for i in range(min(len(original_text), len(user_input))):
#         if original_text[i] != user_input[i]:
#             errors += 1
#     # Count remaining characters in case the lengths differ
#     errors += abs(len(original_text) - len(user_input))
#     return errors

# # Function to display results
# def display_results(original_text, user_input, elapsed_time, wpm, errors, accuracy):
#     print('-------------------------------------------------')
#     print(f"Original text: \n{original_text}")
#     print('-------------------------------------------------')
#     print(f"User's input: \n{user_input}")
#     print('-------------------------------------------------')
#     print(f"Elapsed time: {elapsed_time:.2f} seconds")
#     print(f"Words per minute (WPM): {wpm}")
#     print(f"Errors made: {errors}")
#     print(f"Typing accuracy: {accuracy:.2f}%")

# # Predefined text for typing
# original_text = """The quick brown fox jumps over the lazy dog. This sentence contains every letter of the alphabet and is used to practice typing."""
# print('Please type the following text as accurately and quickly as possible:')
# print('-------------------------------------------------')
# print(original_text)
# print('-------------------------------------------------')
# input('Press Enter to start typing...')

# # Start the timer and collect input
# start_time = time()
# user_input = input()
# end_time = time()

# # Calculate elapsed time in seconds
# elapsed_time = end_time - start_time

# # Count characters and calculate WPM (assuming 5 characters = 1 word)
# chars_count = len(user_input)
# words_count = chars_count / 5
# wpm = round(words_count / (elapsed_time / 60))

# # Calculate errors and accuracy
# errors = calculate_errors(original_text, user_input)
# accuracy = max(0, 100 * (1 - errors / len(original_text)))

# # Display the results
# display_results(original_text, user_input, elapsed_time, wpm, errors, accuracy)


import random
import lorem
from time import time

# Function to count errors in typed text
def calculate_errors(original_text, user_input):
    errors = 0
    for i in range(min(len(original_text), len(user_input))):
        if original_text[i] != user_input[i]:
            errors += 1
    # Count remaining characters in case the lengths differ
    errors += abs(len(original_text) - len(user_input))
    return errors

# Function to display results
def display_results(original_text, user_input, elapsed_time, wpm, errors, accuracy):
    print('-------------------------------------------------')
    print(f"Original text: \n{original_text}")
    print('-------------------------------------------------')
    print(f"User's input: \n{user_input}")
    print('-------------------------------------------------')
    print(f"Elapsed time: {elapsed_time:.2f} seconds")
    print(f"Words per minute (WPM): {wpm}")
    print(f"Errors made: {errors}")
    print(f"Typing accuracy: {accuracy:.2f}%")

# Function to generate a random paragraph of `num_sentences` length
def generate_random_paragraph(num_sentences=5):
    sentences = [lorem.sentence() for _ in range(num_sentences)]
    return ' '.join(sentences)

# User input to set the number of sentences in the paragraph
num_sentences = int(input('Enter the number of sentences for the random paragraph: '))

# Generate random text for typing
original_text = generate_random_paragraph(num_sentences)
print('Please type the following text as accurately and quickly as possible:')
print('-------------------------------------------------')
print(original_text)
print('-------------------------------------------------')
input('Press Enter to start typing...')

# Start the timer and collect input
start_time = time()
user_input = input()
end_time = time()

# Calculate elapsed time in seconds
elapsed_time = end_time - start_time

# Count characters and calculate WPM (assuming 5 characters = 1 word)
chars_count = len(user_input)
words_count = chars_count / 5
wpm = round(words_count / (elapsed_time / 60))

# Calculate errors and accuracy
errors = calculate_errors(original_text, user_input)
accuracy = max(0, 100 * (1 - errors / len(original_text)))

# Display the results
display_results(original_text, user_input, elapsed_time, wpm, errors, accuracy)
