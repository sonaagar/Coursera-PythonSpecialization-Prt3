import re
fname=input("enter file name")
#print("file name is:",fname)
if len(fname)<1: fname="regex_sum_42.txt"
fhand=open(fname)
k=[]
for line1 in fhand:
	line=line1.rstrip()
	#print(line)
	j=re.findall("[0-9]+",line)
	if len(j)==0:
		continue
	else:
		for i in range(len(j)):
			k.append(j[i])
		#print(j)
#print(k)
add=0
for item in k:
	num=int(item)
	add=add+num
print("add is :",add)
