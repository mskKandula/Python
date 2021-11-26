def allConstruct(target,arr,memo=None):

    if memo == None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    output=[]

    for str in arr:
        if target.find(str) == 0:
            result = allConstruct(target[len(str):],arr,memo)
            output += [[str] + x for x in result]

    memo[target] = output
    return output


#Time Complexity O(n ^ m * m), Since we are copying list to append
# Space Complexity O(m * m), Since using the memo, take space
#where n = length of arr, m = target
print(allConstruct("abcdef",["a","b","c","e","d","f","abcd","abcdef"]))



