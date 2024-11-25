# Building an Arithmetic Formatter Project

def arithmetic_arranger(problems, show_answers=False):
    """
    Takes in a string containing addition & substraction problems,
    breaks them into separate problems, stacks them vertically, and solves them.

    Args:
    :str - problems: a string containing addition & substraction problems
    :boolean - show_answers: a boolean indicator to notify if the problems
    or not
    """

    # Checking if the number of problems given is less than 5
    if len(problems) > 5:
        show_answers = False
        return "Error: Too many problems."

    # Storing the list of 1st operand
    first_operands = []
    # Storing the list of 2nd operand
    second_operands = []
    # Storing the list of operators
    operators = []
    # Storing the list of answers
    answers = []

    # Looping through each problem in the list
    for problem in problems:
        # Splitting each part in the problem
        problem_parts = problem.split()

        # Making sure if the problem is exactly in 3 parts
        if len(problem_parts) != 3:
            show_answers = False
            return "Error: Invalid problem format"

        # Storing the parts of the problem
        first_number, operator, second_number = problem_parts

        # Making sure there were only '+' and '-' operators
        allowed_operators = ['+', '-']
        if operator not in allowed_operators:
            show_answers = False
            return "Error: Operator must be '+' or '-'."

        # Making sure the 1st and 2nd operands are digits
        if not first_number.isdigit() or not second_number.isdigit():
            show_answers = False
            return "Error: Numbers must only contain digits."

        # Making sure 1st and 2nd operands are not bigger than 4 digits
        if len(first_number) > 4 or len(second_number) > 4:
            show_answers = False
            return "Error: Numbers cannot be more than four digits."

        # Adding the 1st operand to the 1st operands list
        first_operands.append(first_number)
        # Adding the 2nd operand to the 2nd operands list
        second_operands.append(second_number)
        # Adding operator to the operators list
        operators.append(operator)

        # Do addition or subtraction
        if operator == '+':
            answer = str(int(first_number) + int(second_number))
        else:
            answer = str(int(first_number) - int(second_number))

        # Adding answer to the answers list
        answers.append(answer)

    # Creating a list for arranging the problems
    arranged_problems = []
    # Creating a list of top row
    top_row = []
    # Creating a list of bottom row
    bottom_row = []
    # Creating a list of dash row
    dash_row = []
    # Creating a list of answer row
    answer_row = []

    # Looping through the length of the problem string
    for i in range(len(problems)):
        # Storing the length from the 1st operand to 2nd operand(with 2 space padding)
        width = max(len(first_operands[i]), len(second_operands[i])) + 2
        # Storing the right alignment based on the width in the top row(1st operand)
        top_row.append(first_operands[i].rjust(width))
        # Storing the right alignment based on operator and width in the 
        # bottom row(2nd operand + operator)
        bottom_row.append(operators[i] + ' ' + second_operands[i].rjust(width - 2))
        # Adding up the number of dashes based on the width in the dash_row list
        dash_row.append('-' * width)
        # Adding the calculated answer based on the width length to the answers list
        answer_row.append(answers[i].rjust(width))

    # Adding the top row(1st operand) with 5 padding spaces
    arranged_problems.append('   '.join(top_row))
    # Adding the bottom row(operator + 2nd operand) with 5 padding spaces
    arranged_problems.append('    '.join(bottom_row))
    # Adding the dash row below the bottom row
    arranged_problems.append('    '.join(dash_row))

    # Checking if the prompt wants the answers to show
    if show_answers:
        arranged_problems.append('    '.join(answer_row))

    # Reassigning the problem list with newly arranged problems w/ answers
    problems = '\n'.join(arranged_problems)

    return problems
