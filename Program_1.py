#Read Entire text file
def printfile(file):
    for i in file:
        print(i)

def readfile():
    file = open("myfile.txt","r")
    printfile(file)
    file.close()

readfile()