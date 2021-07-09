email=input("nhap email: ")
if(email[len(email)-10:len(email)]=="@gmail.com" and email[0] !="@"):
    print("email hợp lệ")
else:
    print("email không hợp lệ")
