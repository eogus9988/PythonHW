i = int(input())
for a in range(i):
    for b in reversed(range(i)):
        if b > a:
            print(' ',end='')
        else:
            print('*',end='')
    for b in range(i):
        if b < a:
            print('*', end='')
    print()