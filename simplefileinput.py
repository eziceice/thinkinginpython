import fileinput

for line in fileinput.input(inplace=True):
    line = str(line).rstrip()
    num = fileinput.lineno()
    print(line, num)