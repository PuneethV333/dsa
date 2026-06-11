def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    temp = nums1 + nums2

    temp.sort()

    if len(temp) % 2 == 1:
        return temp[len(temp) // 2]
    else:
        return (temp[int(len(temp) / 2) - 1] + temp[int(len(temp) / 2)]) / 2

    # for i,j in zip(nums1,nums2):


print(findMedianSortedArrays(nums1=[1, 3], nums2=[2, 4]))
