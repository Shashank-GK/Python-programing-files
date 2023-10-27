# This program is used to demonstrate copying the Binary file in python

try:
    source_file = open(
        r"E:\GitHub\Python-programing-files\File Handling\M340i.jpg", "rb"
    )
    data = source_file.read()

    copy_file = open(
        r"E:\GitHub\Python-programing-files\File Handling\BMW_M340i.jpg", "wb"
    )
    copy_file.write(data)
finally:
    source_file.close()
    copy_file.close()
