a=input().split()

b=0
for i in a:
    if i.strip(',.') == 'the':
        b+=1
print(b)