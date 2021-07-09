a=int(input("a="));
b=int(input("b="));
try:
    print(a/b);
except ZeroDivisionError as e:
    print("Error",str(e));
