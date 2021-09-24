dict={}
import string
print(string.ascii_letters)
file=open("rewrite.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)

pyt=True
with open("random.txt") as t:
    while (pyt):
        b=t.read(1)
        if not b:
            print("Nothing in the text file :(")
            break
        if b in dict:
            data=dict[b]
        else:
            data=b
        file.write(data)
        print("written")
        pyt=False

file.close()