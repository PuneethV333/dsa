def maxArea(heights: list[int]) -> int:
    maxVal = 0
    i,j = 0,len(heights)-1
    while j > i:
        maxVal = max(maxVal,(min(heights[i],heights[j])*(j-i)))
        if(heights[i] > heights[j]):
            j-= 1
        else:
            i+=1
    return maxVal

print(maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6]))
        