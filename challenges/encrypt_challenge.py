# TODO todo
# YYY Todo


message = raw_input()
message_len = len(message)


root = pow(message_len,0.5)

if(message_len%root != 0):
	floor_fun = int(root)
	ceil_fun = floor_fun+1
else:
	floor_fun = int(root)
	ceil_fun = floor_fun

if(not ceil_fun*floor_fun > message_len-ceil_fun):
	ceil_fun+=1

new_row = []
new_col = []

count = 0
for i in message:
	if(count < ceil_fun):
		new_col.append(i)
		count+=1
	else:

		new_row.append(new_col)
		new_col = [i]
		count=1
new_row.append(new_col)

new_string = ""
for j in xrange(ceil_fun):
	for i in new_row:
		if(len(i) > j):
			new_string+=i[j]
	new_string+=" "


print new_string
