def search(nums: list[int], target: int) -> int:
        for i,val in enumerate(nums):
            if val == target:
                return i
        return -1
    
print(search(nums = [3,5,6,0,1,2], target = 4))