#Read first n lines of a file

def printfile(file,n):
    for i in file:
        if(n>0):
            print(i)
        n-=1

def readfile():
    file = open("myfile.txt","r")
    n=int(input("Enter how many lines are to be read : "))
    printfile(file,n)
    file.close()

readfile()