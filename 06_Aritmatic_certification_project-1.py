def arithmetic_arranger(problems, show_answers=False):
    first_line = ''
    second_line = ''
    dashes = ''
    result_line = ''

    if len(problems) > 5:
        return 'Error: Too many problems.'
    else:
        for problem in problems:

            #splititng problems
            parts = problem.split()
            operand_one = parts[0]
            operator = parts[1]
            operand_two = parts[2]

            # Error Handler
            if operator not in ['+','-']:
                return "Error: Operator must be '+' or '-'."
            if not operand_one.isdigit() or not operand_two.isdigit():
                return "Error: Numbers must only contain digits."
            if len(operand_one) > 4 or len(operand_two) > 4:
                return "Error: Numbers cannot be more than four digits." 

            # lebar kolom
            width = max(len(operand_one), len(operand_two))+2

            # baris pertama
            first_line += str(operand_one).rjust(width)+'    '

            # baris kedua
            second_line += operator + str(operand_two).rjust(width-1)+'    '\

            #Garis putus-putus
            dashes += '-' * width + '    '

            #baris hasil operasi bilangan
            result = ''
            if operator == '+':
                result = str(int(operand_one)+int(operand_two))
            else: result = str(int(operand_one)-int(operand_two))
            result_line += str(result).rjust(width)+'    '

    arranged_problems = first_line.rstrip()+'\n'+second_line.rstrip()+'\n'+dashes.rstrip()
    if show_answers == True:
        return arranged_problems + '\n'+result_line.rstrip()
    return arranged_problems
    
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49","123 + 49"]))
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
