def factorial(x):
    result = 1
    if x > 0:
        result = x * factorial(x -1)
    return result
number = int(input())
print(factorial(number))