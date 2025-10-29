def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op == '^':
        return 3
    return 0

def is_operator(c):
    return c in ['+', '-', '*', '/', '^']

def infix_to_postfix(expression):
    stack = []
    output = [] 

    expression = expression.replace(" ", "")

    for char in expression:
        if char.isalnum():
            output.append(char)

        elif char == '(':
            stack.append(char)
       
        elif char == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if stack and stack[-1] == '(':
                stack.pop()  # remove '('
            else:
                print("⚠️ Error: Mismatched parentheses detected.")
                return None
       
        elif is_operator(char):
            while (stack and precedence(stack[-1]) >= precedence(char)):
                output.append(stack.pop())
            stack.append(char)
        else:
            print(f"⚠️ Error: Invalid character '{char}' in expression.")
            return None
        
    while stack:
        if stack[-1] == '(':
            print("⚠️ Error: Mismatched parentheses detected.")
            return None
        output.append(stack.pop())

    return " ".join(output)

print("=============================================")
print("      INFIX TO POSTFIX CONVERTER")
print("     (Shunting Yard Algorithm Demo)")
print("=============================================")

infix = input("Enter an infix expression: ")

print("---------------------------------------------")
postfix = infix_to_postfix(infix)

if postfix:
    print("\n Conversion Successful!")
    print("---------------------------------------------")
    print(f"Infix Expression : {infix}")
    print(f"Postfix Expression: {postfix}")
    print("---------------------------------------------")
