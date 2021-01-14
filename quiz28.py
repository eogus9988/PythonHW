with open('words.txt','r') as file:
    a=file.readlines()
for i in a:
    i = i.strip('\n')
    if i == i[::-1]:
        print(i)