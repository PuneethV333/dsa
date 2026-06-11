def findMin(nums: list[int]) -> int:
    minVal = nums[0]
    for i in nums:
        minVal = min(minVal,i)

    return minVal