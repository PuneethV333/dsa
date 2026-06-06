# Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

def productExceptSelf(arr:list[int]) -> list[int]:
    temp = []
    for i in range(len(arr)):
        res= 1
        for j in range(len(arr)):
            if( i == j):
                continue
            res *= arr[j]


        temp.append(res)
    return res
    
    
    
productExceptSelf([1,2,3,4])