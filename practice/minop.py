def minop(arr,k):
    rem=arr[0]%k
    for n in arr:
        if n%k!=rem:
            return -1
    new_arr=[n//k for n in arr]
    new_arr.sort()
    med=new_arr[len(new_arr)//2]
    op=0
    for n in new_arr:
           op+=abs(med-n)
    return op
n=int(input("Enter no of elements: "))
arr=list(map(int,input("Enter elements ").split()))
k=int(input("Enter k: "))
result=minop(arr,k)
print("Result: ",result)