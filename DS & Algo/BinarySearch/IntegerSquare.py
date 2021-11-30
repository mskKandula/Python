def integerSquare(num):
    low,high = 0,num

    while low<=high:
        mid = low+high//2

        midSquared = mid * mid

        if midSquared > num:
            high = mid -1
        elif midSquared <= num:
            low = mid + 1
        
    return low-1

print(integerSquare(12))
print(integerSquare(300))