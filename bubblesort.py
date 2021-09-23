def bub(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if(arr[j]>arr[j+1]):
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp


arra=[1,34,2,3,56,4,3,56]
bub(arra)
for i in arra:
    print(i)