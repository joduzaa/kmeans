# =============== Task 12 ===============

# <<<<< Compulsory Task 1 >>>>>

import math
import csv
import random
import matplotlib.pyplot as plt

#K-Means clustering implementation

#Some hints on how to start have been added to this file.
#You will have to add more code that just the hints provided here for the full implementation.

# ====
# Define a function that computes the distance between two data points

def Distance(x1,y1,x2,y2):
	x = math.pow((x1-x2),2) 
	y =	math.pow((y1-y2),2)
	d = math.sqrt(x+y)
	return d

# ====
# Define a function that reads data in from the csv files  HINT: http://docs.python.org/2/library/csv.html

def Data_Input(file_name):
	data = []
	with open(file_name, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)
	return data

# ====
# Write the initialisation procedure

print "This is a programme to create clusters using K-Means >>>>>"
print ""
File_Num = int(raw_input("Choose (1) for 1953 data or (2) for 2008 data: "))

if File_Num == 1:
	File_Name = "data1953.csv"
elif File_Num == 2:
	File_Name = "data2008.csv"

Data = Data_Input(File_Name)

Country = [item[0] for item in Data]
Country_Names = Country[1:]

Birth_Rate = [item[1] for item in Data]
Birth_Rate_Nums = [float(element) for element in Birth_Rate[1:]]

Life_Exp = [item[2] for item in Data]
Life_Exp_Nums = [float(element) for element in Life_Exp[1:]]

print ""
Cluster_Num = int(raw_input("Choose the number of clusters to divide the data: "))

Int_Country = random.sample(Country_Names,Cluster_Num)

N = []
for i in range(0,Cluster_Num):
	N.append(Country_Names.index(Int_Country[i]))

B = []
for i in range(0,Cluster_Num):
	B.append(Birth_Rate_Nums[N[i]])

L = []
for i in range(0,Cluster_Num):
	L.append(Life_Exp_Nums[N[i]])

# ====
# Implement the k-means algorithm, using appropriate looping

print ""
Iter_Num = int(raw_input("Choose the number of iterations to run: "))

for i in range(0,Iter_Num):

	Cluster = {}
	
	for item in Country_Names:
		D = []
		i = Country_Names.index(item)
		for k in range(0,len(Int_Country)):
			D.append(Distance(Birth_Rate_Nums[i],Life_Exp_Nums[i],B[k],L[k]))
		D_Min = min(D)
		Cluster[item] = [D.index(D_Min), Birth_Rate_Nums[i], Life_Exp_Nums[i]]
	
	B=[]
	L=[]
	C=[]
			
	for n in range(0,Cluster_Num):
		L_sum = 0
		B_sum = 0
		count = 0
		for v, k in Cluster.items():
			if k[0] == n:
				count = 1 + count
				B_sum = k[1] + B_sum
				L_sum = k[2] + L_sum
		C.append(count)
		B.append(B_sum/count)
		L.append(L_sum/count)

# ====
# Print out the results

print ""
for i in range(0,len(C)):
	print "Number of countries in Cluster " + str(i + 1) + ": " + str(C[i])

print ""
for i in range(0,len(L)):
	print "The mean Life Expectancy in Cluster " + str(i + 1) + ": " + str(L[i])

print ""	
for i in range(0,len(B)):
	print "The mean Birth Rate in Cluster " + str(i + 1) + ": " + str(B[i])

for n in range(0,Cluster_Num):
	print ""
	print "The Countries in Cluster " + str(n + 1) + ": "
	for v, k in Cluster.items():
		if k[0] == n:
			print v

#Cluster1_B = []
#Cluster1_L = []	
#Cluster2_B = []
#Cluster2_L = []
#Cluster3_B = []
#Cluster3_L = []

#for v, k in Cluster.items():
	#if k[0] == 0:
		#Cluster1_B.append(k[1])
		#Cluster1_L.append(k[2])	

#for v, k in Cluster.items():
	#if k[0] == 1:
		#Cluster2_B.append(k[1])
		#Cluster2_L.append(k[2])

#for v, k in Cluster.items():
	#if k[0] == 2:
		#Cluster3_B.append(k[1])
		#Cluster3_L.append(k[2])

#plt.xlabel('Birth Rate (per 1000)')
#plt.ylabel('Life Expectancy')
#plt.title('Graph of K-Means Clustering')
#plt.plot(Cluster1_B, Cluster1_L, 'ro')
#plt.plot(Cluster2_B, Cluster2_L, 'go')
#plt.plot(Cluster3_B, Cluster3_L, 'bo')
#plt.axis([0, 60, 0, 90])
#plt.grid(True)
#plt.show()
