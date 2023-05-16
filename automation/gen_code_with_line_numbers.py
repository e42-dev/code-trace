import sys

prefix = """01 #include "భవిష్యత్తులో.నేను"   
02
03 START
04
"""
#
# generate the code with lines.
#

code_file = sys.argv[1]
line_no = 5
output_lines = []
# Read lines from the file
with open(code_file) as fp:
    code_lines = fp.readlines()
    for line in code_lines:
        line = line. rstrip('\n')
        output_lines.append(f"{line_no:02d}" + "   " + line)
        line_no += 1

# add empty line, STOP and empty line
output_lines.append(f"{line_no:02d}")
line_no += 1
output_lines.append(f"{line_no:02d}" + " STOP")
line_no += 1
output_lines.append(f"{line_no:02d}")

print(prefix, end="")
# print(output_lines)
for line in output_lines:
    print(line)