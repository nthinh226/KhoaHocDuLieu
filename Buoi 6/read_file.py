with open("a.txt",mode='r+',encoding='utf-8')as f:
    f.write("1. Công cha như núi Thái Sơn,\n");
    f.write("2. Nghĩa Mẹ như nước trong nguồn chảy ra.\n");
    f.write("3. Một lòng thờ mẹ, kính cha,\n");
    f.write("4. Cho tròn chữ hiếu mới là đạo con.\n");
    
    lines = [];
    for line in f:
        lines.append(line)
        
    print("In dòng thứ 2:\n",lines[1])
    print("Dòng 1 và 4:\n",lines[0], lines[3])
       
f.close();
