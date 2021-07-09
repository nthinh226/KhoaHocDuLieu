def sum(a, b):
    return a+b;

def giaithua(n):
    if (n == 0):
        return 1;
    else:
        return n*giaithua(n-1);
