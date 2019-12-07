#626 too low

#get all numbers in range 246540-787419
initial_n = list(range(246540,787419+1))

print("check that I covered the range: ",min(initial_n),max(initial_n))

# test
# initial_n = [345688]
# initial_n = [111111,223450,123789]

#convert to string
initial_s = [str(x) for x in initial_n]

#find all the numbers in range with at least one consecutive double
mydoubles=[]
for i in initial_s:
	row_char = [x for x in i]
	jcnt=0
	sumlist=[]
	for j in range(len(row_char)-1):
		sumlist.append(row_char[jcnt]==row_char[jcnt+1])
			# print("Yessir",row_char[jcnt])
		jcnt=jcnt+1
	if sumlist.count(True) != 0:
		mydoubles.append(i)
			
		
# print(mydoubles)
print("Number of doubles: ",len(mydoubles))
#of those numbers, find the ones with order never decreasing
finallist=[]
for i in mydoubles:
	row_char = [x for x in i]
	# print(row_char)
	jcnt=0
	sumlist=[]
	for j in range(len(row_char)-1):
		# print(row_char[jcnt],row_char[jcnt+1])
		sumlist.append(row_char[jcnt+1]>=row_char[jcnt])
		jcnt=jcnt+1
	# print(sumlist)
	if sumlist.count(True)==len(row_char)-1:
		finallist.append(i)
		
# print(finallist)
print("Number of doubles never decreasing: ",len(finallist))
# print(finallist)


##### Part 2
##### find strict pairs

import re

# finallist = ['112233','113333','133344','123444','111122','255599']

goodones=[]
for thenum in finallist:
	thisnumber=[]
	for i in range(10):

		#1. for doubles in middle e.g. (*)(!4)(4)(4)(!4)(*)
		pattern1 = "[^" + str(i)+"]"+str(i)+str(i)+"[^" +str(i)+"]"
		#2a. for doubles at start e.g. (4)(4)(!4)(*)(*)(*)
		pattern2 = "^" + str(i)+str(i)+"[^" +str(i)+"]"
		#2b. make sure the last 3 aren't a group of 4
		# actually don't need this because numbers cant decrease
		# pattern2b = re.compile(r"[^" + str(i)+str(i)+str(i)+"]$")
		#3a. 
		pattern3 = "[^" + str(i)+"]"+str(i)+str(i)+"$"
		
		thisnumber.append(re.search("|".join([pattern1,pattern2,pattern3]),thenum) is not None)

	# print(thisnumber)
	if thisnumber.count(True)>0:
		# print("yessir")
		goodones.append(thenum)

# print(finallist)
# print(goodones)	

#check diffs
thediffs = list(set(finallist) - set(goodones))
print(thediffs)

print("Final Answer: ",len(goodones))








