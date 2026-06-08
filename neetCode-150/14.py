def trap(h: list[int]) -> int:
    water = 0
    for i in range(len(h)):
        leftMax,rightMax = 0,0
        for l in range(i+1):  # noqa: E741
            leftMax = max(h[l],leftMax)
        
        for r in range(i,len(h)):
            rightMax = max(h[r],rightMax)
            
        water += min(leftMax,rightMax)-h[i]
        
    return water