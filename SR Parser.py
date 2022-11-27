def check(grammar, target):
    for key, value in grammar.items():
        if target in value:
            return key
    return None
grammar = {
"E": ["E+E", "E-E", "(E)", "a", "b"]
}
starting_symbol = "E"
print("Given grammar is ")
for key, value in grammar.items():
    for val in value:
        print(f"{key}->{val}")
string = input("Enter input string: ")
stack = []
idx = 0
while True:
    s = ""
    flag = False
    while len(stack):
        s += stack.pop()
        nt = check(grammar, s[::-1])
        if nt is not None:
            stack.append(nt)
            print([stack[:], string[idx: ], f"{nt}->{s[::-1]}"])
            flag = True
            break
    if not flag:
        for char in s[::-1]:
            stack.append(char)
        try:
            stack.append(string[idx])
            idx += 1
        except:
            print("string rejected")
            break
        print([stack[:], string[idx: ], f"shifted {string[idx-1]}"])
    if len(stack) == 1 and stack[0] == starting_symbol and idx == len(string):
        print("string accepted")
        break
