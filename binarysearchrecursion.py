def bin_search(l,x,start,end):
    if(start==end):
        if(l[start]==x):  
            return start
        else:
            return -1 
    else:
        mid=int((start+end)/2)
        if(l[mid]==x):
            return mid
        elif(l[mid]>x):
            return bin_search(l,x,start,mid-1)
        else:
            return bin_search(l,x,start+1,end)

    
r=[2,3,5,55,56,57,58]
index=bin_search(r,2,0,(len(r)-1))
if(index==-1):
    print("Not found")
else:
    print("Found at position ",index)
