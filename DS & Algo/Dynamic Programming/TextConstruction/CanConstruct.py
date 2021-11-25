def canConstruct(target,arr,memo=None):

    if memo == None:
        memo = {}

    if target in memo:
        return memo[target]

    if target == "":
        return True

    for str in arr:
        if (target.find(str) == 0):
            remaindertarget = target[len(str):]
            if canConstruct(remaindertarget,arr,memo) == True:
                memo[target] = True
                return True
                
    memo[target] = False
    return False

#m = length of text, n = length of arr
#Time Complexity O(n * m ), Since we are copying list to append
# Space Complexity O(m * m), Since using the memo, take space
print(canConstruct("abcdef",["ab","abc","cd","def","abcd"]))