import re
f = open("alice.txt","r")
file = open("uniq.txt","w")
#or print(f.read())
#or print(f.readlines())
words = []
for lines in f:
    x=lines.split()
    for i in x:
        words.append(i)
unique_words = []
for j in words:
    res = re.sub(r'[^\w\s-]', '', j)
    if res.find("-")>-1 and res[len(res)-1] != "-" and res.find("--") == -1:
        if res[res.find("-")+1:].lower() not in [x.lower() for x in unique_words]:
            unique_words.append(res[res.find("-")+1:])
        if res[:res.find("-")].lower() not in [x.lower() for x in unique_words]:
            unique_words.append(res[:res.find("-")])
    elif res.find("--") > -1 and res[len(res)-1] != "--":
        if res[res.find("--")+2:].lower() not in [x.lower() for x in unique_words]:
            unique_words.append(res[res.find("--")+2:])
        if res[:res.find("--")].lower() not in [x.lower() for x in unique_words]:
            unique_words.append(res[:res.find("--")])
    elif res.lower() not in [x.lower() for x in unique_words]:
        unique_words.append(res)
    # if need to keep punctuation can make new list and store res.lower in it then check through that instaed of unique words.lower
unique_words.sort()
for i in unique_words:
    file.write(i.replace(" ", "") + " ") # this doenst replace the first space in the test file not sure why?
file.close()
f.close()