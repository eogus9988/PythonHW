with open('words.txt','r') as file:
    a=file.readline()
    b=a.split()
    for i in b:
        if 'c' in i:
            print(i.strip(',.'))