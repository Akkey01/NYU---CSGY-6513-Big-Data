#!/usr/bin/env python3
import sys

vowel_counts = {}

# Read input from stdin
for line in sys.stdin:
    vowel, count = line.strip().split("\t")
    count = int(count)
    
    if vowel in vowel_counts:
        vowel_counts[vowel] += count
    else:
        vowel_counts[vowel] = count

# Print total count of each vowel
for vowel in sorted(vowel_counts.keys()):  # Sorting for better readability
    print(f"{vowel}\t{vowel_counts[vowel]}")
