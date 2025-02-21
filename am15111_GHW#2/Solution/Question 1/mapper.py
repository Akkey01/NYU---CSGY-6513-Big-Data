#!/usr/bin/env python3
import sys
import re

# Define sentence-ending punctuation
sentence_delimiters = re.compile(r'[.!?]')

for line in sys.stdin:
    # Trim whitespace and split into sentences using delimiters
    sentences = sentence_delimiters.split(line.strip())
    
    # Emit 1 for each detected sentence
    for sentence in sentences:
        if sentence.strip():  # Ignore empty sentences
            print("Sentence\t1")
