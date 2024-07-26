def rename_file():
    directory = "e:"  # Define the directory where the files are located

    name = input("Enter the file name: ") + ".txt"
    if name in os.listdir(directory):
        name2 = input("Enter the new file name: ") + ".txt"
        os.rename(os.path.join(directory, name), os.path.join(directory, name2))
        print("Your file name has been changed")
    else:
        print("File not found")

rename()
