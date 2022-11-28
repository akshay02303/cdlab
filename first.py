from prettytable import PrettyTable

def first(string):
    first_ = set()
    if string in terminals:
        first_ = {string} 
    elif string == "" or string == "@":
        first_ = {"@"}
    elif string in non_terminals:
        alternatives = productions_dict[string]
        for alternative in alternatives:
            first_ = first_ | first(alternative) 
    else:
        first_2 = first(string[0])
        if "@" in first_2:
            i = 1 
            while "@" in first_2:
                first_ = first_ | (first_2 - {"@"})
                if string[i:] in terminals:
                    first_ = first_ | {string[i:]}
                    break 
                elif string[i:] == "":
                    first_ = first_ | {"@"}
                    break 
                first_2 = first(string[i:])
                first_ = first_ | (first_2 - {"@"})
                i += 1 
        else:
            first_ = first_ | first_2 
    return first_ 

num_terminals = int(input("Enter number of terminals: "))
terminals = []
print("Enter the terminals: ")
for _ in range(num_terminals):
    terminals.append(input())

num_non_terminals = int(input("Enter number of non-terminals: "))
non_terminals = []
print("Enter the non terminals: ")
for _ in range(num_non_terminals):
    non_terminals.append(input())

num_productions = int(input("Enter the number of productions: "))
productions = []
for _ in range(num_productions):
    productions.append(input())

productions_dict = {}
for nt in non_terminals:
    productions_dict[nt] = []

for production in productions:
    lhs, rhs = production.split("->")
    alternatives = rhs.split("/")
    for alternative in alternatives:
        productions_dict[lhs].append(alternative) 

FIRST = {}
for nt in non_terminals:
    FIRST[nt] = set()

for nt in non_terminals:
    FIRST[nt] = FIRST[nt] | first(nt) 

table = PrettyTable(["Non Terminal", "First"])
for nt in non_terminals:
    table.add_row([nt, str(FIRST[nt])])

print(table)
