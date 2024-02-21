#Copy contentsof a file to another file
def copyfile(file1,file2):
    str=""
    for i in file1:
        str+="\n"+i
    file2.write(str)

def printfile(file):
    file.seek(0)
    for i in file:
        print(i)

def readfile():
    print("\n\n-- Storing Data from myfile.txt to a variable --")
    file1 = open("myfile.txt","r")
    filename = input("Enter a new file name : ")
    file2 = open(filename+".txt","w")
    copyfile(file1,file2)
    file2.close()
    print("\n\nNew file looks like : \n\n")
    file2 = open(filename+".txt","r")
    printfile(file2)
    file1.close()
    file2.close()

readfile()