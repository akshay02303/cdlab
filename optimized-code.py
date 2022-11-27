
f = open('data.txt', 'r')

loop_variable = ''
statements_not_containing_loop_variables = []
loop_statements_being_processed = False

for line in f:
    if 'for' in line:
        loop_variable = line[line.find('(') + 1]
        loop_statements_being_processed = True
    if loop_statements_being_processed == False:
        print(line,end="")
        continue
    if loop_variable in line or '{' in line or '}' in line:
        print(line, end="")
        if '}' in line:
            loop_statements_being_processed = False
            while statements_not_containing_loop_variables:
                print(statements_not_containing_loop_variables.pop(0))
    else:
        statements_not_containing_loop_variables.append(line)


