string = "%s dinh"
a = input("Nhập số a: ")

n1 = int( "%s" % a )
n2 = int( "%s%s" % (a,a) )
n3 = int( "%s%s%s" % (a,a,a) )
n4 = int( "%s%s%s%s" % (a,a,a,a) )

print ("Kết quả: ",n1+n2+n3+n4)
