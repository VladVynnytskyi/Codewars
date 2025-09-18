def perimeter(n):                           #поганий розвязок займає забагато часу 
    if n != 0:
        result = [1, 1]
        for num in range(0, n - 1):
            result.append(result[num] + result[num + 1])
    else:
        return 4
    return sum(result) * 4

def perimeter(n):
    a, b = 0, 1
    for _ in range(n + 2):
        a, b = b, a + b
    return (b - 1) * 4


# def fib(n):                     
#     a, b = 0, 1

#     for i in range(n+1):
#         if i == 0:
#             yield b 
#         else:
#             a, b = b, a+b
#             yield b
        

# def perimeter(n):
#     return sum(fib(n)) * 4

# def perimeter(n):
#     a, b = 1, 2
#     while n:
#         a, b, n = b, a + b, n - 1
#     return 4 * (b - 1)