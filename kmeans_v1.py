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

def Data_Input(x):
	data = []
	with open(x, 'rb') as csvfile:
		reader = csv.reader(csvfile)
		for row in reader:
			data.append(row)
	return data

# ====
# Write the initialisation procedure

data = Data_Input('data2008.csv')

Country = [item[0] for item in data]
Country_Names = Country[1:]

Birth_Rate = [item[1] for item in data]
Birth_Rate_Nums = [float(element) for element in Birth_Rate[1:]]

Life_Exp = [item[2] for item in data]
Life_Exp_Nums = [float(element) for element in Life_Exp[1:]]

Int_Country = random.sample(Country_Names,3)

C1 = Country_Names.index(Int_Country[0])
C2 = Country_Names.index(Int_Country[1])
C3 = Country_Names.index(Int_Country[2])

B1 = Birth_Rate_Nums[C1]
B2 = Birth_Rate_Nums[C2]
B3 = Birth_Rate_Nums[C3]

L1 = Life_Exp_Nums[C1]
L2 = Life_Exp_Nums[C2]
L3 = Life_Exp_Nums[C3] 

# ====
# Implement the k-means algorithm, using appropriate looping

for i in range(0,100):
	Cluster1_N = []
	Cluster1_B = []
	Cluster1_L = []
	
	Cluster2_N = []
	Cluster2_B = []
	Cluster2_L = []
	
	Cluster3_N = []
	Cluster3_B = []
	Cluster3_L = []
	
	for i in range (0,len(Country_Names)):
		D1 = Distance(Birth_Rate_Nums[i],Life_Exp_Nums[i],B1,L1)
		D2 = Distance(Birth_Rate_Nums[i],Life_Exp_Nums[i],B2,L2)
		D3 = Distance(Birth_Rate_Nums[i],Life_Exp_Nums[i],B3,L3)
		D = [D1, D2, D3]
		D_min = min(D)
		if D_min == D1:
			Cluster1_N.append(Country_Names[i])
			Cluster1_B.append(Birth_Rate_Nums[i])
			Cluster1_L.append(Life_Exp_Nums[i])
		elif D_min == D2:
			Cluster2_N.append(Country_Names[i])
			Cluster2_B.append(Birth_Rate_Nums[i])
			Cluster2_L.append(Life_Exp_Nums[i])
		elif D_min == D3:
			Cluster3_N.append(Country_Names[i])
			Cluster3_B.append(Birth_Rate_Nums[i])
			Cluster3_L.append(Life_Exp_Nums[i])
			
	Cluster1 = [Cluster1_N, Cluster1_B, Cluster1_L]
	Cluster2 = [Cluster2_N, Cluster2_B, Cluster2_L]
	Cluster3 = [Cluster3_N, Cluster3_B, Cluster3_L]
	
	Bm1 = sum(Cluster1_B)/len(Cluster1_B)
	Lm1 = sum(Cluster1_L)/len(Cluster1_L)
	
	Bm2 = sum(Cluster2_B)/len(Cluster2_B)
	Lm2 = sum(Cluster2_L)/len(Cluster2_L)
	
	Bm3 = sum(Cluster3_B)/len(Cluster3_B)
	Lm3 = sum(Cluster3_L)/len(Cluster3_L)
			
	B1 = Bm1
	L1 = Lm1
	
	B2 = Bm2
	L2 = Lm1
	
	B3 = Bm3
	L3 = Lm1

# ====
# Print out the results

print "Countries in Cluster 1:"
print Cluster1_N
print ""
print "Countries in Cluster 2:"
print Cluster2_N
print ""
print "Countries in Cluster 3:"
print Cluster3_N
print ""
print "Number of countries in Cluster 1: " + str(len(Cluster1_N))
print "Number of countries in Cluster 2: " + str(len(Cluster2_N))
print "Number of countries in Cluster 3: " + str(len(Cluster3_N))
print ""
print "The mean Life Expectancy in Cluster 1: " + str(Lm1)
print "The mean Life Expectancy in Cluster 2: " + str(Lm2)
print "The mean Life Expectancy in Cluster 3: " + str(Lm3)
print ""
print "The mean Birth Rate in Cluster 1: " + str(Bm1)
print "The mean Birth Rate in Cluster 2: " + str(Bm2)
print "The mean Birth Rate in Cluster 3: " + str(Bm3)

plt.xlabel('Birth Rate (per 1000)')
plt.ylabel('Life Expectancy')
plt.title('Graph of K-Means Clustering')
plt.plot(Cluster1_B, Cluster1_L, 'ro')
plt.plot(Cluster2_B, Cluster2_L, 'go')
plt.plot(Cluster3_B, Cluster3_L, 'bo')
plt.axis([0, 60, 0, 90])
plt.grid(True)
plt.show()
