def tower(n,a,b,c):

    if n==0:
        return

    tower(n-1,a,c,b)

    print(a,"to",c)

    tower(n-1,b,a,c)