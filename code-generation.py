# question : 20
operators = {
            '+': 'A',
            '-': 'S',
            '*': 'M',
            '/': 'D'
        }
expression=input()
#expression = "ab*c+"
stack = []
for x in expression:
    if x.isalpha():
        stack.append(x)
    else:
        A = stack.pop()
        B = stack.pop()
        print("L {}".format(B))
        print("{} {}".format(operators[x], A))
        stack.append("{} {} {}".format(B, x, A))

