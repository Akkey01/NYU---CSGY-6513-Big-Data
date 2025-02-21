#!/usr/bin/env python3
import sys

sentence_count = 0

for line in sys.stdin:
    _, count = line.strip().split("\t")
    sentence_count += int(count)

# Print the total count of sentences
print(f"Total Sentences: {sentence_count}")
