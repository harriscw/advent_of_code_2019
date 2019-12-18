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

orbits = [x.split(')') for x in raworbits3]

#create graph
G=nx.DiGraph()

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
#look at paths
print("Nodes", mynodes)
mycnt=0
nodecnt=0
start = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
startsec = time.time()
print("Start time: ", start)

for i in range(len(mynodes)):
	nodecnt += 1
	print("Checking node:",mynodes[i],",",nodecnt,"of", len(mynodes),"(",round(100*(nodecnt/len(mynodes)),1),"%)",". Current count:",mycnt,"Time Elapsed:",round((time.time()-startsec)/60,2),"min")
	for j in range(len(mynodes)):
		for path in nx.all_simple_paths(G, source=mynodes[i], target=mynodes[j]):
			if len(path)>0:
				mycnt +=1
print("Start:",start,"End:",time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime()),"Time Elapsed:",round(time.time()-startsec,5))
print(mycnt)
