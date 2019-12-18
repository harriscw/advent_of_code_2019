#this took 2 hours

import networkx as nx
import csv
import time

file=open("input.csv", "rt")
reader = csv.reader(file)
raworbits3 = []
for line in reader:
	for i in range(len(line)):
		raworbits3.append(line[i])


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

def part2(data,source,target):

	orbits = [x.split(')') for x in data]

	#create graph
	G=nx.Graph()

	#get unique nodes & add to graph
	# print(orbits)
	mynodes=[]
	for i in orbits:
		mynodes.append(i[0])
		mynodes.append(i[1])


	mynodes=list(set(mynodes))
	G.add_nodes_from(mynodes)

	#add edges
	tupelized = []
	for i in orbits:
		tupelized.append((i[0],i[1]))

	G.add_edges_from(tupelized)

	mynodes=sorted(mynodes)

	# print("B In Edges", G.edges("B"))
	# print(nx.shortest_path_length(G, source="B", target="E"))

	#get source orbits

	sourceorbits=G.edges(source)
	sourceorbits=list(sum(sourceorbits, ()))
	sourceorbits=[x for x in sourceorbits if x != source]
	print("ORBITS FOR SOURCE:",source,sourceorbits)

	#get target orbits

	targetorbits=G.edges(target)
	targetorbits=list(sum(targetorbits, ()))
	targetorbits=[x for x in targetorbits if x != target]
	print("ORBITS FOR TARGET:",target,targetorbits)
	
	
	#Now find minimum distance from any source to any target
	pathlens=[]
	for s in sourceorbits:
		for t in targetorbits:
			x = nx.shortest_path(G,source=s,target=t)
			transfers=len(x)-1
			print("Source:",s,"Target:",t,", Shortest Path:",x,",Transfers: ",transfers)
			pathlens.append(transfers)
	print("Min transfers: ",min(pathlens))	

part2(data=raworbits1,source="B",target="C")
part2(data=raworbits2,source="B",target="E")
part2(data=raworbits3,source="YOU",target="SAN")


	# mycnt=0
	# nodecnt=0
	# start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
	# startsec = time.time()
	# print("Start time: ", start)

	# for i in range(len(mynodes)):
		# nodecnt += 1
		# print("Checking node:",mynodes[i],",",nodecnt,"of", len(mynodes),"(",round(100*(nodecnt/len(mynodes)),1),"%)",". Current count:",mycnt,"Time Elapsed:",round((time.time()-startsec)/60,2),"min")
		# for j in range(len(mynodes)):
			# for path in nx.all_simple_paths(G, source=mynodes[i], target=mynodes[j]):
				# if len(path)>0:
					# mycnt +=1
	# print("Start:",start,"End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),"Time Elapsed:",round(time.time()-startsec,5))
	# print(mycnt)
