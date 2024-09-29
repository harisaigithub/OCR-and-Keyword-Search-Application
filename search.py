import re

def search_keywords(text, keyword):
    # Split the text into sentences using regular expressions to handle different sentence endings
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)
    
    # Find sentences containing the keyword
    matching_sentences = [sentence for sentence in sentences if keyword.lower() in sentence.lower()]
    
    return matching_sentences
