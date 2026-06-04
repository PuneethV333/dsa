from collections import Counter

# basics


# int
x = 1

# float
y = 0.1

# string
z = "hello world"

# print
print(x, y, z)
print(type(z))

# operators

# {+,-,*,//,%,**}

print(x / y)


# string

s = "hello"

# len(s)
# s.lower()
# s.capitalize()
# s.upper()
# s.split()
# s.replace()
# s.strip()


s[0]  # 1st alpa.
s[-1]  # last alpa.
s[::-1]  # reversal of string


# List  => can have collection of diff type of var

arr = [1, 2, "str"]

# arr.append(4)
# arr.pop()
# arr.insert()
# arr.remove()
# arr.sort()
# arr.reverse()


# for i in arr:
#     print(i)

r = range(6)

for i in r:
    print(i)


# Tuples

t = {1,2,3,"str"}

# t[0] = 1  => np as tuples are immutable

# Dictionaries {hash map}


mp = {}

mp["a"] = 1
mp["b"] = 1
print(mp)


c = [mp.get("a"),mp.items(),mp.keys(),mp.values()]

print(c)

# set => no dup.

st = set()

st.add(1)
st.remove(1)

i in st


# range 
n = 1
start = 1
end = 9
step = 1
range(n)
range(start,end) 
range(start,end,step) 


# function

def add(a,b) :
    return a+b


# lambda

# lambda x:x*x


# list Comprehensions



# sq = [x*x for x in arr]

# qd = [x*x for x in arr if x == 1]


nums= [1,2,0,1,4,2,3]

# nums.sort()
# n = sorted(nums)

print(nums,n)



cnt = Counter(nums)
# print(cnt)


