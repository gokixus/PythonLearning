# with open("newfile.txt", "r+", encoding="utf-8") as file:
#     # file.write("\nEmel Turan") #sayfa sonunda günceller
#     content = file.read()
#     content = "Ali Çağrı\n" + content #sayfa başında günceller
#     file.seek(0)
#     file.write(content)
# with open("newfile.txt", "r", encoding="utf-8") as file:
#     print(file.read())
    
    
with open("newfile.txt", "r+", encoding="utf-8") as file:
    list = file.readlines()
    list.insert(1, "Yılmaz Aygün\n")
    file.seek(0)
    file.writelines(list)
    
with open("newfile.txt", "r", encoding="utf-8") as file:
    print(file.read())
    