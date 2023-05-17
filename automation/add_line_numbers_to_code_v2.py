import sys

# Read file from the first command line argument
with open(sys.argv[1]) as fp:
    for i, line in enumerate(fp, start=1):
        print(f"{i:02d}   {line.rstrip()}")
