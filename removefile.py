



import os 
def remove_file():
 filename=input("enter file name:")+'.txt'
 
 if(filename in os.listdir('data/')):
    os.remove('data/'+filename)
    print("file has been deleted")
 else:
    print("file not exist")
 
remove_file()


