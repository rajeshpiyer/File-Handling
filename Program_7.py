#Assess if a file is closed after use

def readfile():
    file = open("myfile.txt","r")
    file.close()
    if file.closed:
        print("The file is closed!")
    else:
        print("The file is still open!")

readfile()
