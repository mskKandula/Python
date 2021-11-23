# def canSum(targetSum, arr):
#     if targetSum == 0:
#         return True

#     if targetSum < 0:
#         return False

#     for num in arr:
#         remainder = targetSum - num
        # if (canSum(remainder,arr) == True): ##since we can use a number any Num of times
#             return True

#     return False 

##Time Complexity O(n ^ m), where n = length of arr, m = targetSum
## If you draw a tree there are targetSum levels at worst & arr is constant at all levels
##Space Complexity O(targetSum), Since at worst case target sum stacks are needed  
# print(canSum(13,[5,3,4,7])) #true
# print(canSum(300,[7,14])) #false


def canSum(targetSum, arr,memo=None):
    if memo == None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in arr:
        remainder = targetSum - num
        if (canSum(remainder,arr,memo) == True):
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False 

#Time Complexity O(m * n), Space Complexity O(m)
#where n = length of arr, m = targetSum
print(canSum(13,[5,3,4,7])) #true

print(canSum(300,[7,14])) #false