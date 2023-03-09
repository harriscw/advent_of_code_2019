#to run this enter this at command line:
#python helloworld.py helloworld.txt

import sys, math

#We're assigning our text file to argfile
#What we are saying here is that argfile contains the string, helloworld.txt
argfile = str(sys.argv[1])
 
#open, read, close the helloworld.txt file
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
mylist=[]
for line in f:
    mylist.append(int(line.strip()))
	

#print(mylist)

newlist = [int(x/3)-2 for x in mylist]
print("answer to part 1",sum(newlist))

newerlist=[]
for i in newlist:
	newval=[i]
	while newval[-1] >=6:#6/3=2 then subtract 2 = 0
		x=int(newval[-1]/3)-2
		newval.append(x)
		
	newerlist.append(sum(newval))
print("answer to part 2",sum(newerlist))

