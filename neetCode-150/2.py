from collections import Counter

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.


# Input: s = "racecar", t = "carrace"
# Output: true
# ====================================

# Input: s = "jar", t = "jam"
# Output: true
# ====================================

def isAnagram(s:str,t:str) -> bool:
    countT = Counter(t)
    countS = Counter(s)
    return (countS == countT)


def isAnagram2(s:str,t:str) -> bool:
    if(len(s) != len(t)):
        return False
    else:
        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
        if(sorted_s == sorted_t):
            return True
        else:
            return False
        
print(isAnagram2("jam","jar"))
print(isAnagram2("jam","jma"))