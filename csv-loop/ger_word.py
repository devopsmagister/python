
import re

def grep_word(file_path, word):
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            w = f"{word}.WORLD"

            # Use a regular expression to find lines containing the word
            matching_lines = [line for line in lines if re.search(r'^\s*{}\b'.format(w), line, re.IGNORECASE)]

            return matching_lines
    except FileNotFoundError:
        return f"File not found: {file_path}"

file_path = 'data.csv'
word_to_grep = "xxxxx"
if grep_word(file_path, word_to_grep):
    print("string found")
else:
    print("failed!!!" )   
