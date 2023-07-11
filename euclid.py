def euclid(a,b):
    if b==0:
        return a, 1, 0
    gcd, x1, y1=euclid(b,a%b)
    x=y1
    y=x1-y1*(a//b)
    return gcd, x, y

euclid(67,12)