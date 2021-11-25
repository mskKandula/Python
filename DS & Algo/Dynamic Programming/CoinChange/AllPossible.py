def allPossible(target,arr,memo = None):
    if memo == None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == 0:
        return [[]]

    if target < 0:
        return None
    
    finalResult =[]
    
    for num in arr:
        remainder = target-num
        result = allPossible(remainder,arr,memo)
        if result!=None:
            finalResult+=[[num] + x for x in result]
            
    memo[target] = finalResult
    return finalResult

#Time Complexity O(n ^ m * m), Since we are copying list to append
# Space Complexity O(m * m), Since using the memo, take space
#where n = length of arr, m = target
print(allPossible(7,[5,3,4,7]))