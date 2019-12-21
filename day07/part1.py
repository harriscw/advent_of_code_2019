

def intcomp(mylist,thephase,theinput,debug="Y"):
	inputhappened=False
	if debug=="Y":
		print("original")
		print(mylist)
	# theinput=8

	i = 0
	while i < len(mylist):
		if debug=="Y":
			print(i)
		instruction = str(mylist[i])
		while len(instruction)<5:
			instruction = str(0)+instruction
		#get instructions
		opcode = instruction[-2:]

		# print("instruction",instruction)
		# print(list(instruction)[:-2])
		if debug=="Y":
			print("opcode",opcode)
		
		# dealing with codes with immediate mode	
		if opcode in ["01","02","05","06","07","08"]:
			#get first parameter mode
			if instruction[2] == "0":
				firstpart = mylist[i+1]
			else:
				firstpart = i+1
			#get second parameter mode
			if instruction[1] == "0":
				secondpart = mylist[i+2]
			else:
				secondpart = i+2
			#get save position
			if instruction[0] == "0":
				savepos = mylist[i+3]
			else:
				savepos = i+3

			# print("firstpart",firstpart)
			# print("secondpart",secondpart)
			# print("savepos",savepos)
				
			if opcode =="01":
				# print("Addition")
				mylist[savepos]=mylist[firstpart]+mylist[secondpart]
				i=i+4
				
			elif opcode =="02":
				# print("Multiplication")
				mylist[savepos]=mylist[firstpart]*mylist[secondpart]
				i=i+4
				
			elif opcode=="05":
				if debug=="Y":
					print("First: ",firstpart,"Second: ",secondpart,"compare value",mylist[firstpart])
				oldval=i
				if mylist[firstpart] != 0:
					i = mylist[secondpart]
				else:
					i=i+3
				if debug=="Y":
					print("what changed: i went from ",oldval,"to",i)
				
					
			elif opcode=="06":
				if mylist[firstpart] == 0:
					i = mylist[secondpart]
				else:
					i=i+3	
				
			elif opcode=="07":
				oldval=mylist[savepos]
				if mylist[firstpart] < mylist[secondpart]:
					mylist[savepos] = 1
				else:
					mylist[savepos] = 0
				i=i+4
				if debug=="Y":
					print("what changed: position ",savepos,"went from ",oldval,"to",mylist[savepos])
				
			elif opcode=="08":
				oldval=mylist[savepos]
				if mylist[firstpart] == mylist[secondpart]:
					mylist[savepos] = 1
				else:
					mylist[savepos] = 0
				i=i+4
				if debug=="Y":
					print("what changed: position ",savepos,"went from ",oldval,"to",mylist[savepos])
				
		#codes without immediate mode
		elif opcode=="03":
			if(inputhappened==False):
				inputhappened=True
				mylist[mylist[i+1]]=thephase
			else:
				mylist[mylist[i+1]]=theinput
			i=i+2
			
		elif opcode=="04":
			if mylist[i+1]>len(mylist):
				if debug=="Y":
					print("Opcode: ",opcode,",input: ",theinput,", Output: ",mylist[i+1])
				return mylist[i+1]
			else:
				if debug=="Y":
					print("Opcode: ",opcode,",input: ",theinput,", Output: ",mylist[mylist[i+1]])
				return mylist[mylist[i+1]]
			i=i+2
		
		elif opcode=="99":
			print("breaking")
			break
		else:
			i = i+1
			
			
			
			
			
			
			
			
			
			
			
			
			
			
# mylist=[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]			
# #phase: 4,3,2,1,0
# intcomp(mylist,thephase=4,theinput=0,debug="N")
# intcomp(mylist,thephase=3,theinput=4,debug="N")
# intcomp(mylist,thephase=2,theinput=43,debug="N")
# intcomp(mylist,thephase=1,theinput=432,debug="N")
# intcomp(mylist,thephase=0,theinput=4321,debug="N")

# mylist=[3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]			
# #phase: 0,1,2,3,4
# intcomp(mylist,thephase=0,theinput=0,debug="N")
# intcomp(mylist,thephase=1,theinput=5,debug="N")
# intcomp(mylist,thephase=2,theinput=54,debug="N")
# intcomp(mylist,thephase=3,theinput=543,debug="N")
# intcomp(mylist,thephase=4,theinput=5432,debug="N")

# mylist=[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]			
# #phase: 1,0,4,3,2
# intcomp(mylist,thephase=1,theinput=0,debug="N")
# intcomp(mylist,thephase=0,theinput=6,debug="N")
# intcomp(mylist,thephase=4,theinput=65,debug="N")
# intcomp(mylist,thephase=3,theinput=652,debug="N")
# print(intcomp(mylist,thephase=2,theinput=6521,debug="N"))


mylist=[3,8,1001,8,10,8,105,1,0,0,21,46,55,76,89,106,187,268,349,430,99999,3,9,101,4,9,9,1002,9,2,9,101,5,9,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]



#generate potential phase numbers
from itertools import permutations 
  
# Get all permutations of [1, 2, 3] 
perm = permutations([0,1,2,3,4]) 
  
# get permutations 
thephases=[]
for i in list(perm): 
    thephases.append(list(i))
print(thephases)

thrusts = []
for phase in thephases:
	a=intcomp(mylist,thephase=phase[0],theinput=0,debug="N")
	b=intcomp(mylist,thephase=phase[1],theinput=a,debug="N")
	c=intcomp(mylist,thephase=phase[2],theinput=b,debug="N")
	d=intcomp(mylist,thephase=phase[3],theinput=c,debug="N")
	e=intcomp(mylist,thephase=phase[4],theinput=d,debug="N")
	thrusts.append(e)

print(max(thrusts))

# mylist=[3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]	
# phase = [1,0,4,3,2]
# a=intcomp(mylist,thephase=phase[0],theinput=0,debug="N")
# b=intcomp(mylist,thephase=phase[1],theinput=a,debug="N")
# c=intcomp(mylist,thephase=phase[2],theinput=b,debug="N")
# d=intcomp(mylist,thephase=phase[3],theinput=c,debug="N")
# e=intcomp(mylist,thephase=phase[4],theinput=d,debug="N")
# print(e)
	
	
	
	





















	