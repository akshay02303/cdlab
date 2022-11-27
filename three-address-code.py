#! /usr/bin/env python3

from collections import defaultdict

precedence = {
            '/': 2,
            '*': 2,
            '+': 1,
            '-': 1
        }

def is_operator(op):
    if op in "+*/-":
        return True
    return False

def count_operators(expression):
    count = 0
    for x in expression:
        if is_operator(x):
            count += 1
    
    return count

expression = "2+3*5-2"
op_count = count_operators(expression)
address_count = 0
address_code = defaultdict(str)

while op_count:
    loc = -1
    n = len(expression)

    for i in range(n):
        if is_operator(expression[i]):
            if loc == -1 or precedence[expression[i]] > precedence[expression[loc]]:
                loc = i
    
    beg = loc - 1
    end = loc + 1

    while beg >= 0 and is_operator(expression[beg]) == False:
        beg -= 1
    beg += 1

    while end < n and is_operator(expression[end]) == False:
        end += 1    
    end -= 1

    address_count += 1
    address_code[f't{address_count}'] = expression[beg: end + 1]
    expression = expression[:beg] + f't{address_count}' + expression[end + 1:]  
    op_count -= 1

for key, value in address_code.items():
    print(key, ": ", value)
