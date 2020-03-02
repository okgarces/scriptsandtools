#Reverse Shuffle Merge Challenge

# Return if a str belongs to a any permutations of str_base
# The methos is compare length of Strings and characters
def is_shuffle(str_cmp, str_base):

	char_visited = []

	if len(str_cmp) == len(str_base):
		for i in str_cmp:
			if not i in char_visited:
				if not str_cmp.count(i) == str_base.count(i):
					return False
				else:
					char_visited.append(i)
	else:
		return False

	return True

def base_str(str):
	print "initial str", str
	str_cpy = ""

	for s in str:
		if not s in str_cpy:
			occ = str.count(s)
			str_cpy += (occ/2)*s

	return str_cpy

def min_order_lex(str_array):
	if len(str_array) > 0:
		return sorted(str_array)[0]
"""	
def order_lex1(str):
	change = True
	num = 0

	while change:
		str_temp= ""
		for i in xrange(len(str)):
			print i, "ini"
			if i < len(str)-1:
				print "STR", str
				if str[i] > str[i+1]:
					print i, "Va en"
					
					if i > 0:
						str_temp = str[:i]
					else:
						str_temp = ""
					
					str_temp += str[i+1]
					str_temp += str[i]
					str_temp += str[i+2:]

					print str[i+2:], "error"

					num+=1
					str = str_temp
					print str


		if num == 0:
			change = False
		else:
			num = 0
"""

def reverse(str):
	return str[::-1]

def merge(str1, str2):
	return str1+str2

def smc(str):
	str = reverse(str)
	len_str_ini = len(str)
	str_base = base_str(str)
	number_of_ite = len_str_ini-len(str_base)

	found_strs = []

	for i in xrange(number_of_ite):
		print "numero", i
		found_str = str[i:i+len(str_base)]
		 
		if is_shuffle(found_str,str_base):
			print "Entro a shuffle"

			if is_shuffle(found_str+found_str, str):
				print "Entro a shuffle 2"
				found_strs.append(found_str)
	print found_strs
	return min_order_lex(found_strs)


#str = raw_input()
str_input = "bbcbccbabcbabcbaaccccaaabcbcaacacbabbbbcabcbbbbacbcaccccbcccbccaaabcabacccbaccccbbababccbccacbaccacbcccacbaaacacbbcbaaabbabbaaccbbbabccbccacacacabaababbcbcccbbcacabcabbbccababbcccacccccabbcbcbbaabbaabacabaabbbbcccccccacabaacbbbbbcbbabccbacbaabccbabccbbabccbacccaaaababccbbbacaacaabcabbbabaabbcbcacbcabcabcacbabaaabbbcbbbcccaaacbcacccaabccabbcbbabbcaacabbcacabcbbaccaabbcccaaaaacbabbbccbbcccbaacaaccbccabaccbaabaacbaaaccbbcabbbacccaccaaccbcccbccacbaacbccbbaabbbaccbacaaabaaabcaacabcaccbbaaabcacacbaaacbccbabbbcbabbaaccccbcacaabacbbabbaccabccbacbabccbbaacacbacaccbacbbbaaabcaccabccaabccabbccbaacacbbbbccabcccaaabbcaccaaaaaaacccabcbaabccacaaaaacacacbbaaabbccaabccbaaccbbcabacaaaaabbbbbababacaaabbbcccbbbcacabaacabcbaaccbabbbabbaccacacaabcabbcaabbacaaacabbaccabcbcccccaacccaaacbcabbcbacabacbaccbccbbbbccbacabacabbbbbbbbccccbccccaabaabbcbacabaababcbbacbcabcccbabbcbcaacbaabbbccbbaccaccbbbccbacbccbcaccbccabacccbbccacbbcacaabaccbbccacbabaccaacbbbcacbbaccbcaaacbbabacacbaababbbacaabcccabbcbabccccaabcaaccbbbcbaababacbcaccaacabcbbbbcabbcccacbcbaccaabcccbcabcbaccbcbcccbccaacbccbaccacbccbabccbccaaaaaabcbacccbbbcbbacbacbabaacbbacacbbabccbccbcbbcbccaabaacccabbbbcbcbaccabcabacabccabbacccbabaccacabcbcbcacbabcccacbbaacbccaabcbaacaabaccaccbbcaabbbaabbbcbcabccabbabaccbbaccacccbabbbabaacbbbbaccaaaaabbcabbbbaabcbacbcccbacbcbbbacbcababbcbcbbbacaabbcaacaacbbbacabaacccaaccaacabbabcabccbbabccabacbccbaacacbacabbcaaccabaacccbcbcbccbbabacbcacbacaaaabbacacbcbbccbbbbccaacaabbabaacbbaaaababcccabcababccacbabbccaaccbccbbabaccacccbbacaaabcbaabbccccaababbcaabcabbccbbcbabcaabcbcbaccaaaaccbccacababbaacbaacbccbacabccabbbbbacbcbabacbaccbcabcbaabbcbcbbaccbabccababcbcbcbabbabbaabccacccbcabaccacbcbcbccbaacaabacbabccabaacbbabcbaccbcabcaaacacbaccccbcabbccccabcbaccabbbababbacabbacacbbaabaaaaababbcbbaabcbcacccbbbaabccaccabcbbbbbaababbbcaacbaaaaabbcbbabbaccbbacacbaaaabbcccbbcbcaacacbbaacaaabaacbaababbcaccaacbacabccabbabaaaacacabbabaabbaaacabccaabacaabcbaabbacaaaaacbbcbcabcacababcbabcbbbaacccbcbcacbbccbcacabcacbbbbcbabcbaaaacb"
str_output = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbaaaababbbbbbbbbbbbcbbbbbccbbbccbccbbccbbbcccbbcccbbccbccbbcccbbcccbccbcccbccbcbccbbbccccbbccbbbbccbcbbbcccbcbcbbcbbbcbcbbbccccbccccbbbbbbbbcbcbccbbbbccbccbcbcbcbbcbcccccccccbcbccbbccbbcbbcbccccbbbbbbccbcbcbccbbbcccbbbcbbbbbbbcbcbbccbccbccbbbbccccccbbcbccccccbbcccbccbbbbccbccbbccbccbcccbbbbcbcccbccbbccbbcbccbccbbbbcbccbccccbbbcbbbbccbcbcccbbbcccbccbbcbccbbbbbccbcbcccbcccbcccccccbbbcbbccbcbbccbccbcccbcccbbccbbbbccccbbccbbcbccbbccbbbbcbbccbccccbccccbbbcbbbbbccbcbcbccbcbbbbbbcbccbbbccbbcccbccbbbccbbccbbcbccbbbcbbbbbcbccccccccbbbbbcbbbbbcbcbbccccccccbbbccbbbcbccbbcccbcbbbbcccccbccbbbbccbbbbbcbbccbccccbcccbcccbccbbbbccccbcccbcbccbcccbcccccbcbbbbcbcbbbbbcccbcbccccbcbbcbbccbcbb"

str_input1= "eggegg"
str_output2 = "egg"

print smc(str_input)

#print order_lex(smc(str))
#order_lex1(str)

