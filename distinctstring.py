def findLongest(s):
    maxlen = 0
    s=input()
    longest = ""
    for i in range(0,len(s)):
        subs = s[i:]
        chars = set()
        for j,c in enumerate(subs):
            if c in chars:
                break
            else:
                chars.add(c)
        else:
            j+=1
        if j>maxlen:
            maxlen=j
            longest=s[i:i+j]
    return longest
print(len(findLongest(str)))
