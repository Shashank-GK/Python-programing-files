# This program is used to demonstrate file handling in python

file_path = r"E:\GitHub\Python-programing-files\File Handling\File.txt"

with open(file_path, "r", encoding="utf-8") as file:
    print(file.read())
