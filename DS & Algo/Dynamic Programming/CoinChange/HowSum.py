# def howSum(targetSum, arr):
#     if targetSum == 0:
#         return []

#     if targetSum < 0:
#         return None    

#     for num in arr:
#         remainder = targetSum - num
#         remainderResult = howSum(remainder,arr)
#         if remainderResult !=None:
#             remainderResult.append(num)
#             return remainderResult

#     return None

##Time Complexity O(n ^ m * m), Space Complexity O(m)
##where n = length of arr, m = targetSum
# print(howSum(7,[5,3,7,4]))

# print(howSum(300,[7,14]))


def howSum(targetSum, arr,memo=None):
    if memo == None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None    

    for num in arr:
        remainder = targetSum - num
        remainderResult = howSum(remainder,arr,memo)
        if remainderResult !=None:
            result = remainderResult[:]+[num]
            memo[targetSum] = result
            return result

    memo[targetSum] = None
    return None

#Time Complexity O(n * m * m), Space Complexity O(m * m)
#where n = length of arr, m = targetSum
#Since using the memo object, take space
print(howSum(8,[2,5,3,4,7]))

print(howSum(7,[5,3,7,4]))

print(howSum(300,[7,14]))