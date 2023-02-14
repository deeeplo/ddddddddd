#regex
import re
#adress

#price
lll = ['$1','$20','$1.99','$10.00','$1500.50','$2,000.99','$1,234,567.89','$1.9','$10,23.4']
#txt = input("price:") 
for pr in lll:
    x=re.search(r'^(\$)(\d*|(\d{1,2}(,\d{3})+)*)(\.\d\d|\d)$',pr)
    if(x):
        print(f"{pr}: found {x}")
    else:
        print(f"{pr}: not found") 
#phone
ll = ['(505) 263-2000','(505)263-2000','505-456-7890','(123)4567890','456-7890','330 263-2000']
#txt = input("phone:") 
for ph in ll:
    x=re.search(r'\(*\d{3}(\)|-)\s*\d{3}-+\d{4}',ph)
    if(x):
        print(f"{ph}: found {x}")
    else:
        print(f"{ph}: not found") 
#email
l = ['nsommer@aa.edu','n.sommer@cs.aa.edu','yippee_skippy@yee-haw.wheeeee','n@sommer@aa.edu','n sommer@aa.edu','nsommer@aa..edu','nsommer@aa.edu-org']
#txt = input("email:") 
for ema in l:
    x=re.search(r'^(\w+|\w+\.\w+)@\w+-*\w+\.(\w+|\w+\.\w+)$',ema)
    if(x):
        print(f"{ema}: found {x}")
    else:
        print(f"{ema}: not found")