def is_prime(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    return False

n = int(input("Nhập n= "))
for i in range(n):
    if(is_prime(i)==True):
        print(i)
