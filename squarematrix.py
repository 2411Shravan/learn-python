def square_matrix(n):
    sq=[]
    k=1
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(k)
            k=k+1
        sq.append(l)
    

    for i in range(n):
        for j in range(n):
            print(sq[i][j],end=" ")
        print()



square_matrix(3)