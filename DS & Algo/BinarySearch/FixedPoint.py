def fixedPoint(arr):
    low,high = 0,len(arr)-1

    while low <= high:
        mid = (low+high) //2

        if mid == arr[mid]:
            return mid
        elif mid < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return None

#fixed point is where index == arr [index]
#Time Complexity O(log n)
#where n = length of arr
print(fixedPoint([-2,0,3,5,7,9,12])) #None

print(fixedPoint([-2,0,2,5,7,9,12])) #2