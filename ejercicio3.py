def peakIndexInMountainArray(arr):
    for i in range(len(arr)):
        continuar = True
        for j in range(i):
            if arr[i] <= arr[j]:
                continuar = False
                break
        
        if not continuar:
            continue
        
        for j in range(i+1, len(arr)):
            if arr[j] >= arr[i]:
                continuar = False
                break
        
        if continuar:
            return i

print(peakIndexInMountainArray([5,1,2]))  # Output: 1


