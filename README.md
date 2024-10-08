# Text Parser for Information Retrieval (IR) Engine
This project mainly implements a text parser that is the first component of Information Retrieval (IR) engine. This parser does some tasks like processing documents, tokenizing the text, removing stopwords and stemming all the remaining words and generating word and file dictionaries.

## Features
Tokenizer: Used for tokenization and splits text into tokens by removing numbers and converting tokens into lowercase. 

Removing stopwords: Eliminating some common stopwords from the token list. 

Stemming: This stemming is done by applying Porter stemming algorithm that helps in reducing words to their base forms. 

Word Dictionary: This dictionary is created to map each unique token to a unique ID.

File Dictionary: This dictionary is also created to map each document to a unique ID.

## The inputs processed are stored as output data into parser_output.txt

## The files that are included in this project zip file are:
Project1_PythonCode.py: The main Python script that contains all text parsing functionalities.

input_files: A directory that contains all input files in the form of .txt that are to be parsed.

stopwordlist.txt: A file that contains a list of common stopwords.

parser_output.txt: The output file where the results that are parsed are stored.

WordDictionary.txt: A file that maps unique words to unique ID's. 

FileDictionary.txt: A file that maps document names to unique ID's.

## Requirements that are needed to complete this project1 are:

### Python 3.x

### Required Python libraries:
nltk: Library that is necessary for stemming.

### To install the necessary package, run:
bash
Copy code
pip install nltk

### How to Run the Program
#### Prepare Input Files:

Create a directory named input_files and place all the .txt files you want to parse into this folder or directory. 
Ensure that stopwordlist.txt is also there.
#### Run and execute the script present in the .py file given below:
Project1_PythonCode.py

Next, this script will process all .txt files in the input_files directory and perfrom tokenization, stopwords removal, stemming all other words that are left and next the output is saved into parser_output.txt, WordDictionary.txt, and FileDictionary.txt.

#### Output: After the script runs successfully, the below .txt files are found:

parser_output.txt: Contains the document IDs and the tokens along with their ID's.

WordDictionary.txt: Contains the unique tokens and ID's.

FileDictionary.txt: Contains the document names and IDs.

#### Example Output (from parser_output.txt):

Document: sample1.txt, ID: 1
example	1
test	2
sample	3

Document: sample2.txt, ID: 2
...

#### Troubleshooting is done to ensure: 
Whether the input_files directory contains valid .txt files and that the files are not empty and 
Stopwords File contains stopwords in a properly formatted manner (one word per line).

#### By:
#### Name: Reddy Krishna Reddy Yeddula 
#### Email ID: ReddyKrishnaReddyYeddula@my.unt.edu  
