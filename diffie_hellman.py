import random
def Alice_to_Bob(g,n):
	x = random.randint(1,99)
	A = (g**x)%n
	t1 = []
	t1.append(A)
	t1.append(x)
	print("A and random number is: ",t1)
	return t1
def Bob_to_Alice(g,n):
	y = random.randint(1,99)
	B = (g**y)%n
	t2 = []
	t2.append(B)
	t2.append(y)
	print("B and random number is: ",t2)
	return t2
def Bob_from_Alice(A,y,n):
	k2 = (A**y)%n
	print('k2 : ',k2 )
def Alice_from_Bob(B,x,n):
	k1 = (B**x)%n
	print('k1 : ',k1)
		
g = int(input('G : '))
n = int(input('N : '))	
t1 = Alice_to_Bob(g,n)
t2 = Bob_to_Alice(g,n)
Bob_from_Alice(t1[0],t2[1],n)		
Alice_from_Bob(t2[0],t1[1],n)	
