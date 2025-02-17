#!/usr/bin/env python

import sys

last_term = None
last_frequency = 0

frequency_dict = {}

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    
    try:
        token, count = line.split('\t')
        count = int(count)
    except ValueError:
        continue

    if last_term == token:
        last_frequency += count
    else:
        if last_term:
            frequency_dict[last_term] = last_frequency
        last_frequency = count
        last_term = token

if last_term == token:
    frequency_dict[last_term] = last_frequency

frequency_dict = dict(sorted(frequency_dict.items(), key=lambda item: item[1], reverse=True))

top_count = 0
for key, value in frequency_dict.items():
    top_count += 1
    if top_count <= 10:
        print(f'{key}\t{value}')
    else:
        break

