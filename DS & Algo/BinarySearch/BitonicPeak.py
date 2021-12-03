def bitonicPeak(arr):
    low,high = 0,len(arr)-1

    while low <= high:
        mid = (low + high)//2

        midLeft = arr[mid-1] if mid-1 >=0 else float("-inf")
        midRight = arr[mid+1] if mid+1 <= high else float("inf")  

        if midLeft < arr[mid] > midRight:
            return arr[mid]
        elif midLeft < arr[mid] < midRight:
            low = mid+1
        else:
            high = mid-1

    return None


print(bitonicPeak([1,2,3,4,5,4,3,2,1])) #5
print(bitonicPeak([1,2,3,4,1])) #4
print(bitonicPeak([1,6,5,4,3,2,1])) #6