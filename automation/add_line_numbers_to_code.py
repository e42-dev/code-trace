import sys
#
# generate the code with lines.
#

code_file = sys.argv[1]
line_no = 1
output_lines = []
# Read lines from the file
with open(code_file) as fp:
    code_lines = fp.readlines()
    for line in code_lines:
        line = line. rstrip('\n')
        output_lines.append(f"{line_no:02d}" + "   " + line)
        line_no += 1
output_lines.append(f"{line_no:02d}")
      
# print(output_lines)
for line in output_lines:
    print(line)