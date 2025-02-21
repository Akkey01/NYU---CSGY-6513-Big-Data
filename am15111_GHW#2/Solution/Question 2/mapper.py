#!/usr/bin/env python3
import sys

# Define vowels
vowels = {'a', 'e', 'i', 'o', 'u'}

# Read input line by line
for line in sys.stdin:
    line = line.strip().lower()  # Convert to lowercase
    for char in line:
        if char in vowels:  # Check if character is a vowel
            print(f"{char}\t1")  # Emit vowel with count 1
