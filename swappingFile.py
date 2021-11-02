def swapFileData():
    file1 = input("Please add the name of the fist file")
    file2 = input('Please add the name of the second file')

    f1 = open(file1,"r")
    data_a = f1.read()

    f2 = open(file2,"r")
    data_b = f2.read()

    a1 = open(file1, "w")
    a1.write(data_b)

    a2 = open(file2,"w")
    a2.write(data_a)

swapFileData()
    