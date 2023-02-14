f=open("alice.txt","r")
reverse0 = open("reverse0.txt","w") 
reverse1 = open("reverse1.txt","w") 
reverse2 = open("reverse2.txt","w") 

reverse0.write(f.read()[::-1])
reverse0.close()

lines=f.readlines()

for i in reversed(lines):
    reverse1.write(i)
reverse1.close()

for i in lines:
    reverse2.write(i[::-1])
reverse2.close()

f.close()