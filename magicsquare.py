def square_matrix(n):
    sq=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        sq.append(l)
    


    i=n//2
    j=n-1
    num=n*n
    count=1

    while(count<=num):
        if(i==-1 and j==n):
            i=0
            j=n-2
        else:
            if(j==n):
                j=0
            if(i<0):
                i=n-1

        if(sq[i][j]!=0):
            j=j-2
            i=i+1
            continue
        else:
            sq[i][j]=count
            count=count+1
        i=i-1
        j=j+1

    for i in range(n):
        for j in range(n):
            print(sq[i][j],end=" ")
        print()

square_matrix(7)