def swapfile():
    file1=input("ENTER THE FIRST FILE NAME=")
    file2=input("ENTER THE OTHER FILE NAME=")
    with open(file1,"r") as data1:
        dataA=data1.read()
    with open(file2,"r") as data2:
        dataB=data2.read()
    with open(file1,"w") as A:
        A.write(dataB)
    with open(file2,"w") as B:
        B.write(dataA)
swapfile()