# Exception handling with try and else blocks
def filewriting():
    try:
        fh = open("testfile", "w")
        fh.write("This is my test file for exception handling!!")
    except IOError:
        print("Error: can\'t find file or read data")
    else:
        print("Written content in the file successfully")
        fh.close()


def filewr():
    try:
        fh = open("testfile", "r")
        fh.write("This is my test file for exception handling!!")
    except IOError:
        print("Error: Unable to write data in the file")
    else:
        print("Written content in the file successfully")


def filereading():
    try:
        file = open("PPLassign.txt", "r")
        for line in file:
            print(line)
    except:
        print("File Doesn't exist")


# Exception handling block with try and final block

def try_final():
    try:
        fh = open("testfile", "w")
        fh.write("This file is been opened for writing!!")
    finally:
        print("All work done!!!")


filewriting()
filewr()
filereading()
try_final()

