# This program is used to demonstrate file handling in python
try:
    file = open(
        r"E:\GitHub\Python-programing-files\File Handling\MyData.txt",
        "r",
        encoding="utf-8",
    )
    print(file.read())
finally:
    file.close()
