P = str(input("Write Text: "))
P = P.lower()
output = []
for character in P:
    number = ord(character) - 97
    output.append(int(number))
print("Actual order of string: ",output)

l1 = []
l2 = []
if((len(output)%5) == 4):
    output.append(55)
elif((len(output)%5) == 3):
    output.append(55)
    output.append(55)
elif((len(output)%5) == 2):
    output.append(55)
    output.append(55)
    output.append(55)
elif((len(output)%5) == 1):
    output.append(55)
    output.append(55)
    output.append(55)
    output.append(55)
print("Appended string is: ",output)
j=0

#Encryption
for i in range(len(output)):
	if j==4:
		l2.append(output[i])
		l2[0],l2[1],l2[2],l2[3],l2[4] = l2[1],l2[2],l2[3],l2[4],l2[0]
		l1.append(l2)
		l2=[]
		j=0
	else:
	     l2.append(output[i])
	     j=j+1
	    
print("Encrypted Value is: ",l1)

#Decryption

for i in range(len(l1)):
		l1[i][1],l1[i][2],l1[i][3],l1[i][4],l1[i][0] = l1[i][0],l1[i][1],l1[i][2],l1[i][3],l1[i][4]
print(l1)

		














	
     