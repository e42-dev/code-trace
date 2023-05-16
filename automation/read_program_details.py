import sys

def readlines(file_name):
    all_lines = []
    with open(file_name) as fp:
        lines = fp.readlines()
        for line in lines:
            all_lines.append(line.rstrip("\n"))
    return all_lines

def get_details_from_file(file_name):

    lines = readlines(file_name)

    title = lines[1]
    walkthrough_id = lines[5]
    explaination = lines[9]

    # find the position of variables
    variables_pos = 0
    for i in range(len(lines)):
        if lines[i] == "trace_variables:":
            variables_pos = i

    variables = lines[variables_pos + 1]

    # pos: 13 to (variables_pos - 2) is code
    code_lines = lines[13: variables_pos - 1]
    code = "\n".join(code_lines)

    # pos: (variables_pos + 5) to len(lines) - 1 is walkthrough
    walkthrough_lines = lines[variables_pos + 5 : len(lines)]
    walkthrough = "\n".join(walkthrough_lines)

    return (title, walkthrough_id, explaination, code, variables, walkthrough)

if __name__ == "__main__":
    file_name = sys.argv[1]
    title, walkthrough_id, explaination, code, variables, walkthrough = get_details_from_file(file_name)
    print(title)
    print(walkthrough_id)
    print(explaination)
    print(code)
    print(variables)
    print(walkthrough)