raworbits1 = [
"A)B",
"B)C",
"B)D",
"D)E"]

raworbits2 = [
"COM)B",
"B)C",
"C)D",
"D)E",
"E)F",
"B)G",
"G)H",
"D)I",
"E)J",
"J)K",
"K)L"
]


import csv

file=open("input.csv", "rt")
reader = csv.reader(file)
raworbits3 = []
for line in reader:
	for i in range(len(line)):
		raworbits3.append(line[i])



def myfunc(orbits):

	orbits = [x.split(')') for x in orbits]
	print(orbits)

	tfind=True
	segments = orbits
	mycnt=0

	tflist=[]
	#iterate over each orbit, this is initialized with the original list
	for i in orbits:
		mycnt=mycnt+1
		#print the inner loop count every 1000 loops
		if mycnt%1000==0:
			print(mycnt)
		#iterate over each existing segment to see if there's another segment that can attach to items
		#this is initialized to original orbits
		for j in segments:
			# if the segment can grow, append it to the list of existing segments
			if i[-1]==j[0] and i+j not in segments:
				segments.append(i+j)
				tflist.append(True)
	#if no segments grew then stop the while loop
		if len(tflist)==0:
			break

	#Output length
	print("FINAL ",len(segments))
	
		


	
myfunc(orbits=raworbits3)

