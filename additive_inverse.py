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
	i = int(i) + k
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

c = ""
c2= []
for i in output2:
	i = int(i) - k
	j = i%26
	j = chr(j+97)
	c2.append(j)
c.join(c2)
print("Decripted Text: ")
print c2	