# def nthFibonacciNum(n=8):
#     if n<=2:
#         return 1
#     else:
#         return nthFibonacciNum(n-1) + nthFibonacciNum(n-2)

# # Time Complexity is O(2^n), Tree nodes are increasing in the order of 2*2*2.. = 2^n (order of nodes increasing in each level)
# # Space Complexity is O(n), since at any time only n recursive calls are made so n stacks (height of the recursive tree)
# print(nthFibonacciNum())
# print(nthFibonacciNum(22))
# print(nthFibonacciNum(23))


# Memoization
def nthFibonacciNum(n=8,memo=None):
    if memo == None:
        memo={}

    if n in memo:
        return memo[n]
    elif n<=2:
        return 1
    else:
        # add memo as second argument, passing the same memo dict else new memo dict will be created each time
        memo[n] = nthFibonacciNum(n-1,memo) + nthFibonacciNum(n-2,memo)
        return memo[n]

# Time Complexity is O(2*n) = O(n), Tree nodes are constant i.e: 2*n (order of nodes constant in each level)
# Space Complexity is O(n), since at any time only n recursive calls are made so n stacks (height of the recursive tree)
print(nthFibonacciNum())
print(nthFibonacciNum(22))
print(nthFibonacciNum(50))