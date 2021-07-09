#giải phương trình bậc 2. không sử dụng hàm if
def one(c):
    return "pt vo nghiem";
def two(b,c):
    return -c / b;
def three(a,b,c):
    delta = b * b - 4 * a * c;
    
def test(x):
    switcher = {
        1: one(),
        2: two()
    }
    return switcher.get(x, "nothing")
a=1;
b=2;
c=3;
print(test(1))
    
