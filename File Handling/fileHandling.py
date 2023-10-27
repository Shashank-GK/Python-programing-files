# This program is used to demonstrate file handling in python

file = open(
    r"E:\GitHub\Python-programing-files\File Handling\File.txt", "r", encoding="utf-8"
)
print(file.read())
file.close()
