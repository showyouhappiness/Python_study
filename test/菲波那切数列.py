"""方法一"""

# def fib(n: int) -> int:
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#     return a % 1000000007
#
#
# class Solution:
#     for i in range(10):
#         print(fib(i), end=', ')


'''方法二'''

# class Solution:
#     def fib(n: int) -> int:
#         a, b = 0, 1
#         for _ in range(n):
#             a, b = b, a + b
#         return a % 1000000007
#
#     for i in range(10):
#         print(fib(i), end=', ')


'''方法三'''

# class Solution:
#     def fib(n: int) -> int:
#         dp = [0, 1]
#         for i in range(2, n + 1):
#             dp.append(dp[i - 1] + dp[i - 2])
#         return dp[n] % 1000000007
#
#     for i in range(0, 21):
#         print(fib(i), end=', ')


'''方法四'''

# def fibonacci(n):
#     a, b = 0, 1
#     for _ in range(n):
#         a, b = b, a + b
#         print(a, end=', ')
# fibonacci(10)


'''方法五-Python官网例子  斐波那契数列直到n'''


# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a + b
#
#
# fib(1000)

def fib(n):  # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
