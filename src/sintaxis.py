expr = "(1-4)/(-1+3)"
stack = []

error = False

for e in expr:
    if e=='(':
        stack.append(e)
    elif e==')':
        if len(stack)>0:
            stack.pop()
        else:
            error = True

if error:
    print("Expresión incorrecta")
else:
    if len(stack)==0:
        print("Expresión correcta")
    else:
        print("Expresión incorrecta")                           