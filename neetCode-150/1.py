# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.


# eg 1
# Input: nums = [1, 2, 3, 3]
# Output: true
# ------------------------------------------

# eg 2
# Input: nums = [1, 2, 3, 4]
# Output: false
# ------------------------------------------


# approach 1
def hasDuplicate(arr: list[int]) -> bool:
    for i in range(1,len(arr)):
        if(arr[i] == arr[i-1]):
            return True
    return False

print(hasDuplicate([1,2,3,3]))

def hasDuplicate2(arr:list[int]) -> bool:
    withOutDup = set(arr)
    if(len(arr) == len(withOutDup)):
        return False
    return True

print(hasDuplicate2([1,2,3]))
