# This program is used to demonstrate file handling in python

# Writing into the file
try:
    file = open(
        r"E:\GitHub\Python-programing-files\File Handling\MyData.txt",
        "w",
        encoding="utf-8",
    )
    file.write(
        "\n “Life is a matter of choices, and every choice you make makes you”- John C Maxwell. \n"
    )
finally:
    file.close()

# Reading a file
try:
    file = open(
        r"E:\GitHub\Python-programing-files\File Handling\MyData.txt",
        "r",
        encoding="utf-8",
    )
    print(file.read())
finally:
    file.close()
