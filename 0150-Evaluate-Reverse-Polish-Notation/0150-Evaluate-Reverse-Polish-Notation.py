class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Create a stack to store the operands
        stack = []
        
        # Iterate through each token in the expression
        for token in tokens:
            # If the token is an operator, pop the top two operands from the stack, perform the operation, and push the result back onto the stack
            if token in ['+', '-', '*', '/']:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                else:
                    result = int(operand1 / operand2)  # Use integer division to truncate towards zero
                stack.append(result)
            # If the token is an operand, convert it to an integer and push it onto the stack
            else:
                stack.append(int(token))
        
        # Return the result, which should be the only value left on the stack
        return stack[0]
