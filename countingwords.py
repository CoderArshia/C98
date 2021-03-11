def countwordsfromfile():
    fileName=input("enter the file name")
    numberofWords = 0
    file=open(fileName,'r')
    for line in file:
        words=line.split()
        numberofWords=numberofWords+len(words)
    print("number of words=>",numberofWords)


    









countwordsfromfile()