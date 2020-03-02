
#Growth, plant on Spring
# Initial size = 1

def how_to_growth(initial, num_cycles, size):

	if(initial==num_cycles+1):
		return size

	if(initial==0):
		return how_to_growth(initial+1, num_cycles, size)
	else:
		if(initial%2==0):
			return how_to_growth(initial+1, num_cycles, size+1)
		else:
			return how_to_growth(initial+1,num_cycles, size*2)



#First get the Number of Samples
num_samples = input()



for i in xrange(num_samples):
	num_cycles = input()
	print how_to_growth(0, num_cycles,1)
