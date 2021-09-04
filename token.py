token=0
name=True

while(name):
    token=token+1
    print("Token number ",token," please enter the doctor's cabin.")
    print("Do you wish to continue ? (0/1)")
    n=int(input())
    if(n==0):
        name=False
    else:
        continue
