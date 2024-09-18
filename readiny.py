# try:
#     file = open("newfile2.txt", "r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     print("Dosya kapandı.")
#     file.close()

file =  open("newfile2.txt", "r", encoding="utf-8")
# content1 = file.read()
# print("içerik1")
# print(content1)
# content2 = file.read()
# print("içerik2")
# print(content2)

# content3 = file.read(10)
# print(content3)

content4 = file.readline()
print(content4)
file.close()