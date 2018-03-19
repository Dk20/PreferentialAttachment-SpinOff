# PreferentialAttachment-SpinOff
In link prediction of social network analysis, have chosen algorithm : preferential attachment model("Rich get Richer")
Spin-off : Performing reverse preferential attachment ("poor have a chance to get richer") and and comparing the two models

##Original Preferential attachment model : 
New nodes connect to nodes with the maximum degree(no.of connections), hence "rich get richer " or the capitalist model

##Reverse Preferential Attchment :
New nodes connect to nodes with nodes with minimum degree with a probability, conviniently called the "communist model"

##Test cases:
>	There are 1000 nodes taken.
>	Probabilities[0,1] are generated randomly using random.random()
> For our tweaked preferential attachment model, we have ran it across 1 pass and 3 passes

##RESULTs:
>   The change in degree of each of the 1000 nodes is presented as a list(a python data structure)
>   Average for each pass on each model is calculated , along with the no.of nodes made and destroyed
>	Finally graphs are plotted x: NODE ID , y: NODE DEGREE
>	For each model, blue-dot = capitalist(preferential attach) , red-triangle = communist(reverse-preferentail attchment)

##Evaluation Metrics:
1.	Average Degree distribution
2.	Identifying change in degree in specific nodes after passing through the model
3.	Check if multiple passes through same model gives incorrect values

##Performance Analysis for the identified metrics:
>	Average Degree distribution: The average always increases per pass through our model.
  It is observed in the triple pass test case that:
  At k=1 first pass , average is 1.011
  At k=2 second pass , average is 2.305
  At k=3 third pass, average is 3.153
>	Change in specific nodes(NODE ID’s) are mentioned in circled colour marks given below
>	After multiple passes, k=3, node degree observed by our modified model is still less than iNodes(=1000) ,  node degree < iNodes-1

##OBSERVATION :
We see that in the reverse-preferential attachment model, which we like to call the communist model, 
Nodes with degree less than avg degree have a chance to make more links with other node, and nodes more than avg can only cut down    on the number of nodes they are connected to.


