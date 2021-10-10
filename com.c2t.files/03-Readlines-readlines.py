with open('ReadingFile.txt') as f:
    lines = f.readlines()
    print(lines)
    print(type(lines))

for line in lines:
    print(line,end='')