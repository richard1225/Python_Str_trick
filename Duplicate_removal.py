import sys

with open(sys.argv[1]) as f:
    lines = f.read().split("\n")

lines = list(set(lines))
with open(sys.argv[2],'w') as f:
    for line in lines:
        f.write(line+"\n")
