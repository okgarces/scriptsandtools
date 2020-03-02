sum = lambda x,y: x+y

#i = input()
#k = input()

#print(sum(i,k))

num_lines = input()

for i in range(0,num_lines):
	two = raw_input()
	
	a = int(two.split(' ')[0])
	b = int(two.split(' ')[1])

	print(sum(a,b))