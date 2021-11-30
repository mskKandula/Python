# #iterative
# def basicSearch(target,arr):
#     low,high = 0,len(arr)-1
    
#     while low <= high:
#         mid = (low + high)//2

#         if  arr[mid] == target:
#             return True
#         elif target < arr[mid]:
#             high = mid -1
#         else:
#             low = mid + 1

#     return False


# print(basicSearch(7,[1,3,7,8,12,13,65,100]))


#recursive
def basicSearch(target,arr,low,high):
        if low >= high:
            return False

        mid = (low + high)//2

        if  arr[mid] == target:
            return True
        elif target < arr[mid]:
            return basicSearch(target,arr,low,mid -1) 
        else:
            return basicSearch(target,arr,mid+1,high)

arr = [1,3,7,8,12,13,65,100]
#Time Complexity O(log n)
#where n = length of arr
print(basicSearch(7,arr,0,len(arr)))