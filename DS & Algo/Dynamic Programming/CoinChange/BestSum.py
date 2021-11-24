# def bestSum(targetSum,arr):
   
#     if targetSum == 0:
#         return []

#     if targetSum < 0:
#         return None
        
#     bestCombination = None

#     for num in arr:
#         remainder = targetSum - num
#         remainderResult = bestSum(remainder,arr)

#         if remainderResult != None:
#             remainderResult.append(num)
#             if ((bestCombination == None) or 
#             (len(remainderResult) < len(bestCombination))):
#                 bestCombination = remainderResult

#     return bestCombination

#Time Complexity O(n ^ m * m), Since we are copying list to append
# Space Complexity O(m * m), Since using the list, take space
#where n = length of arr, m = targetSum
# print(bestSum(7,[5,3,4,7]))

# print(bestSum(100,[1,5,10,25]))

def bestSum(targetSum,arr,memo = None):
    if memo == None:
       memo = {}

    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None
        
    bestCombination = None

    for num in arr:
        remainder = targetSum - num
        remainderResult = bestSum(remainder,arr,memo)

        if remainderResult != None:
            combination = remainderResult[:]+[num]
            if (bestCombination == None or len(combination) < len(bestCombination)):
                bestCombination = combination

    memo[targetSum] = bestCombination
    return memo[targetSum]

#Time Complexity O(n * m * m), Since we are copying list to append
# Space Complexity O(m * m), Since using the memo, take space
#where n = length of arr, m = targetSum
print(bestSum(7,[5,3,4,7]))

print(bestSum(100,[1,5,10,25],{}))