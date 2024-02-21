#Append text toa file
def writefile(file,txt):
    file.write(txt)

def printfile(file):
    file.seek(0)
    for i in file:
        print(i)

def appendfile():
    file = open("myfile.txt","a")
    txt=input("Enter the text to be appended to the file : ")
    writefile(file,txt)
    file.close()
    print("Appended Text : ",txt)
    print("Whole file after appending looks like : ")
    file = open("myfile.txt","r")
    printfile(file)
    file.close()

appendfile()