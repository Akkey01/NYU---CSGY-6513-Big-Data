#!/usr/bin/env python

import sys

for line in sys.stdin:
    line = line.strip()
    if not entry:
        continue  # Skip empty lines

    tokens = line.split()
    for token in tokens:
        print(f'{token}\t1')  # Tab-separated output
