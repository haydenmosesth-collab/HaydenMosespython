def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/' or op == '%':
        return 2
    if op == '^':
        return 3
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:
        if ch.isalnum():
            postfix += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()

        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(ch)):
                postfix += stack.pop()
            stack.append(ch)

    while stack:
        postfix += stack.pop()

    return postfix


def evaluate_postfix(postfix):
    stack = []

    for ch in postfix:
        if ch.isdigit():
            stack.append(int(ch))

        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)
            elif ch == '%':
                stack.append(a % b)
            elif ch == '^':
                stack.append(a ** b)

    return stack.pop()


# Main program
expression = input("Infix Expression: ")

postfix = infix_to_postfix(expression)
result = evaluate_postfix(postfix)

print("Postfix Expression:", postfix)
print("Evaluated Result:", result)

        
        
