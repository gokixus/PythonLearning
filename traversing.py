with open("newfile2.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)
    print(file.tell()) 
    print(file.seek(10))
    content2 = file.read()
    print(content2)