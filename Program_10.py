def create_alphabet_file(file_path, letters_per_line):
    try:
        with open(file_path, 'w') as file:
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            for i in range(0, len(alphabet), letters_per_line):
                line = alphabet[i:i+letters_per_line] + '\n'
                file.write(line)
            file.close()
        print(f"Alphabet file '{file_path}' created successfully with {letters_per_line} letters per line.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def printfile(file):
    file.seek(0)
    for i in file:
        print(i,end="")

file_path = input("Enter the file name : ")+".txt"
letters_per_line = int(input("Enter number of letters per line : "))
create_alphabet_file(file_path, letters_per_line)
file=open(file_path,"r")
printfile(file)