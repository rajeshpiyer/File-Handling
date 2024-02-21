#Write a list to a file
def list_input():
    list1=[]
    ch='y'
    while(ch=='y' or ch=='Y'):
        item=input("Enter the item : ")
        while(not item.isdigit()):
            item=input("Invalid Item!\nEnter the item : ")
        list1.append(int(item))
        ch=input("Add another item?(y/n) : ")
    return list1

def printfile(file):
    file.seek(0)
    for i in file:
        print(i)

def writefile():
    file=open("newfile.txt","w")
    print("Create a list to write into file : ")
    list1 = list_input()
    text=""
    for i in list1:
        text+=str(i)
    file.write(text)
    file.close()
    file=open("newfile.txt","r")
    print("File after writing the list looks like : ")
    printfile(file)
    file.close()

writefile()