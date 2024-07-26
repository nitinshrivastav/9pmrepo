def create_file():
    name=input("enter your file name wich you want to create")+".txt"
    file=open("d:"+name,w)
    file.write("hello"+name)
    file.close
    print("file has been created")