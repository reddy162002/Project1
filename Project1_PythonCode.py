import re
import os
from collections import defaultdict
from nltk.stem import PorterStemmer
# First initialize the Porter Stemmer
stemmer = PorterStemmer()
# Next proceed with tokenization by tokenizing text into tokens
def tokenize(text):
    tokens = re.findall(r'\b[a-zA-Z]+\b', text)
    tokens = [token.lower() for token in tokens]
    return tokens
# After that we are eliminating stopwords from that token list
def remove_stopwords(tokens, stopwords):
    return [token for token in tokens if token not in stopwords]
# Next stemming is done on remaining words
def stem(word):
    return stemmer.stem(word)
# A word dictionary is then created to map each unique word to a unique ID
class WordDictionary:
    def __init__(self):
        self.word_to_id = {}
        self.current_id = 1
    def get_word_id(self, word):
        if word not in self.word_to_id:
            self.word_to_id[word] = self.current_id
            self.current_id += 1
        return self.word_to_id[word]
    def save(self, file):
        with open(file, 'w') as f:
            for word, word_id in self.word_to_id.items():
                f.write(f"{word}\t{word_id}\n")
# Then a file dictionary is created to map each document name to a unique ID
class FileDictionary:
    def __init__(self):
        self.file_to_id = {}
        self.current_id = 1
    def get_file_id(self, file_name):
        if file_name not in self.file_to_id:
            self.file_to_id[file_name] = self.current_id
            self.current_id += 1
        return self.file_to_id[file_name]
    def save(self, file):
        with open(file, 'w') as f:
            for file_name, file_id in self.file_to_id.items():
                f.write(f"{file_name}\t{file_id}\n")
# Next we use a function to process input documents and to generate results in parser_output.txt
def process_documents(input_dir, stopwords_file, output_file):
    word_dict = WordDictionary()
    file_dict = FileDictionary()
    try:
        with open(stopwords_file, 'r') as f:
            stopwords = set(f.read().splitlines())
            print(f"Loaded stopwords: {stopwords}")
    except FileNotFoundError:
        print(f"Stopwords file '{stopwords_file}' not found.")
        return
    if not os.path.exists(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        return
    with open(output_file, 'w') as output:
        for filename in os.listdir(input_dir):
            if filename.endswith(".txt"):
                file_path = os.path.join(input_dir, filename)
                doc_id = file_dict.get_file_id(filename)
                try:
                    with open(file_path, 'r') as file:
                        text = file.read()
                        if len(text) == 0:
                            print(f"File '{filename}' is empty.")
                            continue
                        print(f"File processing: {filename}")
                        print(f"Original text: {text[:100]}...")
                        tokens = tokenize(text)
                        if len(tokens) == 0:
                            print(f"No valid tokens present in '{filename}' after tokenization.")
                            continue
                        print(f"Tokens before stopwords removal: {tokens}")
                        tokens = remove_stopwords(tokens, stopwords)
                        if len(tokens) == 0:
                            print(f"No tokens present in '{filename}' after stopwords removal.")
                            continue
                        tokens = [stem(token) for token in tokens]
                        print(f"Finally tokens for {filename}: {tokens}")
                        output.write(f"Document: {filename}, ID: {doc_id}\n")
                        for token in tokens:
                            word_id = word_dict.get_word_id(token)
                            output.write(f"{token}\t{word_id}\n")
                        output.write("\n")
                except FileNotFoundError:
                    print(f"File '{file_path}' not found.")
    word_dict.save("WordDictionary.txt")
    file_dict.save("FileDictionary.txt")
    print(f"Processing completed successfully and output is written into '{output_file}'.")
if __name__ == "__main__":
    # Directory that have all input files taken from input TREC data
    input_dir = "input_files"
    # File that contains list of stopwords
    stopwords = "stopwordlist.txt"
    # Output file that contains results that are parsed are stored here
    output = "parser_output.txt"
    process_documents(input_dir, stopwords, output)
    print("Processing completed successfully and output is checked in 'parser_output.txt'.")