# BookBot

BookBot is a simple Python project that takes in a book (as a `.txt` file) and generates a statistical analysis of the characters in the text. It’s designed as a lightweight tool to explore how often each character appears, making it easy to analyze large amounts of text programmatically.

---

## Features
- Reads plain text book files (`.txt`)
- Counts the frequency of each character
- Sorts results by most/least common characters
- Outputs a clear statistical summary

---

## Example Output

For a given book, BookBot might output something like:

--- BookBot Report ---
Total characters: 235,411
Unique characters: 68
Top 10 most frequent characters:
' ' (space): 52,310 times
'e': 32,844 times
't': 24,111 times
'a': 20,876 times
...

---

## Installation

Clone this repository:
git clone https://github.com/nash226/bookbot.git

No external libraries are required—BookBot runs on standard Python.

---

## Usage

Run BookBot by passing in the path to your text file:
python bookbot.py books/frankenstein.txt

Output will be printed directly in your terminal.
