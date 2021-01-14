a=list(map(int,input().split(';')))
a.sort(reverse=True)
for i in a:
    print(format(i,',').rjust(9))