import math, random
import scipy, pylab

print("Beginning Capitalist model(preferential attachment model) , we are using 1 pass")
print(" ")
dNetwork = {}
iNodes = 1000
iLinks = 0
des=0
add=0
for i in range(iNodes):
	dNetwork[i] = []
	for node in list(dNetwork.values()):
		fThresh = 1.0 / (iLinks + i + 1) * (len(node) + 1)
		if(random.random() <= fThresh):
			node.append(i)
			iLinks += 1

print(" ")
lDegrees = [len(node) for node in list(dNetwork.values())]
x=[i for i in range(iNodes)]
print(lDegrees)
print("Total after capitalist first pass :",iLinks)
avg = sum(lDegrees)/float(iNodes)
print("Average Degree : ",avg)
pylab.figure(1)
pylab.plot(x,lDegrees,'bo')
pylab.xlabel("Node ID")
pylab.ylabel("Node Degree")
pylab.title("Preferential Attachment Capitalist")
print(" ")
j=0
k=3#using 3 passes!!!
print("Beginning Communist model(reverse-preferential attachment) , we are using ",k," passes")

while(j<k):

    lDegrees1 = [len(node) for node in list(dNetwork.values())]
    avg = sum(lDegrees1)/float(iNodes)
    print("Average Degree after pass ",j," : ",avg)
    j+=1
    for i in range(iNodes):
            #avg = sum(lDegrees)/float(iNodes)
            #print "For node ",i,"  avg is ",avg
            for node in list(dNetwork.values()):
                    fThresh = 1.0 / (iLinks + i + 1) * (len(node) + 1)
                    rd=random.random()
                    if(rd <= fThresh):
                            if(node):
                                    node.pop()
                                    iLinks -=1
                                    des +=1
                    if(rd <= (1-fThresh) and len(node)<avg):
                            node.append(i);
                            iLinks += 1
                            add += 1

    print(lDegrees1)

lDegrees1 = [len(node) for node in list(dNetwork.values())]
x=[i for i in range(iNodes)]
#print lDegrees1
print(" ")
print("Total after communist ",k," passes :",iLinks)
print("Total Links Destroyed, after ",k," passes :",des)
print("Total Links Made, after ",k," passes :",add)
print(" ")
print("Please look to other screens for graphs")
pylab.figure(2)
#pylab.plot(x,lDegrees,'bo',x,lDegrees1,'r^')
pylab.plot(x,lDegrees1,'r^')
pylab.xlabel("Node ID")
pylab.ylabel("Node Degree")
pylab.title("Preferential Attachment Communist")
#pylab.hist(lDegrees,100)



pylab.figure(3)
pylab.plot(x,lDegrees,'bo',x,lDegrees1,'r^')
pylab.xlabel("Node ID")
pylab.ylabel("Node Degree")
pylab.title("Preferential Attachment Capitalist/Communist")
pylab.show()
