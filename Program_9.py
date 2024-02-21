#counting words from the file

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = text.split()
            words = [word.strip(",") for word in words]
            num_words = len(words)
            print("The number of words in the file "+file_path+"is: "+str(num_words))
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


file_path =input("Enter the filename : ")+".txt"
count_words(file_path)