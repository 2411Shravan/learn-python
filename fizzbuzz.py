for i in range(1,51):
    if (i%3==0):
        print(str(i) + ' = fizz')
    if(i%5==0):
        print(str(i)+' = buzz')
    if((i%3==0) and (i%5==0)):
        print(str(i)+ ' = fizz buzz')
