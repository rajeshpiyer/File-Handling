import random

def filelength(file):
    length=0
    for i in file:
        length+=1
    return length

def readrandom(file):
    length = filelength(file)
    file.seek(0)
    num = random.randint(1,length)
    counter=1
    print("Line number :",num)
    for i in file:
        if counter==num:
            print(i)
            break
        counter+=1

def file_input():
    file = open("myfile.txt","r")
    ch='y'
    while(ch=='y' or ch=='Y'):
        file.seek(0)
        readrandom(file)
        ch=input("Do you want to read another random line?(y/n)")
    file.close()

file_input()

