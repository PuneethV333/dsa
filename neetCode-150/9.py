def longestConsecutive(nums:list[int]) -> int:
    if(len(nums) == 0):
        return 0
    arr = list(set(nums))

    maxVal = 0
    for i in arr:
        if i-1 not in arr:
            val = 1
            while i+val in arr:
                val += 1
            maxVal = max(val,maxVal)
            
    print(arr)
        
    return maxVal

print(longestConsecutive([0,3,2,5,4,6,1,1]))