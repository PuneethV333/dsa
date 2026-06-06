# Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

class Solution:
    def encode(self,strs:list[str]) -> str:
        st = ""
        for s in strs:
            for i in s:
                st += s
            st += f"#{len(s)}"
        return st
    
    
    def decode(self,s:str) -> list[str]:
        
        return []
    
def encode(strs:list[str]) -> str:
    s = ""
    for i in strs:
        s += str(len(i)) + "#" + i
    return s

def decode(s):
    res = []
    i,j = 0,0

    while i != len(s):
        if(s[j] != "#"):
            j += 1
        else:
            a = s[i:j]
            print(i,j,a)
            count = int(a)
            temp = s[j+1:j+count+1]
            res.append(temp)
            i = j+count+1
            j = i
            
    return res

# s = encode([""])
# print(s)
# # s = encode(["hello","world"])
# # print(type(s))
# print(decode(s))