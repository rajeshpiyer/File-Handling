#Read Entire text file and store in a variable
def storefile(file):
    str=""
    for i in file:
        str+="\n"+i
    return str

def readfile():
    print("\n\n-- Storing Data from myfile.txt to a variable --")
    file = open("myfile.txt","r")
    str = storefile(file)
    print("\n\nAfter storing, the variable looks like : \n\n",str)
    file.close()

readfile()