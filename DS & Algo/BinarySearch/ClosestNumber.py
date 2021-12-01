def closestNum(target,arr):
    low,high =0,len(arr)-1
    minMid,close = float("inf"),None

    while low <= high:
        mid = (low + high) //2

        if arr[mid] == target:
            return target

        if mid+1 < len(arr):
            midRight = abs(arr[mid+1] - target)
            
        if mid-1 > 0:
            midLeft = abs(arr[mid-1] - target)

        if midRight>midLeft:
            minMid = midLeft
            close = arr[mid-1]
        else:
            minMid = midRight
            close = midLeft

        if target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return close 
#Time Complexity O(log n)
#where n = length of arr
print(closestNum(9,[1,2,4,7,9,12,16,21,27]))
