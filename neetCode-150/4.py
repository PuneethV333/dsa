# from collections import Counter

def groupAnagrams(strs:list[str]) -> list[list[str]]:
    mp={}
    for str in strs:
        temp = "".join(sorted(str))
        x = mp.get(temp,[])
        x.append(str)
        mp[temp] = x
    return list(mp.values())
    
x = groupAnagrams(["act","pots","tops","cat","stop","hat"])
print(x)