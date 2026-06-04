# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

def twoSum(arr: list[int], target: int) -> list[int]:
    i,j = 0,1
    
    while i != len(arr)-1:
        while j != len(arr):
            if arr[i]+arr[j] == target:
                return [i,j]
            j += 1
        i += 1
        j = i+1
        

    return []


print(twoSum([2,5,5,11],10))
