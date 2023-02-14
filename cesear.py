import re

def decrypt(string,key):
    dString = ""
    dList = []
    try:
        key=int(key)
        if key > 25:
            key = key-26
    except:
        key = -1
        print("Unknown key, brute forcing")
    if key !=-1:
        for i in string:
            if i != " ":
                asci = ord(i)-key
                if i.isupper():
                    if asci < 65 :
                        asci = asci +26
                else:
                    if asci < 97 :
                        asci = asci + 26
                dString+=chr(asci)
            else:
                dString+=" "
        return dString
    else:
        for j in range(1,25):
            key = j
            for i in string:
                if i != " ":
                    asci = ord(i)-key
                    if i.isupper():
                        if asci < 65 :
                            asci = asci +26
                    else:
                        if asci < 97 :
                            asci = asci + 26
                    dString+=chr(asci)
                else:
                    dString+=" "
            dList.append(dString + f" key: {j}")
            dString = ""
    return dList

def encrypt(string,key=-1):
    eString = ""
    try:
        key=int(key)
        if key >25:
            key = key-26
    except:
        key = -1
        return("Uknown key")
    if key !=-1:
        for i in string:
            if i != " ":
                asci = ord(i)+key
                if i.isupper():            
                    if asci > 90:
                        asci = asci - 90 +63
                else:
                    if asci > 122:
                        asci = asci - 122 + 96
                eString+=chr(asci)
            else:
                eString+=" "
    return eString
def main():
    fp=open(r'1000.txt', 'r') #https://gist.githubusercontent.com/deekayen/4148741/raw/98d35708fa344717d8eee15d11987de6c8e26d7d/1-1000.txt
    for i in range(1,6):
        f=open(f"cipher{i}.txt", "r")
        lines = f.readlines()
        res = re.sub(r'[^\d]', '', lines[1])
        print(f"Number {i}:")
        if lines[0] == "decrypt\n":
            try:
                int(res)
                print(decrypt(lines[2],res))
            except: #sorts by most probable deciphered string(need a bigger wordlist to be more accurate)
                listy = decrypt(lines[2],res)
                sortedlist = [0] * len(listy)
                contents = fp.read()
                for i in range(len(listy)):
                    dd = listy[i].split()
                    for j in dd:
                        if j in contents:
                            sortedlist[i] +=1
                listy = [x for _,x in sorted(zip(sortedlist,listy),reverse=True)] #zips the lists then sorts due to order in sortedlist
                #(stole idea off python docs )
                for i in listy:
                    print(i)  
        if lines[0] == "encrypt\n":
            print(lines[2])
            print(encrypt(lines[2],res))
            print(decrypt(encrypt(lines[2],res),res))
    fp.close()
    f.close()
if __name__ == "__main__":
    main()
