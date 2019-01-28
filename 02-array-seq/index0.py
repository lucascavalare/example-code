"""Build an index mapping word -> list of occurrences"""

import sys
import re

WORD_RE = re.compile('\w+')

index = {}
with open(sys.argv[1], encoding ='utf-8') as fp:
    for line_no, line inenumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no, column_no)
            # this is ugly; coded like this to make a point.
            occurrences = index.get(word, [])
            occurrences.append(location)
            index[word] = occurrences 

for word in sorted(index, key=str.upper):
    print(word, index[word])
