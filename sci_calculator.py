import math


def addition(operand1, operand2):
    return operand1 + operand2


def subtract(operand1, operand2):
    return operand1 - operand2


def multiplication(operand1, operand2):
    return operand1 * operand2


def division(operand1, operand2):
    return operand1 / operand2


def exponential(base, exponent):
    return math.pow(base, exponent)


def logarithm(base, value):
    return math.log(value, base)


def start_calculator():
    calculator_on = True
    results = []
    print_menu = True

    while calculator_on:

        if print_menu:
            if len(results) == 0:
                print(f'Current Result: 0.0\n')
            else:
                print(f'Current Result: {results[len(results) - 1]}\n')
            print('Calculator Menu\n'
                  '---------------\n'
                  '0. Exit Program\n'
                  '1. Addition\n'
                  '2. Subtraction\n'
                  '3. Multiplication\n'
                  '4. Division\n'
                  '5. Exponentiation\n'
                  '6. Logarithm\n'
                  '7. Display Average\n')
        print_menu = True

        menu_selection = int(input('Enter Menu Selection: '))

        if 6 >= menu_selection > 0:
            operand1 = input('Enter first operand: ')
            if operand1 == 'RESULT':
                operand1 = results[len(results) - 1]
            else:
                operand1 = float(operand1)

            operand2 = input('Enter second operand: ')
            print()
            if operand2 == 'RESULT':
                operand2 = results[len(results) - 1]
            else:
                operand2 = float(operand2)

            if menu_selection == 1:
                results.append(addition(operand1, operand2))
            elif menu_selection == 2:
                results.append(subtract(operand1, operand2))
            elif menu_selection == 3:
                results.append(multiplication(operand1, operand2))
            elif menu_selection == 4:
                results.append(division(operand1, operand2))
            elif menu_selection == 5:
                results.append(exponential(operand1, operand2))
            elif menu_selection == 6:
                results.append(logarithm(operand1, operand2))
        elif menu_selection == 0:
            print('Thanks for using this calculator. Goodbye!')
            calculator_on = False
        elif menu_selection == 7:
            if len(results) > 0:
                sum_of_calculations = sum(results)
                print(f'Sum of calculations: {sum_of_calculations: .2f}')
                print(f'Number of calculations: {len(results)}')
                print(f'Average of calculations: {sum_of_calculations / len(results): .2f}')
                print_menu = False
            else:
                print('Error: No calculations yet to average!\n')
                print_menu = False
        else:
            print('Error: Invalid selection!\n')
            print_menu = False


if __name__ == '__main__':
    start_calculator()
