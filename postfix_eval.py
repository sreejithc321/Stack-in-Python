from stack import Stack

def eval_postfix(postfixExpr):
    operand_stack = Stack()
    tokenList = postfixExpr.split()
    for token in tokenList:
		# If the token is an operand, convert it from a string to an integer and push the value onto stack
        if token in "0123456789":
            operand_stack.push(int(token))
        # If the token is an operator, *, /, +, or -, Pop the operandStack twice.     
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            # Perform the arithmetic operation.
            result = evaluate(token,operand1,operand2)
            # Push the result back on the stack. 
            operand_stack.push(result)
    return operand_stack.pop()

def evaluate(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(eval_postfix('7 8 + 3 2 + /'))
