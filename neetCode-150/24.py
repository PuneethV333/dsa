import math
def minEatingSpeed(piles: list[int], h: int) -> int:
    l,r = 1,max(piles)  # noqa: E741
    res = r
    
    while r >= l:
        k = (l+r)//2
        
        total = 0
        for p in piles:
            total+=math.ceil(float(p)/k)
            
        if total <= h:
            res = k
            r = k-1
        else:
            l = k+1  # noqa: E741
        
    return res
        

print(minEatingSpeed(piles = [25,10,23,4], h = 4))