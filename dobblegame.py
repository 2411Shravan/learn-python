import string
import random
symbols=[]
symbols=list(string.ascii_letters)
card1=[0]*5
card2=[0]*5
pos1=random.randint(0,4)
pos2=random.randint(0,4)
sames=random.choice(symbols)
symbols.remove(sames)
print(pos1,pos2)
if(pos1==pos2):
  card2[pos1]=sames
  card1[pos1]=sames
else:
  card1[pos1]=sames
  card2[pos2]=sames
  card1[pos2]=random.choice(symbols)
  symbols.remove(card1[pos2])
  card2[pos1]=random.choice(symbols)
  symbols.remove(card2[pos1])
  
i=0

while(i<5):
  if(i!=pos1 and i!=pos2):
    alp=random.choice(symbols)
    symbols.remove(alp)
    alp1=random.choice(symbols)
    symbols.remove(alp1)
    card1[i]=alp
    card2[i]=alp1
    
    
  i=i+1
  
print(card2)
print(card1)
ch=input("Enter the similar character : ")
if(ch==sames):
  print("Right")
else:
  print("Wrong")
    