import re
from Nucleotide import *

def nucleoReader(filename):

    nucleoList = []
    with open(filename, 'r') as f:
        for line in f:
            line.strip()
            m = re.findall(r'\b[A-Z]\d+ : [G,C,U,A] .*\b', line)
            if (m):
                line = line.split(" ")
                tuple = line[0], line[2] 
                nucleotide = Nucleotide(None, None, tuple[1], tuple[0], None)
                nucleoList.append(nucleotide)

    return nucleoList