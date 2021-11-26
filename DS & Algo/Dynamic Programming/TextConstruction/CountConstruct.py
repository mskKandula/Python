def countConstruct (target,arr,memo =None):

    if memo == None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return 1

    finalCount = 0

    for str in arr:
        if target.find(str)==0:
            if countConstruct(target[len(str):],arr) == 1:
                finalCount+=1
    
    memo[target] = finalCount
    return memo[target]

#m = length of target string, n = length of arr
#Time Complexity O(n * m), Since we are copying list to append
# Space Complexity O(m * m), Since using the memo, take space
print(countConstruct("abcdef",["a","b","c","e","d","f","abcd","abcdef"]))
