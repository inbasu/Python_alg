def find_action(problem):
    actions = [ '+', '-', '*', '/']
    for action in actions:
        if action in problem:
            return action


def solving(num1, num2, action):
    num1, num2 = int(num1), int(num2)
    if action == '+':
        return num1 + num2
    elif action == '*':
        return num1 * num2
    elif action == '-':
        return num1 - num2
    elif action == '/':
        try:
            return num1 / num2
        except ZeroDivisionError:
            return  "You can't divide by zero!"
    else:
        return 'Wrong pattern'


def calculator(problem):
    action= find_action(problem)
    num1, num2 = problem.split(action)
    result = solving(num1, num2, action)
    return result
    
    

if __name__ == '__main__':
    while True:
        print(calculator(
            input()
        ))