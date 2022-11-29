prods={
    'E+E':'E',
    'E-E':'E',
    '(E)':'E',
    'a':'E',
    'b':'E'
} 
def checkForMatch(stack):
    string=""
    count=0
    while stack!=[]:
        string+=stack.pop()
        count+=1
        if string[::-1] in prods:
            return count
    return -1 
inputString='(a+b)'
# inputString='a-b+' 
stack=[] 
for x in inputString:
    stack.append(x)
    print(stack,inputString[inputString.find(x)+1:],f'Shifted {x}')
    countToReplace=checkForMatch(stack.copy())
    while countToReplace>0:
        string=""
        while countToReplace:
            string+=stack.pop()
            countToReplace-=1
        string=string[::-1]
        stack.append(prods[string])
        print(stack,inputString[inputString.find(x)+1:],f'{prods[string]}->{string}')
        countToReplace=checkForMatch(stack.copy()) 
if len(stack)==1:
    print('String accepted!')
else:
    print('String rejected!')
