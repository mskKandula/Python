# # Either travel to right / downwards by only a single step
# def gridTraveller(rows,cols):
#     if rows==0 or cols==0:
#         return 0
#     elif rows==1 and cols==1:
#         return 1
#     else:
#         # if travel diagonal, then decrease both rows & cols
#         # if we travel downwards, row will be decreased. if right, column will be decreased
#         return gridTraveller((rows-1),cols)+gridTraveller(rows,(cols-1))

# Time complexity O(2^rows+cols), space complexity O(rows+cols)
# print(gridTraveller(2,3))


# Either travel to right / downwards by only a single step
def gridTraveller(rows,cols,memo=None):
    if memo == None:
        memo = {}

    key = str(rows) +','+ str(cols)

    if key in memo :
        return memo[key]
        
    if rows==0 or cols==0:
        return 0
    elif rows==1 and cols==1:
        return 1
    else:
        # if travel diagonal, then decrease both rows & cols
        # if we travel downwards, row will be decreased. if right, column will be decreased
        memo[key]= gridTraveller((rows-1),cols,memo)+gridTraveller(rows,(cols-1),memo)
        return memo[key]

# Time Complexity O(rows * cols), Space Complexity O(rows+cols)
print(gridTraveller(18,18))
