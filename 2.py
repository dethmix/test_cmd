filename="test.txt"
list=[]
for line in open (filename):
	temp=line.split(",")
	first_name=temp[0]
	second_name=temp[1]
	age=int (temp[2])
	chunk=(first_name,second_name,age)
	list.append(chunk)


print list
#total_age=0
#for first_name, second_name, age in list:
#	print "first_name", first_name
#	print "second_name", second_name
#	print "age", age
#	total_age+=age
#print total_age
