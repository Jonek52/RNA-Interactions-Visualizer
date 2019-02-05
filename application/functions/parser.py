def parser(fileName):
    import re

    file = open('output.txt', 'w')
    with open(fileName , 'r') as f:
        for line in f:
            line.strip()
            m = re.findall(
                r'\b[A-Z].+-[A-Z].+ : [G,C,U,A]-[G,C,U,A] [W,S,H][w,s,h]/[W,S,H][w,s,h] pairing antiparallel.*\b', line)
            if (m):
                pattern = (r'(?<=[A-Z])[a-z]| pairing antiparallel|(?<=cis).*|(?<=trans).*')
                s = re.sub(pattern, "", line)

                patter2 = (r'-| : ')
                d = re.sub(patter2, " ", s)

                pattern3 = (r'[/]')
                n = re.sub(pattern3, "", d)
                file.write(n)

    file.close()