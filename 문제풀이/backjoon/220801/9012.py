for _ in range(int(input())):
    gh = input()
    stack = []
    for g in gh:
        if g == '(':
            stack.append('(')
        elif g == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if len(stack) > 0:
            print('NO')
        else:
            print('YES')