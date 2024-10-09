# Text Parser for Information Retrieval (IR) Engine

This project implements a text parser, which serves as the initial component of an Information Retrieval (IR) engine. The parser performs several key tasks such as document processing, tokenization, removing stopwords, stemming the remaining tokens, and creating word and file dictionaries.

## Key Features
Tokenizer: Breaks down text into individual tokens by excluding numbers and converting all tokens to lowercase.
Stopwords Removal: Filters out common stopwords from the list of tokens.
Stemming: Applies the Porter Stemming Algorithm to reduce tokens to their base or root forms.
Word Dictionary: Creates a mapping between each unique token and a corresponding unique ID.
File Dictionary: Creates a mapping between each document and its own unique ID.

 ## Output

The processed data is saved in `parser_output.txt`.

## Project Files

The following files are included within this project:

 **chandumukkamala.py**: The primary Python script that implements all text parsing functionalities.
  
 **Input_Files**: A folder that contains all the `.txt` input files that need to be parsed.
  
 **stopwordlist.txt:** A file that contains a list of commonly used stopwords.
  
 **parser_output.txt:** The output file where the parsing results are saved.
  
 **WordDictionary.txt:** A file that maps each unique word to its unique ID.
  
 **FileDictionary.txt:** A file that maps each document to its unique ID.

## Requirements for Project Completion

### Python Version

 Python 3.x or higher.

### Required Python Libraries

 **nltk:** This library is required for stemming functionality.


## Running the Program

### Preparing Input Files:

1. To begin, create a folder called `Input_Files` and fill it with all of the `.txt` files you wish to process.
2. Verify that the same directory has the `stopwordlist.txt` file as well.

### Running the Script:

Execute the `chandumukkamala.py` script. This script processes all `.txt` files in the `input_files` directory by performing tokenization, removing stopwords, and stemming the remaining tokens. The results are saved into `parser_output.txt`, `WordDictionary.txt`, and `FileDictionary.txt`.

### Output Files

After running the script, the following output files will be generated:

 **parser_output.txt:** Contains document IDs and the corresponding tokens along with their unique IDs.
  
 **WordDictionary.txt:** Contains all unique tokens and their IDs.
  
 **FileDictionary.txt:** Contains document names and their IDs.

### Sample Output (from `parser_output.txt`):


Document: sample1.txt, ID: 1
example    1
test       2
sample     3

Document: sample2.txt, ID: 2
...


## Troubleshooting Tips

 Verify that there are actual `.txt} files in the {Input_Files} directory and that none of the files are empty.

 Check that every stopword is on a different line in the `stopwordlist.txt` file, and that the formatting is proper.


**Author Information:**

**Name:** Harichandana Mukkamala  
**Email ID:** Harichandana Mukkamala@my.unt.edu 
