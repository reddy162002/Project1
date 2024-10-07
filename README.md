# Text Parser for Information Retrieval (IR) Engine Overview
This project implements a Text Parser, which serves as the first component of an Information Retrieval (IR) engine. The parser processes documents, tokenizes the content, removes stopwords, stems the remaining tokens, and generates dictionaries for both terms and documents.

# Features
Tokenizer: Splits the text into tokens, removes numbers, and converts tokens to lowercase.

Stopword Removal: Eliminates common stopwords from the token list.
Stemming: Applies the Porter stemming algorithm to reduce words to their base forms.
Word Dictionary: Maps each unique token to a unique numerical ID.
File Dictionary: Maps each document to a unique numerical ID.
Outputs processed data into parser_output.txt.
Files Included
text_parser.py: The main Python script containing the text parsing functionalities.
input_files/: A directory containing the input .txt documents to be parsed.
stopwordlist.txt: A file containing a list of common stopwords, one per line.
parser_output.txt: The output file where the parsed results are stored.
WordDictionary.txt: A file mapping unique words to their IDs.
FileDictionary.txt: A file mapping document names to their IDs.
Requirements
Python 3.x
Required Python libraries:
nltk: For stemming.
To install the necessary package, run:

bash
Copy code
pip install nltk
How to Run the Program
Prepare Input Files:

Create a directory named input_files and place all the .txt files you want to parse into this directory.
Ensure that stopwordlist.txt is in the same directory as the Python script.
Run the Script: Execute the Python script:

bash
Copy code
python text_parser.py
The script will:

Process all .txt files in the input_files directory.
Tokenize, remove stopwords, and stem each document.
Save the output to parser_output.txt, WordDictionary.txt, and FileDictionary.txt.
Output: After the script finishes running, you will find:

parser_output.txt: Contains the document IDs and the corresponding tokens along with their IDs.
WordDictionary.txt: Contains the unique tokens and their IDs.
FileDictionary.txt: Contains the document names and their IDs.
Example Output (from parser_output.txt):
yaml
Copy code
Document: sample1.txt, ID: 1
example	1
test	2
sample	3

Document: sample2.txt, ID: 2
...
Notes:
Stemming: The implementation uses the Porter Stemmer from the nltk library for word stemming.
Stopwords: Modify stopwordlist.txt to include or exclude specific stopwords as needed.
Troubleshooting
Empty Output: Ensure that the input_files directory contains valid .txt files and that the files are not empty.
Stopwords File: Ensure stopwordlist.txt is present and properly formatted (one word per line).
Author
Your Name
Contact: [Your email/contact details]
