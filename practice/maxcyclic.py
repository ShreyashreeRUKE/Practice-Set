def maxcyclic(s):
    n=len(s)
    s2=s+s
    seen=set()
    left=0
    maxm=0
    current=0
    for i in range(len(s2)):
        char=s2[i]
        val=ord(char)-ord('a')+1

        if char in seen:
            left_char=s2[i]
            seen.remove(left_char)
            current-=ord(left_char)-ord('a')+1
            left+=1
        
        seen.add(char)
        current+=val

        while i-left+1>n:
            left_char=s2[i]
            seen.remove(left_char)
            current-=ord(left_char)-ord('a')+1
            left+=1
        maxm=max(maxm,current)
    return maxm
    
s=input("Enter string: ")
result=maxcyclic(s)
print("Maximum sum: ",result)
