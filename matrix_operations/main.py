def read_matrices(lines):
    matrices = {}  # dictionary to store matrices
    index = 2  # start index of the matrix data

    while index < len(lines):
        line = lines[index].strip()

        if line == 'operations':
            break
        # read the matrix id
        matrix_id = line
        index += 1
        matrix = []
        # read the matrix data
        while index < len(lines) and lines[index].strip():
            # store the matrix data in the list
            matrix.append(list(map(int, lines[index].strip().split())))
            index += 1
        # store the matrix in the dictionary
        matrices[matrix_id] = matrix
        index += 1  # skip blank line
    # return the matrices and the index where operations start
    return matrices, index + 1

def read_operations(lines, start_index):
    # read the operations from the input
    return [line.strip() for line in lines[start_index:] if line.strip()]

def to_postfix(expression, operator):
    # convert infix expression to postfix expression
    postfix_expr = []
    stack = []
    # loop through each character in the expression
    for char in expression.replace(' ', ''):
        # check if the character is an operator
        if char in operator:
            if char == '(':
                stack.append(char)
            elif char == ')':
                # pop operators from the stack until '(' is found
                while stack and stack[-1] != '(':
                    postfix_expr.append(stack.pop())
                stack.pop()  # pop '(' from the stack
            else:
                # pop operators with higher or equal precedence from the stack
                while stack and stack[-1] != '(' and operator[char] <= operator[stack[-1]]:
                    postfix_expr.append(stack.pop())
                stack.append(char)
        else:
            # append operands to the postfix expression
            postfix_expr.append(char)
    # append remaining operators to the postfix expression
    postfix_expr.extend(reversed(stack))
    return postfix_expr

def compute_expression(expression, matrices, operator):
    # compute the expression using the matrices
    stack = []
    # loop through each character in the expression
    for char in expression:
        if char in operator:
            # pop two matrices from the stack
            b = stack.pop()
            a = stack.pop()
            if char == '+':
                # matrix addition
                result = [[a[i][n] + b[i][n] for n in range(len(a[0]))] for i in range(len(a))]
            elif char == '*':
                # matrix multiplication
                result = [[sum(a[i][k] * b[k][n] for k in range(len(a[0]))) for n in range(len(b[0]))] for i in range(len(a))]
            stack.append(result)
        else:
            # push the matrix to the stack
            stack.append(matrices[char])
    return stack.pop()

def format_matrix(matrix):  # format the matrix for output
    return '\n'.join([' '.join(map(str, row)) for row in matrix])

with open('matrix_operations/input.txt', 'r') as file:  # read input file
    lines = file.readlines()

# read matrices and operations from the input
matrix_data, operation_start_index = read_matrices(lines)
operation_list = read_operations(lines, operation_start_index)
# define the precedence of operators
operator = {'+': 1, '*': 2}

# loop through each operation
for operation in operation_list:
    # convert infix expression to postfix expression
    postfix_expr = to_postfix(operation, operator)
    result_matrix = compute_expression(postfix_expr, matrix_data, operator)
    formatted_output = format_matrix(result_matrix)
    print(operation, formatted_output, end='\n\n', sep='\n')