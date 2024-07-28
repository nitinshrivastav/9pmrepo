def create_file():
    file_name=input('enter a file name: ')+'.txt'
    file=open('data:'+file_name,'w')
    num=int(input("enter a no: "))
    b=[]
    for i in range(2,num+1):
        a=0
        for j in range(1,i+1):
           if(i%j==0):
             a+=1
        if(a==2):
           b.append(i)
    file.write(str(b)+'\n')
    file.close()
    print("File has been created successfully by Naveen")