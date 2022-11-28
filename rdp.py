def E():
    T()
    A()

def A():
    global lookahead
    if string[lookahead] == "+":
        lookahead += 1
        T()
        A()
    elif string[lookahead] == "e":
        lookahead += 1
    else:
        return 

def T():
    F()
    B()

def B():
    global lookahead
    if string[lookahead] == "*":
        lookahead += 1
        F()
        B()
    elif string[lookahead] == "e":
        lookahead += 1
    else:
        return 

def F():
    global lookahead
    if string[lookahead] == "(":
        lookahead += 1
        E()
        if string[lookahead] == ")":
            lookahead += 1
    elif string[lookahead] == "i":
        lookahead += 1
    else:
        return

lookahead = 0
string = input()
E()
if string[lookahead] == '$':
    print("Accepted")
else:
    print("Not Accepted")
