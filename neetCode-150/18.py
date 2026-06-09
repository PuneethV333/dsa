def search(nums: list[int], target: int) -> int:
    i, j = 0, len(nums) - 1

    while j >= i:
        mid = i + ((j - i) // 2)
        if nums[mid] > target:
            j = mid -1
        elif nums[mid] < target:
            i = mid + 1
        else:
            return mid


print(search([1, 2, 3, 4, 5], 4))
