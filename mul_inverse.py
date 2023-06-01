input = raw_input('Write Text: ')
input = input.lower()
output = []
output2 = []
for character in input:
    number = ord(character) - 97
    output.append(int(number))
print output

k = int(raw_input('Enter the value of K: '))
c = ""
c2= []
for i in output:
	i = int(i) * k
	j = i%26
	j = chr(j+97)
	c2.append(j)
c.join(c2)
print("Encripted Text: ")
print c2

# Decription Part
for character in c2:
    number = ord(character) - 97
    output2.append(int(number))
print output2

b = k 
n =26

r1 = n
r2 = b
t1 = 0
t2 = 1
c3=[]
while r2>0:
	q = r1/r2
	r = r1-q*r2
	r1 = r2
	r2 = r
	t = t1 - q*t2
	t1 = t2
	t2 = t
if r1 == 1:
	b_inv = t1

for i in output2:
	i = int(i) * b_inv
	j = i%26
	j = chr(j+97)
	c3.append(j)
c.join(c3)
print("Decripted Text: ")
print c3
